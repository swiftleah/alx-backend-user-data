#!/usr/bin/env python3
''' auth file '''
import bcrypt


def _hash_password(password: str) -> bytes:
    ''' returns hashed password '''
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)
