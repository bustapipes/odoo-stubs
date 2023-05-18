from typing import Any, Optional, Union

import werkzeug.contrib.sessions
import werkzeug.wsgi

from .api import Environment
from .sql_db import Cursor

_logger: Any
rpc_request: Any
rpc_response: Any
STATIC_CACHE: Any
_request_stack: Any
request: Union[HttpRequest, JsonRequest]

def replace_request_password(args): ...

NO_POSTMORTEM: Any

def dispatch_rpc(service_name, method, params): ...
def local_redirect(
    path,
    query: Optional[Any] = ...,
    keep_hash: bool = ...,
    forward_debug: bool = ...,
    code: int = ...,
): ...
def redirect_with_hash(url, code: int = ...): ...

class WebRequest:
    httprequest: werkzeug.wrappers.Request
    httpresponse: Response
    disable_db: bool
    endpoint: Any
    endpoint_arguments: Any
    auth_method: Any
    website = Environment()["website"]
    _cr: Cursor
    _uid: int
    _context: dict
    _env: Environment
    _failed: Any
    def __init__(self, httprequest) -> None: ...
    @property
    def cr(self) -> Cursor: ...
    @property
    def uid(self) -> int: ...
    @uid.setter
    def uid(self, val) -> None: ...
    @property
    def context(self) -> dict: ...
    @context.setter
    def context(self, val) -> None: ...
    @property
    def env(self) -> Environment: ...
    @property
    def lang(self): ...
    @property
    def session(self) -> OpenERPSession: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...
    def set_handler(self, endpoint, arguments, auth) -> None: ...
    def _handle_exception(self, exception) -> None: ...
    def _call_function(self, *args, **kwargs): ...
    @property
    def debug(self): ...
    def registry_cr(self) -> None: ...
    @property
    def registry(self): ...
    @property
    def db(self): ...
    def csrf_token(self, time_limit: int = ...): ...
    def validate_csrf(self, csrf): ...
    def redirect(self, url: str, code=302): ...

def route(route: Optional[Any] = ..., **kw): ...

class JsonRequest(WebRequest):
    _request_type: str
    jsonp_handler: Any
    params: Any
    jsonp: Any
    jsonrequest: Any
    context: Any
    def __init__(self, *args): ...
    def _json_response(
        self, result: Optional[Any] = ..., error: Optional[Any] = ...
    ): ...
    def _handle_exception(self, exception): ...
    def dispatch(self): ...

def serialize_exception(e): ...

class HttpRequest(WebRequest):
    _request_type: str
    params: Any
    def __init__(self, *args) -> None: ...
    def _handle_exception(self, exception): ...
    def dispatch(self): ...
    def make_response(
        self, data, headers: Optional[Any] = ..., cookies: Optional[Any] = ...
    ): ...
    def render(
        self, template, qcontext: Optional[Any] = ..., lazy: bool = ..., **kw
    ): ...
    def not_found(self, description: Optional[Any] = ...): ...

addons_module: Any
addons_manifest: Any
controllers_per_module: Any

class ControllerType(type):
    def __init__(cls, name, bases, attrs) -> None: ...

Controller: Any

class EndPoint:
    method: Any
    original: Any
    routing: Any
    arguments: Any
    def __init__(self, method, routing) -> None: ...
    @property
    def first_arg_is_req(self): ...
    def __call__(self, *args, **kw): ...

def routing_map(modules, nodb_only, converters: Optional[Any] = ...): ...

class AuthenticationError(Exception): ...
class SessionExpiredException(Exception): ...

class OpenERPSession(werkzeug.contrib.sessions.Session):
    inited: bool
    modified: bool
    rotate: bool
    def __init__(self, *args, **kwargs) -> None: ...
    def __getattr__(self, attr): ...
    def __setattr__(self, k, v): ...
    db: Any
    uid: Any
    login: Any
    session_token: Any
    def authenticate(
        self,
        db,
        login: Optional[Any] = ...,
        password: Optional[Any] = ...,
        uid: Optional[Any] = ...,
    ): ...
    def check_security(self) -> None: ...
    def logout(self, keep_db: bool = ...) -> None: ...
    def _default_values(self) -> None: ...
    context: Any
    def get_context(self): ...
    def _fix_lang(self, context) -> None: ...
    def save_action(self, action): ...
    def get_action(self, key): ...
    def save_request_data(self) -> None: ...
    def load_request_data(self) -> None: ...

def session_gc(session_store) -> None: ...

class Response(werkzeug.wrappers.Response):
    default_mimetype: str
    def __init__(self, *args, **kw) -> None: ...
    template: Any
    qcontext: Any
    uid: Any
    def set_default(
        self,
        template: Optional[Any] = ...,
        qcontext: Optional[Any] = ...,
        uid: Optional[Any] = ...,
    ) -> None: ...
    @property
    def is_qweb(self): ...
    def render(self): ...
    def flatten(self) -> None: ...

class DisableCacheMiddleware:
    app: Any
    def __init__(self, app) -> None: ...
    def __call__(self, environ, start_response): ...

class Root:
    _loaded: bool
    def __init__(self) -> None: ...
    def session_store(self): ...
    def nodb_routing_map(self): ...
    def __call__(self, environ, start_response): ...
    def load_addons(self) -> None: ...
    def setup_session(self, httprequest): ...
    def setup_db(self, httprequest) -> None: ...
    def setup_lang(self, httprequest) -> None: ...
    def get_request(self, httprequest): ...
    def get_response(self, httprequest, result, explicit_session): ...
    def dispatch(self, environ, start_response): ...
    def get_db_router(self, db): ...

def db_list(force: bool = ..., httprequest: Optional[Any] = ...): ...
def db_filter(dbs, httprequest: Optional[Any] = ...): ...
def db_monodb(httprequest: Optional[Any] = ...): ...
def send_file(
    filepath_or_fp,
    mimetype: Optional[Any] = ...,
    as_attachment: bool = ...,
    filename: Optional[Any] = ...,
    mtime: Optional[Any] = ...,
    add_etags: bool = ...,
    cache_timeout=...,
    conditional: bool = ...,
): ...
def content_disposition(filename): ...

class CommonController(Controller):
    def jsonrpc(self, service, method, args): ...
    def gen_session_id(self): ...

root: Any
