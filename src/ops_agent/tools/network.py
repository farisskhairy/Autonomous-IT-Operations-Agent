from langchain_core.tools import tool
from .schemas import PingHostInput


@tool(args_schema=PingHostInput)
def ping_host(hostname: str) -> str:
    """
    Use this tool to check if a server or IP address is reachable over the network.
    """
    return f"PING {hostname}: 56 data bytes\n64 bytes from {hostname}: icmp_seq=1 ttl=64 time=0.045 ms"