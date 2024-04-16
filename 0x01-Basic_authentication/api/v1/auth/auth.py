#!/usr/bin/env python3
''' implements functionality within flask application '''
from typing import List, TypeVar
from flask import request


class Auth:
    ''' manages API authentication '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        ''' returns false '''
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        for excluded_path in excluded_paths:
            if path.rstrip('/') == excluded_path.rstrip('/'):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        ''' returns None '''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        ''' returns None '''
        return None
