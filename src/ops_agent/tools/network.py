from langchain_core.tools import tool
from .schemas import PingHostInput
from ops_agent.execution.docker_runner import DockerSandbox


@tool(args_schema=PingHostInput)
def ping_host(hostname: str) -> str:
    """
    Use this tool to check if a server or IP address is reachable over the network.
    """
    sandbox = DockerSandbox()

    command = f"ping -c 4 {hostname}"

    return sandbox.run_command(command)