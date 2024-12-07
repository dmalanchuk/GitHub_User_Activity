import json
import urllib.request
import urllib.error
import ssl
import certifi


def github_activity(username):
    try:
        username = str(username)
        
        url = f'https://api.github.com/users/{username}/events'
        
        context = ssl.create_default_context(cafile=certifi.where())
        
        headers = {"User-Agent": "Python-CLI-App"}
        request = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(request, context=context) as response:
            if response.status == 404:
                print(f'user: {username} not found')
                return
            elif response.status != 200:
                print(f'Failed to fetch data. HTTP Status: {response.status}')
                return
            
            data = response.read().decode()
            events = json.loads(data)
        
        if not events:
            print(f'No activity found for user {username}')
        else:
            print(f'Latest activity for user {username}:')
            for event in events[:5]:
                print(f'-- {event["type"]} in {event["repo"]["name"]}')
                
    except urllib.error.HTTPError as e:
        print(f'HTTP Error: {e.code} - {e.reason}')
    except urllib.error.URLError as e:
        print(f'URL Error: {e.reason}')
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    username = input('Enter GitHub username: ')
    github_activity(username)
