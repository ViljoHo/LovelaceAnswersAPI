locust -f .\tests\locust\testing_locust.py --host http://86.50.168.252/ --users 500 --spawn-rate 4 --run-time 110s
locust -f .\tests\locust\testing_locust.py --host http://86.50.168.252/ --users 500 --spawn-rate 4 --run-time 110s --csv .\tests\locust\results\api1\jotain

locust -f .\tests\locust\testing_locust.py --host http://86.50.168.252/ --users 500 --spawn-rate 4 --run-time 110s --csv .\tests\locust\results\api1\jotain --csv-full-history

# locust -f .\tests\locust\locust.py --host http://127.0.0.1:8000/ --users 10 --spawn-rate 1 --run-time 1m
# locust -f .\tests\locust\locust.py --host http://127.0.0.1:8000/ --users 10 --spawn-rate 1 --run-time 1m --headless --html report.html
# locust -f testing_locust.py --host http://86.50.168.252/ --users 10 --spawn-rate 1   
# locust -f .\tests\locust\get_test.py --host http://86.50.168.252/ --users 10 --spawn-rate 1 --headless