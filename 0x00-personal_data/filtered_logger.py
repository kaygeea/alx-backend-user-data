#!/usr/bin/env python3
"""Create a function - 'filter_datum' that returns obfuscated log messages"""
import logging
import mysql.connector
import os
import re
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


def get_logger() -> logging.Logger:
    """
    Create a new logger for user data.

    Return:
        A logging.Logger object
    """
    logger = logging.getLogger("user_data")
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.setLevel(logging.INFO)
    logger.propagate = False
    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Create a connector to a database.

    Return:
        A connector the specified database
    """
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME", "")
    db_user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_pwd = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    connection = mysql.connector.connect(
        host=db_host,
        port=3306,
        user=db_user,
        password=db_pwd,
        database=db_name,
    )
    return connection


def main():
    """Logs the information about user records in a table.
    """
    fields = "name,email,phone,ssn,password,ip,last_login,user_agent"
    columns = fields.split(',')
    query = "SELECT {} FROM users;".format(fields)
    info_logger = get_logger()
    connection = get_db()
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            record = map(
                lambda x: '{}={}'.format(x[0], x[1]),
                zip(columns, row),
            )
            msg = '{};'.format('; '.join(list(record)))
            args = ("user_data", logging.INFO, None, None, msg, None, None)
            log_record = logging.LogRecord(*args)
            info_logger.handle(log_record)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = "; "

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Implement format for a LogRecord"""

        log_msg: str = super(RedactingFormatter, self).format(record)
        log_msg_text: str = filter_datum(self.fields, self.REDACTION,
                                         log_msg, self.SEPARATOR)
        return log_msg_text


if __name__ == "__main__":
    main()
