from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    userEmail:str
    userPassword:str

    model_config = SettingsConfigDict(
        env_file = "/home/tupac/abdo-toggle/toggle-mcp/.env",
        extra = "ignore"
    )


Config = Settings()

# print(Config.userEmail)

