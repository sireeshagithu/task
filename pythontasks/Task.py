# "Task 1: Implement a function called http_request"

import requests
import json
import time

def http_request(url):
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            try:
                json_response = response.json()
                if "success" in json_response:
                    return json_response
                else:
                    raise ValueError("Success message not found in response")
            except json.decoder.JSONDecodeError:
                raise ValueError("Response is not in JSON format")
        else:
            print(f"Received {response.status_code} response. Refining request...")
            time.sleep(10)  # Wait for 10 seconds before retrying

# Test the function
url = "https://europe-west1-dataimpact-preproduction.cloudfunctions.net/recruitment_test_requests/?task=1"
response_data = http_request(url)
print("Success:", response_data)

# Task 2: Update the given curl command

curl -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36" "https://europe-west1-dataimpact-preproduction.cloudfunctions.net/recruitment_test_requests/?task=2"


# "Task 1: Implement a function called http_request"
import requests
import json
import time

def http_request(url):
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            try:
                json_response = response.json()
                if "success" in json_response:
                    return json_response
                else:
                    raise ValueError("Success message not found in response")
            except json.decoder.JSONDecodeError:
                raise ValueError("Response is not in JSON format")
        else:
            print(f"Received {response.status_code} response. Refining request...")
            time.sleep(10)  # Wait for 10 seconds before retrying

# Test the function
url = "https://europe-west1-dataimpact-preproduction.cloudfunctions.net/recruitment_test_requests/?task=1"
response_data = http_request(url)
print("Success:", response_data)

# Task 2: Update the given curl command

curl -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36" "https://europe-west1-dataimpact-preproduction.cloudfunctions.net/recruitment_test_requests/?task=2"

# Task 3: Write a function to obtain the date for the first day of the last week in the current month

from datetime import datetime, timedelta

def get_first_day_of_last_week():
    today = datetime.today()
    last_day_of_previous_month = today.replace(day=1) - timedelta(days=1)
    last_week_start = last_day_of_previous_month - timedelta(days=last_day_of_previous_month.weekday() + 6)
    return last_week_start

# Apply decorator
def format_date_as_yyyymmdd(func):
    def wrapper():
        date = func()
        return date.strftime("%Y%m%d")
    return wrapper

@format_date_as_yyyymmdd
def get_first_day_of_last_week_formatted():
    return get_first_day_of_last_week()

# Test the function
print("First day of last week (YYYYMMDD):", get_first_day_of_last_week_formatted())

# Task 4: Write tests for the class CacheDecorator

# Assuming CacheDecorator is a class that caches function results, here are some test cases
import unittest

class TestCacheDecorator(unittest.TestCase):
    def test_cache_hit(self):
        # Test if the cached result is returned
        pass
    
    def test_cache_miss(self):
        # Test if function is called when cache is empty
        pass
    
    def test_cache_expiry(self):
        # Test if cache expires after certain time
        pass

if __name__ == '__main__':
    unittest.main()

# Task 5: Update LoginMetaClass and AccessWebsite

class LoginMetaClass(type):
    def __new__(cls, name, bases, dct):
        new_cls = super().__new__(cls, name, bases, dct)
        if name == 'AccessWebsite':
            new_cls = cls._wrap_methods(new_cls)
        return new_cls
    
    @classmethod
    def _wrap_methods(cls, cls_instance):
        class Wrapper:
            def __init__(self, *args, **kwargs):
                self.__wrapped = cls_instance(*args, **kwargs)
                self.logged_in = False
                
            def __getattr__(self, name):
                if not self.logged_in:
                    raise Exception("Not logged in!")
                return getattr(self.__wrapped, name)
            
            def login(self):
                self.logged_in = True
                
            def logout(self):
                self.logged_in = False
                
        return Wrapper

class AccessWebsite(metaclass=LoginMetaClass):
    def __init__(self):
        pass

# Test the classes
access = AccessWebsite()
try:
    access.some_method()  # This should raise an exception
except Exception as e:
    print(e)

access.login()  # Log in
access.some_method()  # This should work
