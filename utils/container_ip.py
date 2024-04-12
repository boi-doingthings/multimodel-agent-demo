import docker

def get_container_ip(container_name):
    """Returns the IP address of a Docker container given its name.

    Args:
        container_name (str): The name of the Docker container.

    Returns:
        str: The IP address of the container, or None if not found or on error.
    """

    try:
        client = docker.from_env()
        container = client.containers.get(container_name)
        ip_address = container.attrs['NetworkSettings']['IPAddress']
        return ip_address
    except docker.errors.NotFound:
        print(f"Container '{container_name}' not found")
        return None
    except docker.errors.APIError as e:
        print(f"Docker API error: {e}")
        return None