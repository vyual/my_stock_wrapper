from pathlib import Path

from environs import Env

env = Env()
env.read_env()

LOGIN_MS = env.str("LOGIN_MS")
PASSWORD_MS = env.str("PASSWORD_MS")
