from abc import ABC, abstractmethod
from collections import defaultdict
from collections.abc import MutableMapping
from typing import Any, Callable, Generator, Iterable, Literal, Mapping, TypeVar

import werkzeug
from odoo.addons.base.models.res_lang import Lang
from odoo.addons.website.models.website import Website
from werkzeug.datastructures import Headers
from werkzeug.exceptions import NotFound
from werkzeug.middleware.proxy_fix import ProxyFix as ProxyFix_
from werkzeug.routing import Map, Rule
from werkzeug.urls import URL

from .api import Environment
from .models import BaseModel
from .modules.registry import Registry
from .sql_db import Cursor
from .tools._vendor import sessions
from .tools.geoipresolver import GeoIPResolver

_T = TypeVar("_T")

ProxyFix: Callable[..., ProxyFix_]
CORS_MAX_AGE: int
CSRF_FREE_METHODS: tuple[str, ...]
CSRF_TOKEN_SALT: int
DEFAULT_LANG: str

def get_default_session() -> dict[str, Any]: ...

JSON_MIMETYPES: tuple[str, ...]
MISSING_CSRF_WARNING: str
ROUTING_KEYS: set[str]
SESSION_LIFETIME: int
STATIC_CACHE: int
STATIC_CACHE_LONG: int

class SessionExpiredException(Exception): ...

def content_disposition(filename: str) -> str: ...
def db_list(force: bool = ..., host: str | None = ...) -> list[str]: ...
def db_filter(dbs: Iterable[str], host: str | None = ...) -> list[str]: ...
def dispatch_rpc(service_name: str, method: str, params: Mapping): ...
def is_cors_preflight(request: Request, endpoint) -> bool: ...
def serialize_exception(exception: Exception): ...
def send_file(
    filepath_or_fp,
    mimetype: str | None = ...,
    as_attachment: bool = ...,
    filename: str | None = ...,
    mtime: str | None = ...,
    add_etags: bool = ...,
    cache_timeout: int = ...,
    conditional: bool = ...,
) -> werkzeug.Response: ...

class Stream:
    type: str
    data: bytes | None
    path: str | None
    url: str | None
    mimetype: str | None
    as_attachment: bool
    download_name: str | None
    conditional: bool
    etag: bool
    last_modified: float | None
    max_age: int | None
    immutable: bool
    size: int | None
    public: bool
    def __init__(self, **kwargs) -> None: ...
    @classmethod
    def from_path(
        cls, path: str, filter_ext: tuple[str, ...] = ..., public: bool = ...
    ) -> Stream: ...
    @classmethod
    def from_attachment(cls, attachment) -> Stream: ...
    @classmethod
    def from_binary_field(cls, record: BaseModel, field_name: str) -> Stream: ...
    def read(self) -> bytes: ...
    def get_response(
        self,
        as_attachment: bool | None = ...,
        immutable: bool | None = ...,
        content_security_policy: str = ...,
        **send_file_kwargs
    ) -> werkzeug.Response: ...

class Controller:
    children_classes: defaultdict[Any, list]
    @classmethod
    def __init_subclass__(cls) -> None: ...

def route(
    route: str | list[str] | None = ...,
    type: str = ...,
    auth: str = ...,
    methods: list[str] = ...,
    cors: str = ...,
    csrf: bool = ...,
    **kw
): ...

class FilesystemSessionStore(sessions.FilesystemSessionStore):
    def get_session_filename(self, sid: str) -> str: ...
    def save(self, session: Session) -> None: ...
    def get(self, sid: str) -> Session: ...
    def rotate(self, session: Session, env: Environment) -> None: ...
    def vacuum(self, max_lifetime=...) -> None: ...

class Session(MutableMapping):
    can_save: bool
    is_dirty: bool
    is_new: bool
    should_rotate: bool
    sid: str
    def __init__(self, data: dict, sid: str, new: bool = ...) -> None: ...
    def __getitem__(self, item: str): ...
    def __setitem__(self, item: str, value) -> None: ...
    def __delitem__(self, item: str) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterable[str]: ...
    def __getattr__(self, attr: str): ...
    def __setattr__(self, key: str, val) -> None: ...
    def clear(self) -> None: ...
    uid: int | None
    pre_login: str | None
    pre_uid: int
    def authenticate(
        self, dbname: str, login: str | None = ..., password: str | None = ...
    ) -> int: ...
    def finalize(self, env: Environment) -> None: ...
    def logout(self, keep_db: bool = ...) -> None: ...
    def touch(self) -> None: ...

request: Request

def borrow_request() -> Generator[Request, None, None]: ...
def make_request_wrap_methods(attr) -> tuple[Callable, Callable]: ...

class HTTPRequest:
    environ: dict
    def __init__(self, environ: dict) -> None: ...
    def __enter__(self) -> HTTPRequest: ...

HTTPREQUEST_ATTRIBUTES: list[str]

