from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "autojob"
    POSTGRES_PASSWORD: str = "autojob_dev_2024"
    POSTGRES_DB: str = "autojob"

    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    # MiMo V2.5 (Vision)
    MIMO_API_KEY: str = ""
    MIMO_BASE_URL: str = ""
    MIMO_MODEL: str = "mimo-v2.5"

    # DeepSeek (Text Extraction)
    DEEPSEEK_API_KEY: str = ""
    DEEPSEEK_BASE_URL: str = "https://api.deepseek.com/v1"
    DEEPSEEK_MODEL: str = "deepseek-chat"

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    class Config:
        env_file = ".env"


settings = Settings()
