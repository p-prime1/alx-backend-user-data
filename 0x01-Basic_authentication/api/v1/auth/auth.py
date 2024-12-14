#!/usr/bin/env python3
from flask import request
"""Module contains the Auth class"""


class Auth:
    """
    A class that handles authentication for a Flask application.
    This includes methods to check if authentication is required,
    retrieve authorization headers, and get the current user.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines whether a given path requires authentication.

        Args:
            path(str): The path to check.
            excluded_paths (List[str]): A list of paths that do not
                require authentication

        Returns:
            bool: True if authentication is required, False otherwise
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from a Flask request object.

        Args:
            request: The Flask request object.

        Returns:
            str: The value of Authorization header if available,
                otherwise None.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user based on the request.

        Args:
            request: The Flask request object.

        Returns:
            TypeVar: The current user object or None if not available.
        """
        return None