class Response(werkzeug.Response):
    default_mimetype: str
    def __init__(self, *args, **kw) -> None: ...
    @classmethod
    def load(cls, result, fname: str = ...): ...
    template: Any
    qcontext: dict
    uid: int
    def set_default(
        self,
        template: Any | None = ...,
        qcontext: dict | None = ...,
        uid: int | None = ...,
    ) -> None: ...
    @property
    def is_qweb(self) -> bool: ...
    def render(self): ...
    def flatten(self) -> None: ...
    def set_cookie(
        self,
        key: str,
        value: str = ...,
        max_age: Any | None = ...,
        expires: Any | None = ...,
        path: str = ...,
        domain: str | None = ...,
        secure: bool = ...,
        httponly: bool = ...,
        samesite: str | None = ...,
        cookie_type: str = ...,
    ) -> None: ...

class FutureResponse:
    charset: str
    max_cookie_size: int
    headers: Headers
    def __init__(self) -> None: ...
    def set_cookie(
        self,
        key: str,
        value: str = ...,
        max_age: Any | None = ...,
        expires: Any | None = ...,
        path: str = ...,
        domain: str | None = ...,
        secure: bool = ...,
        httponly: bool = ...,
        samesite: str | None = ...,
        cookie_type: str = ...,
    ) -> None: ...

class Request:
    httprequest: werkzeug.Request
    future_response: FutureResponse
    dispatcher: Dispatcher
    params: dict
    registry: Registry | None
    session: Session
    db: str | None
    env: Environment | None
    website: Website
    website_routing: int
    is_frontend: bool
    is_frontend_multilang: bool
    lang: Lang
    def __init__(self, httprequest: werkzeug.Request) -> None: ...
    def update_env(
        self,
        user=...,
        context: dict[str, Any] | None = ...,
        su: bool | None = ...,
    ) -> None: ...
    def update_context(self, **overrides) -> None: ...
    @property
    def context(self) -> dict[str, Any]: ...
    @context.setter
    def context(self, value) -> None: ...
    @property
    def uid(self) -> int: ...
    @uid.setter
    def uid(self, value) -> None: ...
    @property
    def cr(self) -> Cursor: ...
    @cr.setter
    def cr(self, value) -> None: ...
    @property
    def geoip(self) -> dict[str, Any]: ...
    @property
    def best_lang(self) -> str | None: ...
    def csrf_token(self, time_limit: int | None = ...) -> str: ...
    def validate_csrf(self, csrf: str) -> bool: ...
    def default_context(self) -> dict: ...
    def default_lang(self) -> str: ...
    def get_http_params(self) -> dict: ...
    def get_json_data(self): ...
    def make_response(
        self,
        data: str,
        headers: list[tuple[str, Any]] | None = ...,
        cookies: Mapping | None = ...,
        status: int = ...,
    ) -> Response: ...
    def make_json_response(
        self,
        data,
        headers: list[tuple[str, Any]] | None = ...,
        cookies: Mapping | None = ...,
        status: int = ...,
    ) -> Response: ...
    def not_found(self, description: str | None = ...) -> NotFound: ...
    def redirect(
        self, location: URL | str, code: int = ..., local: bool = ...
    ) -> werkzeug.Response: ...
    def redirect_query(
        self,
        location: str,
        query: Mapping[str, str] | Iterable[tuple[str, str]] | None = ...,
        code: int = ...,
        local: bool = ...,
    ) -> werkzeug.Response: ...
    def render(
        self, template: str, qcontext: dict | None = ..., lazy: bool = ..., **kw
    ): ...

class Dispatcher(ABC):
    routing_type: str
    @classmethod
    def __init_subclass__(cls) -> None: ...
    request: Request
    def __init__(self, request: Request) -> None: ...
    @classmethod
    @abstractmethod
    def is_compatible_with(cls, request: Request) -> bool: ...
    def pre_dispatch(self, rule: Rule, args) -> None: ...
    @abstractmethod
    def dispatch(self, endpoint, args): ...
    def post_dispatch(self, response: werkzeug.Response) -> None: ...
    @abstractmethod
    def handle_error(self, exc: Exception) -> Callable: ...

class HttpDispatcher(Dispatcher):
    routing_type: str
    @classmethod
    def is_compatible_with(cls, request: Request) -> Literal[True]: ...
    def dispatch(self, endpoint, args): ...
    def handle_error(self, exc: Exception) -> Callable: ...

class JsonRPCDispatcher(Dispatcher):
    routing_type: str
    jsonrequest: dict
    request_id: object
    def __init__(self, request: Request) -> None: ...
    @classmethod
    def is_compatible_with(cls, request: Request) -> bool: ...
    def dispatch(self, endpoint, args): ...
    def handle_error(self, exc: Exception) -> Callable: ...

class Application:
    @property
    def statics(self) -> dict[str, str]: ...
    def get_static_file(self, url: str, host: str = ...) -> str | None: ...
    @property
    def nodb_routing_map(self) -> Map: ...
    @property
    def session_store(self) -> FilesystemSessionStore: ...
    @property
    def geoip_resolver(self) -> GeoIPResolver | None: ...
    def get_db_router(self, db: str): ...
    def set_csp(self, response: werkzeug.Response) -> None: ...
    def __call__(self, environ: dict, start_response: Callable): ...

root: Application
