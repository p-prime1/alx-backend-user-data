#!/usr/bin/env python3
"""Module contains a filter datum that returns an obfuscated message"""
from typing import List
import re


def filter_datum(fields: List, redaction: str, message: str,
                 seperator: str) -> str:
    """Function returns obfuscated log message
    Args:
        fields (List): List of strings to be obfucated
        redaction (str): What the fiels would be obfuscated with
        message (str): Represents the log line
        separator (str): The seperating character

    Return:
        (str): Returns the obfuscated message
    """
    parts = message.split(seperator)
    for i, part in enumerate(parts):
        for field in fields:
            if part.startswith(field + '='):
                parts[i] = re.sub(r'=(.+)$', f'={redaction}', part)
    return (seperator.join(parts))
