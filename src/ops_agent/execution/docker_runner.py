import docker
from docker.errors import ContainerError


class DockerSandbox:

    def __init__(self):
        self.client = docker.from_env()

    def run_command(self, command: str) -> str:
        try:
            raw_output = self.client.containers.run(
                image="ubuntu:latest",
                command=command,
                remove=True,
                stdout=True,
                stderr=True
            )

            return raw_output.decode("utf-8")

        except ContainerError as e:
            error_logs = e.stderr.decode("utf-8")
            return f"Command failed with exit code {e.exit_status}:\n{error_logs}"
        except Exception as e:
            return f"System Error executing command: {str(e)}"
        