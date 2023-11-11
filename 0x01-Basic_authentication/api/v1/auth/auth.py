#!/usr/bin/env python3
"""Create a class to manage authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Implement authentication system for app"""

    def __init__(self):
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return False for now"""
        return False

    def authorization_header(self, request=None) -> str:
        """Return None for now"""
        return None

    def current_user(Self, request=None) -> TypeVar('User'):
        """Return None for now"""
        return None
