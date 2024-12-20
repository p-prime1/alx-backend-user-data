#!/usr/bin/env python3
"""Module contains the Auth class for handling authentication
    in a flask application
"""


from flask import request
from typing import List, TypeVar, Any


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
        if not path or not excluded_paths:
            return True
        normalized_path = path if path.endswith('/') else f"{path}/"
        return normalized_path not in excluded_paths

    def authorization_header(self, request=None) -> Any:
        """
        Retrieves the Authorization header from a Flask request object.

        Args:
            request: The Flask request object.

        Returns:
            str: The value of Authorization header if available,
                otherwis None.
        """
        if request is None:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> Any:
        """
        Retrieves the current user based on the request.

        Args:
            request: The Flask request object.

        Returns:
            TypeVar: The current user object or None if not available.
        """
        return None
