import os

ENV = bool(os.environ.get("ENV", False))

if ENV:
    from Config.legend_config import Config
else:
    if os.path.exists("config.py"):
        from config import Development as Config
