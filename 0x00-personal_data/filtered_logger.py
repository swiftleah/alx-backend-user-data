#!/usr/bin/env python3
''' filtered_logger.py '''
import logging
import re
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
    ''' returns a log message obfuscated
    - uses regex pattern '''
    pat = '|'.join(fields)
    fv_pat = r'[^' + separator + r']+'
    return re.sub(r'(' + pat + r')=' + fv_pat, r'\1=' + redaction, message)


def get_logger() -> logging.Logger:
    ''' returns logger.Logger object for user data '''
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    stream_handler = StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        ''' initialization: accepts list of str(fields) '''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        ''' formats the log records '''
        msg = super(RedactingFormatter, self).format(record)
        return(filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR))
