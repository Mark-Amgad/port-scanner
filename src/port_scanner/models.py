from pydantic import BaseModel, conint

class ScanConfig(BaseModel):
    host: str
    start_port: conint(ge=1, le=65535) = 1
    end_port: conint(ge=1, le=65535) = 1024
    timeout: float = 1.0