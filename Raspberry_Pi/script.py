import requests
import json
import os
import time
from datetime import datetime


token_headers = {'Authorization': 'Token xxxxxx'}

while(1):
    # get devices
    r = requests.get('URL/get_device/', headers=token_headers)
    list_device = r.json()
    print(list_device)
    humidity_data = []

    for device in list_device:
        if device["status"]:
            id = device["id"]
            type = device["type"]
            port = device["gpio"]
            count = 2
            command = "python3 AWS_DHT_RPI.py --topic device/" + str(id) + "/data --ca_file ~/Desktop/mqtt/AmazonRootCA1.pem --cert ~/Desktop/mqtt/certificate.pem.crt --key ~/Desktop/mqtt/private.pem.key " \
                      "--endpoint a3vf4f15xaiiy7-ats.iot.eu-west-3.amazonaws.com" \
                      + " --gpio " + str(port) + " --device_id " + str(id) + " --count " + str(count)
            os.system(command)

    time.sleep(10)


