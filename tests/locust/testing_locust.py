import time
from locust import HttpUser, task, between, constant, events
from environs import Env
import json
import requests

env = Env()
env.read_env()

api_key = env("API_KEY_SERVERS_ADMIN")

target_hosts = ["192.168.1.221"]
#target_hosts = ["192.168.1.221", "192.168.1.20"]


def clear_database_for_host(host_ip):
    """Clears the answer database for a specific host IP."""
    print(f"--> Clearing database for {host_ip}")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-Target-Host': host_ip,
        'X-API-KEY': api_key,
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
    for host in target_hosts:
        clear_database_for_host(host)


class QuickstartUser1(HttpUser):
    wait_time = constant(2)

    def on_start(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-Target-Host': target_hosts[0],
            'X-API-KEY': api_key,
        }

        self.payload = json.dumps(
            {
                "exercise": "EXERCISE_1",
                "instance": "COURSE_1",
                "user": "USER_1",
                "revision": 1,
                "language_code": "fi-Fi",
                "answerer_ip": "192.0.2.1",
                "given_answer": "vastaus",
                "task_id": "TASK_123",
                "collaborators": "Aku",
                "checked": False,
                "draft": True,
                "evaluation": None,
            }
        )

    @task
    def hello_world(self):
        self.client.get("api/answers/", headers=self.headers)

    @task
    def view_items(self):
        self.client.post(
            "api/answers/textfield/", data=self.payload, headers=self.headers
        )


# class QuickstartUser2(HttpUser):
#     wait_time = constant(2)

#     def on_start(self):
#         self.headers = {
#             'Content-Type': 'application/json',
#             'Accept': 'application/json',
#             'X-Target-Host': target_hosts[1],
#             'X-API-KEY': api_key,
#         }

#         self.payload = json.dumps(
#             {
#                 "exercise": "EXERCISE_2",
#                 "instance": "COURSE_2",
#                 "user": "USER_2",
#                 "revision": 1,
#                 "language_code": "fi-Fi",
#                 "answerer_ip": "192.0.2.1",
#                 "given_answer": "vastaus 2",
#                 "task_id": "TASK_123",
#                 "collaborators": "Aku 2",
#                 "checked": False,
#                 "draft": True,
#                 "evaluation": None,
#             }
#         )

#     @task
#     def hello_world(self):
#         self.client.get("api/answers/", headers=self.headers)

#     @task
#     def view_items(self):
#         self.client.post(
#             "api/answers/textfield/", data=self.payload, headers=self.headers
#         )
