#!/usr/bin/env python3
"""Implement password encryption"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash and salt a password.

    Arg:
        password (str): incoming argument for the password str to be hashed.

    Returns:
        A salted, hashed password as a byte string
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
