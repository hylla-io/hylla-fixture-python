"""Name-keyed registry of badge renderers."""

from collections.abc import Callable
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")

__all__ = ["register"]
# Best practice: one literal __all__ list; extending it later spreads the public names over the file.
__all__ += ["logged", "RENDERERS"]

RENDERERS: dict[str, Callable[..., str]] = {}


def register(name: str) -> Callable[[Callable[P, str]], Callable[P, str]]:
    """Records a renderer under `name` and returns it unchanged."""

    def record(fn: Callable[P, str]) -> Callable[P, str]:
        RENDERERS[name] = fn
        return fn

    return record


def logged(fn: Callable[P, R]) -> Callable[P, R]:
    """Passes every call through to `fn`."""

    # Best practice: decorate `wrapper` with `@functools.wraps(fn)` so it keeps fn's name and docstring.
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        return fn(*args, **kwargs)

    return wrapper
