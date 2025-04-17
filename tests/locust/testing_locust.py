import time
from locust import HttpUser, task, between, constant, events
from environs import Env
import json
import requests

from base_users import BaseQuickstartUser

env = Env()
env.read_env()

API_KEY = env("API_KEY_SERVERS_ADMIN")

# TARGET_HOSTS = ["192.168.1.221"]
# TARGET_HOSTS = ["192.168.1.221", "192.168.1.20",]
# TARGET_HOSTS = ["192.168.1.221", "192.168.1.20", "192.168.1.69", "192.168.1.225"]
TARGET_HOSTS = ["192.168.1.221", "192.168.1.20", "192.168.1.69", "192.168.1.225", "192.168.1.62", "192.168.1.137", "192.168.1.30"]

def clear_database_for_host(host_ip):
    """Clears the answer database for a specific host IP."""
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
        response = client.get(
            "http://86.50.168.252/api/answers/"
        )
        if response.status_code == 200:
            answers = response.json()
            for answer in answers:
                answer_id = answer.get("id")
                if answer_id:
                    del_response = client.delete(
                        f"http://86.50.168.252/api/answers/{answer_id}/"
                    )
                    print(
                        f"Deleted ID {answer_id} from {host_ip}, status: {del_response.status_code}"
                    )
        else:
            print(
                f"GET /api/answers failed for {host_ip}, status: {response.status_code}"
            )
    except Exception as e:
        print(f"Error connecting to {host_ip}: {e}")


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("A new test is starting")
    for host in TARGET_HOSTS:
        clear_database_for_host(host)


class QuickstartUser1(BaseQuickstartUser):
    index = 0
    target_ip = TARGET_HOSTS[0]


class QuickstartUser2(BaseQuickstartUser):
    index = 1
    target_ip = TARGET_HOSTS[1]

class QuickstartUser3(BaseQuickstartUser):
    index = 2
    target_ip = TARGET_HOSTS[2]

class QuickstartUser4(BaseQuickstartUser):
    index = 3
    target_ip = TARGET_HOSTS[3]

class QuickstartUser5(BaseQuickstartUser):
    index = 4
    target_ip = TARGET_HOSTS[4]

class QuickstartUser6(BaseQuickstartUser):
    index = 5
    target_ip = TARGET_HOSTS[5]

class QuickstartUser7(BaseQuickstartUser):
    index = 6
    target_ip = TARGET_HOSTS[6]
