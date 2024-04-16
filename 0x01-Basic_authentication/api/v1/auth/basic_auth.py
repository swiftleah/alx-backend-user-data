#!/usr/bin/env python3
''' basic authentication '''
from api.v1.auth.auth import Auth
import binascii
import base64


class BasicAuth(Auth):
    ''' basic authentication class that inherits from Auth '''
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        ''' returns Base64 part of Authorization header '''
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        parts = authorization_header.split(" ")
        if len(parts) != 2:
            return None
        base64_part = parts[1]
        return base64_part

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        ''' returns decoded value of Base64 string '''
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except (binascii.Error, UnicodeDecodeError):
            return None
