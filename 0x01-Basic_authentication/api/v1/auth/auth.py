#!/usr/bin/env python3
"""Create a class to manage authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Implement authentication system for app"""

    def __init__(self):
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check whether an API endpoint requires authentication

        Args:
            path (str) - Incoming arg for the path to be checked
            excluded_paths (list) - Incoming arg for a list of paths that
                                    require authentication

        Return:
            A boolean indicating whether or not a checked path requires auth
        """
        if excluded_paths and path:
            if path[-1] != '/':
                full_path = path + '/'
                return full_path not in excluded_paths
            else:
                return path not in excluded_paths
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """Return None for now"""
        return None

    def current_user(Self, request=None) -> TypeVar('User'):
        """Return None for now"""
        return None
