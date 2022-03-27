
import pyttsx3
import asyncio
import requests
from jokeapi import Jokes

# engine = pyttsx3.init()
#
# def greet():
#     engine.say(
#         "Hello duh testa as long as you believe in yourself "
#         "you can accomplish any thing you desire")

response = requests.get("https://v2.jokeapi.dev/joke/")
response.status_code
response.ok
print(response.text)


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



