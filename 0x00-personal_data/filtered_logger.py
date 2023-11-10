#!/usr/bin/env python3
"""Create a function - 'filter_datum' that returns obfuscated log messages"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    
    Obfuscate log messages by performing regex substitution

    Args:
    a. fields - Incoming arg of a list of strs rep'ing fields to obfuscate
    b. redaction - Incoming arg of the str to substitute with value of fields
    c: message - Incoming arg of the string rep'ing the log input to obfuscate
    d. separator - Incoming arg for separator character for 'message'

    Returns:
        A log message with the values in 'fields' obfuscated.

    """

    return re.sub(
        r'(?P<field>{})=[^{}]*'.format('|'.join(fields), separator),
        r'\g<field>={}'.format(redaction),
        message
        )
