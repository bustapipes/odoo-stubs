from collections import Mapping
from typing import Any

from odoo.addons.base.res.res_users import Users

from .modules.registry import Registry
from .sql_db import Cursor

WRAPPED_ATTRS: Any
INHERITED_ATTRS: Any

class Params:
    args: Any
    kwargs: Any
    def __init__(self, args, kwargs) -> None: ...

class Meta(type):
    def __new__(meta, name, bases, attrs): ...

def attrsetter(attr, value): ...
def propagate(method1, method2): ...
def constrains(*args): ...
def onchange(*args): ...
def depends(*args): ...
def returns(model, downgrade: Any | None = ..., upgrade: Any | None = ...): ...
def downgrade(method, value, self, args, kwargs): ...
def aggregate(method, value, self): ...
def split_context(method, args, kwargs): ...
def model(method): ...
def multi(method): ...
def one(method): ...
def model_cr(method): ...
def model_cr_context(method): ...
def cr(method): ...
def cr_context(method): ...
def cr_uid(method): ...
def cr_uid_context(method): ...
def cr_uid_id(method): ...
def cr_uid_id_context(method): ...
def cr_uid_ids(method): ...
def cr_uid_ids_context(method): ...
def cr_uid_records(method): ...
def cr_uid_records_context(method): ...
def v7(method_v7): ...
def v8(method_v8): ...
def noguess(method): ...
def guess(method): ...
def expected(decorator, func): ...
def call_kw_model(method, self, args, kwargs): ...
def call_kw_multi(method, self, args, kwargs): ...
def call_kw(model, name, args, kwargs): ...

class Environment(Mapping):
    cr: Cursor = ...
    uid: int = ...
    context: dict = ...
    envs: Environments = ...
    @classmethod
    def manage(cls) -> None: ...
    @classmethod
    def reset(cls) -> None: ...
    registry: Registry
    cache: Any
    dirty: Any
    all: Environments
    def __new__(cls, cr: Cursor, uid, context) -> Environment: ...
    def __contains__(self, model_name) -> bool: ...
    def __getitem__(self, model_name): ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __call__(
        self, cr: Cursor | None = ..., user: Any | None = ..., context: Any | None = ...
    ) -> Environment: ...
    def ref(self, xml_id, raise_if_not_found: bool = ...): ...
    @property
    def user(self) -> Users: ...
    @property
    def lang(self): ...
    def do_in_draft(self): ...
    @property
    def in_draft(self): ...
    def do_in_onchange(self): ...
    @property
    def in_onchange(self): ...
    def invalidate(self, spec) -> None: ...
    def invalidate_all(self) -> None: ...
    def clear(self) -> None: ...
    def clear_upon_failure(self) -> None: ...
    def protected(self, field): ...
    def protecting(self, fields, records) -> None: ...
    def field_todo(self, field): ...
    def check_todo(self, field, record): ...
    def add_todo(self, field, records) -> None: ...
    def remove_todo(self, field, records) -> None: ...
    def has_todo(self): ...
    def get_todo(self): ...
    def check_cache(self) -> None: ...
    @property
    def recompute(self): ...
    def norecompute(self) -> None: ...

class Environments:
    envs: Any
    todo: Any
    mode: bool
    recompute: bool
    def __init__(self) -> None: ...
    def add(self, env) -> None: ...
    def __iter__(self): ...
