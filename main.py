
import pyttsx3
import requests
import json


engine = pyttsx3.init()


payload = {'type': 'twopart'}
response = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,"
                        "explicit&type=twopart&amount=2", params=payload)


joke_data = response.json()


engine.say(joke_data)

for i in joke_data['jokes']:
    print(i)
pyttsx3.speak(joke_data)









