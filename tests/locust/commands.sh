locust -f .\tests\locust\locust.py --host http://127.0.0.1:8000/ --users 10 --spawn-rate 1
# locust -f .\tests\locust\locust.py --host http://127.0.0.1:8000/ --users 10 --spawn-rate 1 --run-time 1m
# locust -f .\tests\locust\locust.py --host http://127.0.0.1:8000/ --users 10 --spawn-rate 1 --run-time 1m --headless --html report.html