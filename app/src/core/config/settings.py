__all__ = ("settings", )

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class SettingsApp(BaseModel):
    title: str = "FastAPI Short Link"


class SettingsSQLite(BaseModel):
    name: str

    @property
    def url(self) -> str:
        return f"sqlite+aiosqlite:///{self.name}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="backend_",
        env_nested_delimiter="__",
    )

    sqlite: SettingsSQLite
    app: SettingsApp = SettingsApp()


settings = Settings()
