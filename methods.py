"""Python API"""

# Utilities
import requests
import json


def api_get():
    """Make a get request to the url"""

    url = 'https://httpbin.org/get'
    args = {
        'name': 'Manuel',
        'company': 'Sofka',
        'english_level': 'B2'
    }
    response = requests.get(url, params=args)    # requests.get() returns a response object

    if response.status_code == 200:
        # print(response.content)   print the html of the url
        content = response.content 
        # print(content)

        with open('data_get.txt', 'wb') as file:
            file.write(content)     

        # If we need to work with json there ara twi ways.
        # 1.

        # response_json = response.json()
        # origin = response_json['origin']
        # print(origin)

        # 2.

        response_json = json.loads(response.text)
        origin = response_json['origin']
        print(origin)


def api_post():
    """Make a post request to the url"""

    url = 'https://httpbin.org/post'
    payload = {
        'name': 'Manuel',
        'company': 'Sofka',
        'english_level': 'B2'
    }
    response = requests.post(url, json=payload)    
    # if we pass the dictionary to json like this (json=payload) it will be serialized
    # if we pass the dictionary to data like this (data=payload) it wont be serialized
    # if we pass the dictionary to data like this (data=json.dups(payload)) it will be serialized
    
    if response.status_code == 200:
        # print(response.content)   print the html of the url
        content = response.content  
        # print(content)

        with open('data_post.txt', 'wb') as file:
            file.write(content)   


def api_post_header():
    """Make a post including a header"""

    url = 'https://httpbin.org/post'
    payload = {
        'name': 'Manuel',
        'company': 'Sofka',
        'english_level': 'B2'
    }
    headers = {
        'Content-Type': 'aplication/json',
        'access-token': '12345'
    }
    response = requests.post(url, json=payload, headers=headers)    
      
    if response.status_code == 200:

        # content = response.content        
        # print(content)   

        # with open('data_post_header.txt', 'wb') as file:
        #     file.write(content) 

        # To read a header
        headers_response = response.headers
        print(headers_response)

        # To read a header value
        server = headers_response['Server']
        print(server)


def api_put():
    """Make a put method"""

    url = 'https://httpbin.org/put'
    payload = {
        'name': 'Manuel',
        'company': 'Sofka',
        'english_level': 'B2'
    }
    headers = {
        'Content-Type': 'aplication/json',
        'access-token': '12345'
    }
    response = requests.put(url, json=payload, headers=headers)    
      
    if response.status_code == 200:
        
        content = response.content        
        print(content)  

        with open('data_put_header.txt', 'wb') as file:
            file.write(content) 


def api_delete():
    """Make a delete method"""

    url = 'https://httpbin.org/delete'
    payload = {
        'name': 'Manuel',
        'company': 'Sofka',
        'english_level': 'B2'
    }
    headers = {
        'Content-Type': 'aplication/json',
        'access-token': '12345'
    }
    response = requests.delete(url, json=payload, headers=headers)    
      
    if response.status_code == 200:
        
        content = response.content        
        print(content)  

        with open('data_delete_header.txt', 'wb') as file:
            file.write(content)


if __name__ == '__main__':
    """Main function"""

    # GET
    api_get()

    # POST
    api_post()

    # PUT
    api_put()

    # DELETE
    api_delete()