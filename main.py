import json

import pyttsx3
import asyncio
import requests
from jokeapi import Jokes

engine = pyttsx3.init()
#
# def greet():
#     engine.say(
#         "Hello duh testa as long as you believe in yourself "
#         "you can accomplish any thing you desire")
# url = "https://v2.jokeapi.dev/joke/"
payload = {'type':'twopart'}
response = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=twopart&amount=2", params=payload)
# response.status_code
# response.ok
engine.say(response.json())

# async def print_joke():
#     j = await Jokes()
#     joke = await j.get_joke(category=['programming'], blacklist=['nsfw', 'racist', 'religious', 'political', 'sexist'])
#
#
#     if joke["type"] == "twopart":
#         print(joke["setup"])
#         print(joke["delivery"])
#     else:
#         print(joke["joke"])
#
#     print_joke()
jokes_data = response.text
print(jokes_data)
class Joke:
    def __init__(self, setup, delivery) -> None:
        self.setup = setup
        self.delivery = delivery

    def __str__(self) -> str:
        return f"setup {self.setup} delivery {self.delivery}"
jokes = []

for joke in jokes:
    print(joke)
# jsonData = json.loads(requests)
# print(jsonData)
pyttsx3.speak(Joke)
#
# print(jokes)



# async def print_joke():
#     j = await Jokes()
#     joke = await j.get_joke(category=['programming'], blacklist=['nsfw', 'racist', 'religious', 'political', 'sexist'])
#     if joke["type"] == "single":
#         print(joke["joke"])
#     else:
#         print(joke["setup"])
#         print(joke["delivery"])
#     asyncio.run(print_joke())


#
# # engine.say('Sally sells seashells by the seashore.')
# # engine.say('The quick brown fox jumped over the lazy dog.')



