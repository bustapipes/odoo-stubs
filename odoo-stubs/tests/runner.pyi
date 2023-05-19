import unittest
from typing import Any

class OdooTestResult(unittest.result.TestResult):
    time_start: float | None
    queries_start: int | None
    def __init__(self) -> None: ...
    shouldStop: Any
    def update(self, other) -> None: ...
    def log(
        self,
        level,
        msg,
        *args,
        test: Any | None = ...,
        exc_info: Any | None = ...,
        extra: Any | None = ...,
        stack_info: bool = ...,
        caller_infos: Any | None = ...
    ) -> None: ...
    def getDescription(self, test): ...
    def startTest(self, test) -> None: ...
    def addError(self, test, err) -> None: ...
    def addFailure(self, test, err) -> None: ...
    def addSubTest(self, test, subtest, err) -> None: ...
    def addSkip(self, test, reason) -> None: ...
    def addUnexpectedSuccess(self, test) -> None: ...
    def logError(self, flavour, test, error) -> None: ...
    def getErrorCallerInfo(self, error, test): ...
