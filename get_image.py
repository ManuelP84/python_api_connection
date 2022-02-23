"""Get image from an API"""

# Utilities
# import json
import requests

def getImage():
    """GET an  image from a URL"""

    url = 'https://i.imgur.com/n9z3sLg.jpg'
    response = requests.get(url, stream=True)   # Make the GET request withouth downloading the content

    with open('image.jpg', 'wb') as file:
        for chunk in response.iter_content():   # Download the content
            file.write(chunk)

    response.close()

if __name__ == '__main__':
    getImage()
