"""Session cookies"""

# Utilities
import requests
from decouple import config


def get_session_cookies():
    """Get session cookies from gitHub"""

    url = 'https://api.github.com/users'
    user = config("user")
    passw = config("passw")

    session = requests.session()
    session.auth = (user, passw)

    response = session.get(url)

    if response.ok:
        
        response = session.get('https://github.com/ManuelP84')

        if response.ok:

            print(response.cookies)


if __name__ == '__main__':
    """Main function"""
    
    get_session_cookies()