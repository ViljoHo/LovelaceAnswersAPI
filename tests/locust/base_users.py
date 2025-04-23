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
UPPER_LIMIT = {1: 1399, 4: 349, 7: 199}

GIVEN_ANSWERS = [
    "correct answer",
    "incorrect answer 1",
    "incorrect answer 2",
    "incorrect answer 3",
    "incorrect answer 4",
]


class BaseUser(HttpUser):
    abstract = True
    wait_time = constant(2)
    index = None
    target_ip = None
    api_amount = None

    def on_start(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-Target-Host': self.target_ip,
            'X-API-KEY': API_KEY,
        }


class BaseTestUser(BaseUser):
    abstract = True

    def create_textfield_payload(self):
        payload = json.dumps(
            {
                "exercise": f"{random.choice(EXERCISES)}",
                "instance": f"{random.choice(INSTANCES)}",
                "user": f"{USERS[random.randint(0, UPPER_LIMIT.get(self.api_amount))]}_API_{self.index + 1}",
                "revision": 1,
                "language_code": "fi-Fi",
                "answerer_ip": "192.0.2.1",
                "given_answer": f"{random.choice(GIVEN_ANSWERS)}",
                "task_id": "TASK_123",
                "checked": False,
                "draft": True,
                "evaluation": None,
            }
        )

        return payload

    def create_multiplechoice_payload(self):
        payload = json.dumps(
            {
                "exercise": f"{random.choice(EXERCISES)}",
                "instance": f"{random.choice(INSTANCES)}",
                "user": f"{USERS[random.randint(0, UPPER_LIMIT.get(self.api_amount))]}_API_{self.index + 1}",
                "revision": 1,
                "language_code": "fi-Fi",
                "answerer_ip": "192.0.2.1",
                "chosen_answer": f"Chosen_answer_{random.randint(1, 10)}",
                "task_id": "TASK_123",
                "checked": False,
                "draft": True,
                "evaluation": None,
            }
        )

        return payload

    def create_evaluation_payload(self):
        payload = json.dumps(
            {
                "evaluator": f"Evaluator_{random.randint(1, 20)}",
                "correct": True,
                "suspect": False,
                "points": 2,
                "max_points": 5,
                "feedback": "good",
                "comment": "Well done!",
            }
        )

        return payload

    @task
    def post_textfield(self):
        self.client.post(
            "api/answers/textfield/",
            data=self.create_textfield_payload(),
            headers=self.headers,
        )

    @task
    def get_by_user(self):
        self.client.get(
            f"api/users/{USERS[random.randint(0, UPPER_LIMIT.get(self.api_amount))]}_API_{self.index + 1}/answers/",
            headers=self.headers,
            name="/api/users/:USER_ID/answers/",
        )

    @task
    def post_get_delete_evaluation(self):
        response = self.client.post(
            "api/answers/multiplechoice/",
            data=self.create_multiplechoice_payload(),
            headers=self.headers,
        )
        if response.status_code != 201:
            return

        location = response.headers.get('Location')
        if not location:
            return

        location = location.lstrip("/")

        self.client.put(
            f"{location}evaluation/",
            data=self.create_evaluation_payload(),
            headers=self.headers,
            name="/api/answers/:ANSWER_ID/evaluation/",
        )

        self.client.get(
            f"{location}evaluation/",
            headers=self.headers,
            name="/api/answers/:ANSWER_ID/evaluation/",
        )

        self.client.delete(
            f"{location}evaluation/",
            headers=self.headers,
            name="/api/answers/:ANSWER_ID/evaluation/",
        )
