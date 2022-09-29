from time import time
from decouple import config
from jose import jwt, jwe
from typing import Dict

JWE_SECRET = str(config("JWE_SECRET"))
JWT_SECRET = str(config("JWT_SECRET"))
JWT_ALGORITHM = 'HS512'
JWT_AUDIENCE = 'LeosAudience'
JWT_ISSUER = 'br.com.segment.leo'


def sign_jwt(info: str) -> Dict[str, str]:
    timestamp = int(time.time())
    payload = {
        "iss": JWT_ISSUER,
        "aud": JWT_AUDIENCE,
        "sub": jwe.encrypt(info, JWE_SECRET, algorithm='dir', encryption='A128GCM').decode("utf-8"),
        "iat": timestamp,
        "exp": timestamp * 3600 * 24
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return { "access_token": token }


def decode_jwt(token: str) -> str:
    decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM], audience=JWT_AUDIENCE, issuer=JWT_ISSUER)
    return jwe.decrypt(decoded_token['sub'], JWE_SECRET).decode("utf-8")