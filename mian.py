import os
import json
import http.client
from dotenv import load_dotenv

# os.getenv('api_key')
def configure():
    load_dotenv()
    

def github_activity(username):
    username = input('enter username: ')
    try:
        username = str(username)
    except ValueError as ve:
        print(f'incorrect value: {ve}')
        
        
    try:
        connection = http.client.HTTPConnection('api.github.com')
        
        endpoint = f'/users/{username}/events'
        connection.request('GET', endpoint)
        
        response = connection.getresponse()
        if response.status == 404:
            print(f'user: {username} not found')
            return
        elif response.status != 200:
            print(f'failed to fetch data. HTTP status: {response.status}')
                
    except Exception as e:
        print(f'error : {e}')


if __name__ == '__main__':
    github_activity('dmalanchuk')