#!/usr/bin/env python3
"""Module contains a filter datum that returns an obfuscated message"""
from typing import List
import re, logging


def filter_datum(fields: List[str], redaction: str, message: str,
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
    parts: List[str] = message.split(seperator)
    for i, part in enumerate(parts):
        for field in fields:
            if part.startswith(field + '='):
                parts[i] = re.sub(r'=(.+)$', f'={redaction}', part)
    return (seperator.join(parts))


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPERATOR = ";"

    def __init__(self, fields):
        self.fields = fields
        super(RedactionFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        obfuscated_message = filter_datum(self.fields, self.REDACTION, record.getMessage(), self.SEPERATOR)
        record.message = obfuscated_message
        return super().format(record)
