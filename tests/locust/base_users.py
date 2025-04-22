from locust import HttpUser, task, between, constant, events
import json
import random
from environs import Env
import generate_data

env = Env()
env.read_env()

API_KEY = env("API_KEY_SERVERS_ADMIN")
EXERCISES = generate_data.read_exercises()
INSTANCES = generate_data.read_instances()
USERS = generate_data.read_users()
GIVEN_ANSWERS = ["correct answer", "incorrect answer 1", "incorrect answer 2", "incorrect answer 3", "incorrect answer 4"]


class BasePostingUser(HttpUser):
    abstract = True
    wait_time = constant(2)
    index = None
    target_ip = None

    def on_start(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-Target-Host': self.target_ip,
            'X-API-KEY': API_KEY,
        }

    def create_payload(self):
        payload = json.dumps(
            {
                "exercise": f"{random.choice(EXERCISES)}",
                "instance": f"{random.choice(INSTANCES)}",
                "user": f"{random.choice(USERS)}_API_{self.index + 1}",
                "revision": 1,
                "language_code": "fi-Fi",
                "answerer_ip": "192.0.2.1",
                "given_answer": f"{random.choice(GIVEN_ANSWERS)}",
                "task_id": "TASK_123",
                "collaborators": f"Collaborator {self.index + 1}",
                "checked": False,
                "draft": True,
                "evaluation": None,
            }
        )

        return payload

    @task
    def post_textfield(self):
        self.client.post(
            "api/answers/textfield/", data=self.create_payload(), headers=self.headers
        )
