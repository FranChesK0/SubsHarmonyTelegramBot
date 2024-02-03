import os
import sys

from pydantic_settings import BaseSettings, SettingsConfigDict

root_dir: str = os.path.dirname(os.path.abspath(__file__)).removesuffix(os.path.join("src", "core"))


class BotSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=os.path.join(root_dir, "data", ".env"), env_prefix="BOT_")

    token: str = "xxx"


class DBSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=os.path.join(root_dir, "data", ".env"), env_prefix="DB_")

    host: str = "xxx"
    port: int = 1000
    name: str = "xxx"
    user: str = "xxx"
    password: str = "xxx"


class Settings(BaseSettings):
    debug: bool = "-d" in sys.argv or "--debug" in sys.argv
    root_dir: str = root_dir
    bot: BotSettings = BotSettings()
    db: DBSettings = DBSettings()


settings: Settings = Settings()
