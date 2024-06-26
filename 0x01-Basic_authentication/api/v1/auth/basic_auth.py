#!/usr/bin/env python3
''' basic authentication '''
from api.v1.auth.auth import Auth
import binascii
import base64
from models.user import User
from typing import TypeVar


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

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        ''' returns user email and password from base64
        decoded value '''
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(
                ':',
                1)
        return email, password

    def user_object_from_credentials(
            self,
            user_email: str, user_pwd: str) -> TypeVar('User'):
        ''' returns the User instance based on email and password '''
        if user_email is None or user_pwd is None:
            return None
        if not isinstance(user_pwd, str):
            return None
        if not isinstance(user_email, str):
            return None
        users = User.search({"email": user_email})
        if not users:
            return None

        user = users[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        ''' overloads Auth and retrieves User instance for req '''
        if request is None:
            return None

        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        base64_auth_header = self.extract_base64_authorization_header(auth_header)
        if base64_auth_header is None:
            return None

        decoded_auth_header = self.decode_base64_authorization_header(base64_auth_header)
        if decoded_auth_header is None:
            return None

        user_email, user_pwd = self.extract_user_credentials(decoded_auth_header)
        if user_email is None or user_pwd is None:
            return None

        user = self.user_object_from_credentials(user_email, user_pwd)
        return user

