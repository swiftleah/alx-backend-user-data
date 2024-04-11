#!/usr/bin/env python3
''' encrypting passwords '''
import bcrypt


def hash_password(password: str) -> bytes:
    ''' returns salted, hashes password - byte string '''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    ''' checks if pswd is valid '''
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
