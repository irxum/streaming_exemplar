"""
See for codebase
https://medium.com/python-point/mqtt-basics-with-python-examples-7c758e605d4

and
https://support.haltian.com/knowledgebase/open-mqtt-data/
for broker

URL      : live-data.haltian.com
Port     : 1883
Password : none
Topic    : cloudext/json/pr/fi/office/#
"""


import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion
import time

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))

mqttBroker ="live-data.haltian.com"
mqttPort = 1883

client = mqtt.Client(CallbackAPIVersion.VERSION2, "umber_exemplar")
client.connect(host=mqttBroker, port=mqttPort) 

client.loop_start()
print("after loop_start")
client.subscribe("cloudext/json/pr/fi/office/#")
client.on_message=on_message 
print("after on_message")
time.sleep(200)
client.loop_stop()