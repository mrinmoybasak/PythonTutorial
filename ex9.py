# from win32com.client import Dispatch
# #fre news api key - 24fbf74f05cd4b3ba623f06c2c6218fd
# speak = Dispatch("SAPI.SpVoice")
# speak.Speak("I LOve You Manika")



def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(str)

if __name__ == '__main__':
    import requests
    import json
    url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=24fbf74f05cd4b3ba623f06c2c6218fd')

    response = requests.get(url)
    text = response.text
    my_json = json.loads(text)
    for i in range(0, 11):
        speak(my_json['articles'][i]['title'])