import requests
import json
from socket import timeout
import logging

Person_ISS = []
Person_Tangoo = []


def space_data(url):
    response = requests.get(url)
    dump = response.json()
    # print(dump["count"])
    print(dump)
    for person in dump["people"]:
        print(person["craft"])
        try:
            if person["craft"] == "ISS":
                Person_ISS.append(person["name"])
                print(Person_ISS)
            else:
                Person_Tangoo.append(person["name"])
                print(Person_Tangoo)

        except requests.exceptions.Timeout:
            logging.error()


space_data("http://api.open-notify.org/astros.json")
