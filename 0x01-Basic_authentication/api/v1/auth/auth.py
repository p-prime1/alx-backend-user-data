#!/usr/bin/env python3
from flask import request
"""Module contains the Auth class"""


class Auth:
    """A new class that handles authentication for my flask
    application"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return False

    def authorization_header(self, request=None) -> str:
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        return None
