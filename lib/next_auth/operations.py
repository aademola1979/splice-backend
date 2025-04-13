from cryptography.hazmat.primitives.kdf.hkdf import HKDF
import time

from lib.next_auth.next_auth_exceptions import TokenExpiredException


def derive_key(secret: str, length: int, salt: bytes, algorithm, context: bytes) -> bytes:
    hkdf = HKDF(
        algorithm=algorithm,
        length=length,
        salt=salt,
        info=context
    )
    return hkdf.derive(bytes(secret, "ascii"))
    


def check_expiry(exp: int, cur_time: int = None):
    if cur_time is None:
        cur_time = time.time()
    if exp < cur_time:
        raise TokenExpiredException(403, "Token Expired")
