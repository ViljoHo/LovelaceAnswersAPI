# Main run
locust -f .\tests\locust\testing_1_api.py --host http://86.50.168.252/ --users 500 --spawn-rate 4 --run-time 110s --csv .\tests\locust\results\api1\api1 --csv-full-history
locust -f .\tests\locust\testing_4_api.py --host http://86.50.168.252/ --users 500 --spawn-rate 4 --run-time 110s --csv .\tests\locust\results\api4\api4 --csv-full-history
locust -f .\tests\locust\testing_7_api.py --host http://86.50.168.252/ --users 500 --spawn-rate 4 --run-time 110s --csv .\tests\locust\results\api7\api7 --csv-full-history

# Rerun1
locust -f .\tests\locust\testing_1_api.py --host http://86.50.168.252/ --users 500 --spawn-rate 4 --run-time 110s --csv .\tests\locust\results\api1\rerun1\rerun1 --csv-full-history
locust -f .\tests\locust\testing_4_api.py --host http://86.50.168.252/ --users 500 --spawn-rate 4 --run-time 110s --csv .\tests\locust\results\api4\rerun1\rerun1 --csv-full-history
locust -f .\tests\locust\testing_7_api.py --host http://86.50.168.252/ --users 500 --spawn-rate 4 --run-time 110s --csv .\tests\locust\results\api7\rerun1\rerun1 --csv-full-history

# Rerun2
locust -f .\tests\locust\testing_1_api.py --host http://86.50.168.252/ --users 500 --spawn-rate 4 --run-time 110s --csv .\tests\locust\results\api1\rerun2\rerun2 --csv-full-history
locust -f .\tests\locust\testing_4_api.py --host http://86.50.168.252/ --users 500 --spawn-rate 4 --run-time 110s --csv .\tests\locust\results\api4\rerun2\rerun2 --csv-full-history
locust -f .\tests\locust\testing_7_api.py --host http://86.50.168.252/ --users 500 --spawn-rate 4 --run-time 110s --csv .\tests\locust\results\api7\rerun2\rerun2 --csv-full-history

locust -f .\tests\locust\testing_4_api.py --host http://86.50.168.252/ --users 500 --spawn-rate 4 --run-time 110s --csv .\tests\locust\results\api4\rerun3\rerun3 --csv-full-history

# Headless mode
# locust -f .\tests\locust\testing_locust.py --host http://86.50.168.252/ --users 500 --spawn-rate 4 --run-time 110s --csv .\tests\locust\results\api1\api1 --csv-full-history --headless --html report.html
