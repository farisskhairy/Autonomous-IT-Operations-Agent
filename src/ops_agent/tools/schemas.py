from pydantic import BaseModel, Field


class PingHostInput(BaseModel):
    hostname: str = Field(
        description="The IP address or server name to ping, like '192.168.1.1' or 'db-01'"
    )
