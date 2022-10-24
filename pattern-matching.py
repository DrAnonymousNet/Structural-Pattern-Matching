import requests
from http import HTTPStatus


class Post:
    #__match_args__ = ("userId", "post_id", "title", "body")
    def __init__(self, userId, id, title, body):
        self.userId = userId
        self.title = title
        self.body = body
        self.post_id = id

class Post2:
    pass


def main(response):
    post = Post(**response.json())
    match post:
        case Post(4 | 5):
            print("Pattern 1")
        case Post(1 | 2, id) if id >= 2:
            print("Pattern 2")
        case Post(1 | 2, id) if id == 1:
            print("Pattern 3")
        case _:
            print("No pattern matches the response status code !")


def main(response):
   post_data = response.json()
   
   match post_data:
        case {"user_id":1, **others}:
            print("Pattern 1 matched ", **others)
        case {"userId":user_id, "id":post_id, **others} if user_id < post_id:
            print("pattern 2 matched", others)
        case {"userId":user_id, "id":1|2|3, **others} if "title" in others.keys():
            print("pattern 3 matched")
            print(others)
        case _:
            print("No pattern matched")


def main(response):
   values = [response.status_code, response.encoding, response.json()]
   match values:
       case [status_code, encoding]:
           print("The first pattern matches the subject")
           print(status_code, encoding)
       case [status_code, encoding, response_data] if status_code <= 399:
           print("The second pattern matches the subject")
           print(status_code, encoding, response_data)

#AS PATTERN

def main(response):
    values = [response.status_code, response.encoding, response.json()]
    match values:
        case [int() as status_code, str() as encoding]:
            print("The first pattern matches the subject")
                     
        case [int() as status_code, str() as encoding, str() as response_data]:
            print("The second pattern matches the subject")
 
        case [int() as status_code, str() as encoding, dict() as response_data]:
            print("The Third pattern matches the subject")
    print(f"status_code:{status_code}, encoding:{encoding}, response_data:{response_data}")


#WILDCARD PATTERN

def main(response):
    status_code = response.status_code
    match status_code:
        case 300:
            print("The response is 300")
        case 400:
            print("The response is 400")
        case _:
            print("No pattern matches the response status !")

def main(response):
   values = [response.status_code, response.encoding, response.json()]
   match values:
       case [ _, encoding]:
           print("The first pattern matches the subject")
           print(encoding)
       case [ _, encoding, _ ]:
           print("The second pattern matches the subject")
           print(encoding)

#OR PATTERN

def main(response):
   encoding = response.encoding
   match encoding:
       case "utf-8" | "utf-16" as encoding:
           print(f"The response was encoded with {encoding} encoding scheme")
       case "base64" | "ascii" as encoding:
           print(f"The response was encoded with {encoding} encoding scheme")
       case _:
           print("No pattern matches the response encoding !")

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
#__import__("ipdb").set_trace()
main(response)

#VALUE PATTERN

from http import HTTPStatus
import requests

def main(response):
   match (response.status_code, response.json()):
       case (HTTPStatus.OK.value, body):
           print(f"The response is OK")
       case (HTTPStatus.BAD_REQUEST.value | HTTPStatus.NOT_FOUND.value, _):
           print(f"Bad request or Not found")
       case _:
           print("No pattern matches the response status code !")


response = requests.get("https://jsonplaceholder.typicode.com/posts/0")  #new
main(response)

def main(response):
   match response.json():
       case [last_post]:
           print(last_post)
       case first_post, *_, last_post:
           print("first_post: ", first_post)
           print("last_post:", last_post)
       case _:
           print("No pattern matches the response status code !")


response = requests.get("https://jsonplaceholder.typicode.com/posts")
main(response)


# MAPPING PATTERN

#MATCHING KEYS

def main(response):
   post_data = response.json()
   match post_data:
        case {"user_id":1}:
            print("Pattern 1 matched")
        case {"userId":1, "postId":1}:
            print("pattern 2 matched")
        case {"userId":1, "id":1}:
            print("pattern 3 matched")
        case _:
            print("No pattern matched")
    

#MATCHING VALUES

def main(response):
   post_data = response.json()
   match post_data:
        case {"userId":2}:
            print("Pattern 1 matched")
        case {"userId":user_id, "id":post_id} if user_id < post_id:
            print("pattern 2 matched")
        case {"userId":user_id, "id":1|2|3} if user_id >= 1:
            print("pattern 3 matched")
        case _:
            print("No pattern matched")

#KEY VALUE PAIR

def main(response):
   post_data = response.json()
   match post_data:
        case {"user_id":1, **others}:
            print("Pattern 1 matched ", others)
        case {"userId":user_id, "id":post_id, **others} if user_id < post_id:
            print("pattern 2 matched", others)
        case {"userId":user_id, "id":1|2|3, **others} if "title" in others.keys():
            print("pattern 3 matched")
            print(others)
        case _:
            print("No pattern matched")

#CLASS PATTERN

def main(response):
    post = Post(**response.json())
    match post:
        case Post(4 | 5):
            print("Pattern 1")
        case Post(1 | 2, id) if id >= 2:
            print("Pattern 2")
        case Post(1 | 2, id) if id == 1:
            print("Pattern 3")
        case _:
            print("No pattern matches the response status code !")

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
main(response)



