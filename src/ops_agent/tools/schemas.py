from pydantic import BaseModel, Field


class PingHostInput(BaseModel):
    hostname: str = Field(
        description="The IP address or server name to ping, like '192.168.1.1' or 'db-01'"
    )


class ScanPortInput(BaseModel):
    hostname: str = Field(
        description="The IP address or server to scan"
    )
    port: int = Field(
        description="The TCP port number to check"
    )

class HttpCheckInput(BaseModel):
    url: str = Field(
        description="The full URL to check, including http:// or https://"
    )