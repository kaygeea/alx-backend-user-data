#!/usr/bin/env python3
"""Implement password encryption"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash and salt a password.

    Arg:
        password (str) - incoming argument for the password str to be hashed.

    Returns:
        A salted, hashed password as a byte string
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check the validity of an inputed password by comparing with that hashed
    version

    Args:
        hashed_password - incoming arg for the hashed version of a password
        password - incoming arg for the string version of password

    Returns:
        A boolean based on whether the inputed password is valid or not.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
