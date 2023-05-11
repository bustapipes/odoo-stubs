from . import Command
from typing import Any, Optional

class Deploy(Command):
    session: Any
    def __init__(self) -> None: ...
    def deploy_module(self, module_path, url, login, password, db: str = ..., force: bool = ...): ...
    def upload_module(self, server, module_file, force: bool = ..., csrf_token: Optional[Any] = ...): ...
    def authenticate(self, server, login, password, db: str = ...): ...
    def zip_module(self, path): ...
    def run(self, cmdargs) -> None: ...
