import urllib.parse
from cryptography.hazmat.primitives import hashes
from lib.next_auth.next_auth_exceptions import InvalidTokenError


def extract_csrf_info(csrf_string: str) -> [str, str]:
    csrf_token_unquoted = urllib.parse.unquote(csrf_string)
    if "|" not in csrf_token_unquoted:
        raise InvalidTokenError(status_code=401, message="Unrecognized CSRF token format")
    csrf_cookie_token, csrf_cookie_hash = csrf_token_unquoted.split("|")

    return csrf_cookie_token, csrf_cookie_hash


def validate_csrf_info(secret: str, csrf_token: str, expected_hash: str):
    csrf_token_bytes = bytes(csrf_token, "ascii")
    secret_bytes = bytes(secret, "ascii")

    hasher = hashes.Hash(hashes.SHA256())
    hasher.update(csrf_token_bytes)
    hasher.update(secret_bytes)
    actual_hash = hasher.finalize().hex()

    if expected_hash != actual_hash:
        raise InvalidTokenError(status_code=401, message="CSRF hash mismatch")
