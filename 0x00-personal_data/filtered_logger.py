#!/usr/bin/env python3
''' filtered_logger.py '''
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
