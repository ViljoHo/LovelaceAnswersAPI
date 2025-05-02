from locust import events
from environs import Env
import requests

from base_users import BaseTestUser

env = Env()
env.read_env()

API_KEY = env("API_KEY_SERVERS_ADMIN")


TARGET_HOSTS = [
    "192.168.1.221"
]


def clear_database_for_host(host_ip):
    """Clears the answer database for a specific host IP using the reset endpoint."""
    print(f"--> Clearing database for {host_ip}")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-Target-Host': host_ip,
        'X-API-KEY': API_KEY,
    }

    client = requests.Session()
    client.headers.update(headers)

    try:
        response = client.delete("http://86.50.168.252/testing/reset/answers/")
        if response.status_code == 204:
            print(
                f"Successfully reset database for {host_ip}, status: {response.status_code}"
            )
        else:
            print(f"Reset failed for {host_ip}, status: {response.status_code}")
    except Exception as e:
        print(f"Error connecting to {host_ip}: {e}")


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("A new test is starting")
    for host in TARGET_HOSTS:
        clear_database_for_host(host)


class TestUser1(BaseTestUser):
    index = 0
    target_ip = TARGET_HOSTS[0]
    api_amount = 1