from langchain_core.tools import tool
from .schemas import PingHostInput, ScanPortInput, HttpCheckInput
from ops_agent.execution.docker_runner import DockerSandbox


@tool(args_schema=PingHostInput)
def ping_host(hostname: str) -> str:
    """
    Use this tool to check if a server or IP address is reachable over the network.
    """
    sandbox = DockerSandbox()

    command = f"ping -c 4 {hostname}"

    return sandbox.run_command(command)


@tool(args_schema=ScanPortInput)
def scan_port(hostname: str, port: int) -> str:
    """
    Scans a specific TCP port on a host to see if it is open.
    """
    sandbox = DockerSandbox()

    command = f"nc -z -v -w 2 {hostname} {port}"

    return sandbox.run_command(command)


@tool(args_schema=HttpCheckInput)
def check_web_service(url: str) -> str:
    """
    Checks the HTTP status of a website URL to see if it is online and returning a valid response.
    """
    sandbox = DockerSandbox()

    command = f"wget -q -S --spider {url}"

    return sandbox.run_command(command)