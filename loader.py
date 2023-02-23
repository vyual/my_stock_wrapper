from api.main import MyStockWrapper
from data.config import load_config

config = load_config()
wrapper = MyStockWrapper(login=config.misc.login_ms, password=config.misc.password_ms)
