#!/usr/bin/env python3
''' filtered_logger.py '''
import logging
import re
from typing import List


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
    ''' returns a log message obfuscated
    - uses regex pattern '''
    pat = '|'.join(fields)
    fv_pat = r'[^' + separator + r']+'
    return re.sub(r'(' + pat + r')=' + fv_pat, r'\1=' + redaction, message)


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
