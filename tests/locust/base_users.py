from locust import HttpUser, task, between, constant, events
import json
from environs import Env

env = Env()
env.read_env()

API_KEY = env("API_KEY_SERVERS_ADMIN")

class BaseQuickstartUser(HttpUser):
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
        self.payload = json.dumps({
            "exercise": f"EXERCISE_{self.index + 1}",
            "instance": f"COURSE_{self.index + 1}",
            "user": f"USER_{self.index + 1}",
            "revision": 1,
            "language_code": "fi-Fi",
            "answerer_ip": "192.0.2.1",
            "given_answer": f"vastaus {self.index + 1}",
            "task_id": "TASK_123",
            "collaborators": f"Aku {self.index + 1}",
            "checked": False,
            "draft": True,
            "evaluation": None,
        })

    @task
    def view_items(self):
        self.client.post("api/answers/textfield/", data=self.payload, headers=self.headers)
    
    # @task
    # def hello_world(self):
    #     self.client.get("api/answers/", headers=self.headers)