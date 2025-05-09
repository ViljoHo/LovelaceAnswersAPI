from locust import events
from environs import Env
import requests

from base_users import BaseTestUser

env = Env()
env.read_env()

API_KEY = env("API_KEY_SERVERS_ADMIN")


TARGET_HOSTS = [
    "192.168.1.221",
    "192.168.1.128",
    "192.168.1.113",
    "192.168.1.11",
    "192.168.1.171",
    "192.168.1.82",
    "192.168.1.16",
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
    api_amount = 7


class TestUser2(BaseTestUser):
    index = 1
    target_ip = TARGET_HOSTS[1]
    api_amount = 7


class TestUser3(BaseTestUser):
    index = 2
    target_ip = TARGET_HOSTS[2]
    api_amount = 7


class TestUser4(BaseTestUser):
    index = 3
    target_ip = TARGET_HOSTS[3]
    api_amount = 7


class TestUser5(BaseTestUser):
    index = 4
    target_ip = TARGET_HOSTS[4]
    api_amount = 7


class TestUser6(BaseTestUser):
    index = 5
    target_ip = TARGET_HOSTS[5]
    api_amount = 7


class TestUser7(BaseTestUser):
    index = 6
    target_ip = TARGET_HOSTS[6]
    api_amount = 7
