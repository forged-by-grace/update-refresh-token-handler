from pydantic_settings import BaseSettings, SettingsConfigDict
import os


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=os.path.abspath('.env'), env_file_encoding='utf-8')
    
    # Event Streaming Server
    api_event_streaming_host:str
    api_event_streaming_client_id: str

    # Service metadata
    service_name: str

    # Streaming topics    
    api_update_account: str    
    api_update_token: str   
    api_db_url: str 
    
    # Cache credentials
    api_redis_host_local: str
   
settings = Settings()
