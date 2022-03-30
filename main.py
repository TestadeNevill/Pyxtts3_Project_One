
import pyttsx3
import requests
# import json


engine = pyttsx3.init()


payload = {'type': 'twopart'}
response = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,"
                        "explicit&type=twopart&amount=2", params=payload)

# engine.say(response.json())

print(response.json())

#
# jokes_data = response.
# json_data = json.loads(jokes_data)
# print(json_data)


class Joke:

    def __init__(self, setup, delivery) -> None:
        self.setup = setup
        self.delivery = delivery

    def __str__(self) -> str:
        return f"setup {self.setup} delivery {self.delivery}"


# pyttsx3.speak(Joke)
