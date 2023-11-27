import requests
import json
from socket import timeout
import logging


def hit_endpoint_url(url):
    list = []
    if url != "null":
        response = requests.get(url)
        dump = response.json()
        print(dump["count"])
        # print(dump)
        for link in dump["entries"]:
            print(link["Link"])
            try:
                data = requests.get(link["Link"], timeout=10)
                if data.status_code == 200:
                    print("Status code is  200")

                else:
                    list.append(link["Link"])
                    print("status code is not 200")
                    print(list)

            except requests.exceptions.Timeout:
                logging.error()


hit_endpoint_url("https://api.publicapis.org/entries")
