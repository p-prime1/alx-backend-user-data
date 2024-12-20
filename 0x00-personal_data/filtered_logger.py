#!/usr/bin/env python3
"""Module contains a filter datum that returns an obfuscated message"""
from typing import List
import re
import logging
import mysql.connector
import os


PII_FIELDS = ("email", "phone", "ssn", "password", "ip")


def get_logger() -> logging.Logger:
    """Function returns a logging.logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger


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

    REDACTION: str = "***"
    FORMAT: str = """[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s:
            %(message)s"""
    SEPERATOR: str = ";"

    def __init__(self, fields: List[str]):
        """Initialzes Formatter from the parent class"""
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """Method obfuscate (hides) sensitive information and format
        using the RedactingFormatter"""
        original_message = super().format(record)
        obfuscated_message = filter_datum(self.fields, self.REDACTION,
                                          original_message, self.SEPERATOR)
        return obfuscated_message


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Function returns a connector to database object"""
    connection = mysql.connector.connect(
            host=os.getenv(PERSONAL_DATA_DB_HOST),
            user=os.getenv(PERSONAL_DATA_DB_USERNAME),
            password=os.getenv(PERSONAL_DATA_DB_PASSWORD),
            database=os.getenv(PERSONAL_DATA_DB_NAME)
            )
    return connection
