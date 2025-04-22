import time
from locust import HttpUser, task, between, constant, events
from environs import Env
import json
import requests

from base_users import BaseGettingUser

env = Env()
env.read_env()

API_KEY = env("API_KEY_SERVERS_ADMIN")


TARGET_HOSTS = [
    "192.168.1.221",
    "192.168.1.240",
    "192.168.1.173",
    "192.168.1.203",
    "192.168.1.71",
    "192.168.1.121",
    "192.168.1.179",
]





class GettingUser1(BaseGettingUser):
    index = 0
    target_ip = TARGET_HOSTS[0]


class GettingUser2(BaseGettingUser):
    index = 1
    target_ip = TARGET_HOSTS[1]


class GettingUser3(BaseGettingUser):
    index = 2
    target_ip = TARGET_HOSTS[2]


class GettingUser4(BaseGettingUser):
    index = 3
    target_ip = TARGET_HOSTS[3]


class GettingUser5(BaseGettingUser):
    index = 4
    target_ip = TARGET_HOSTS[4]


class GettingUser6(BaseGettingUser):
    index = 5
    target_ip = TARGET_HOSTS[5]


class GettingUser7(BaseGettingUser):
    index = 6
    target_ip = TARGET_HOSTS[6]