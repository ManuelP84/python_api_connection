"""GitHub API connection"""

# Utilities
import requests
from decouple import config


# 1. Create the Oauth app to get the client_id and client_secret
# client_id = 'xxxxxxxxxxxxxxxxxx'
# client_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# 2. To get the code 
# https://github.com/login/oauth/authorize?client_id=b3ecef0556ca8e471413&scope=repo
# Login in Github and get the code from the URL
# code='xxxxxxxxxxxxxxx'

# 3. To get the access token
# url = 'https://github.com/login/oauth/access_token'
# Run the script -> get_access_token()
# Get the access token from the response.json()

client_id = config("client_id")
client_secret = config("client_secret")
code = config("code")
access_token = config("access_token")

def get_access_token():
    """Get the acces token"""
    
    url = 'https://github.com/login/oauth/access_token'
    headers = {'Accept': 'application/json'}
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_json = response.json()

        access_token = response_json['access_token']
        print(access_token)


def get_repos():
    """Get the user repositories names"""

    # Endpoint to get the user repos
    url = 'https://api.github.com/user/repos'
    headers = {'Authorization': 'token '+ access_token}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        payload = response.json()

        for project in payload:
            name = project['name']
            print(name)
    else:
        print(response.content)


def create_repo():
    """Create a new repositorie"""

    url = 'https://api.github.com/user/repos'
    payload = {'name': 'python_api_connection'}
    headers = {
        'Accept': 'application/json',
        'Authorization': 'token ' + access_token    
    }

    response = requests.post(url, headers=headers, json=payload)

    if requests.status_codes == 200:
        print(response.json())
    else:
        print(response.content)


if __name__ == '__main__':
    """Main function"""

    # get_access_token()
    # get_repos()
    # create_repo()
