from dataclasses import dataclass
from functools import lru_cache

from environs import Env


@dataclass(frozen=True)
class Miscellaneous:
    login_ms: str
    password_ms: str
    api_key: str


@dataclass(frozen=True)
class Config:
    misc: Miscellaneous


@lru_cache
def load_config() -> Config:
    env = Env()
    env.read_env()

    return Config(
        misc=Miscellaneous(
            login_ms=env.str("LOGIN_MS"),
            password_ms=env.str("PASSWORD_MS"),
            api_key=env.str("API_KEY")
        )
    )
