
import pyttsx3
import requests


engine = pyttsx3.init()


payload = {'type': 'twopart'}
response = requests.get \
    ("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=twopart&amount=2", params=payload)

engine.say(response.json())


jokes_data = response.text
print(jokes_data)
class Joke:

    def __init__(self, setup, delivery) -> None:
        self.setup = setup
        self.delivery = delivery

    def __str__(self) -> str:
        return f"setup {self.setup} delivery {self.delivery}"


pyttsx3.speak(Joke)
