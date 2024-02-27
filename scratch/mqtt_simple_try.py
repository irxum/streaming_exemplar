"""
From
https://github.com/eclipse/paho.mqtt.python/blob/master/examples/subscribe_simple.py
and
https://support.haltian.com/knowledgebase/open-mqtt-data/
for broker

URL      : live-data.haltian.com
Port     : 1883
Password : none
Topic    : cloudext/json/pr/fi/office/#
"""



import context  # Ensures paho is in PYTHONPATH

import paho.mqtt.subscribe as subscribe

topics = ['#']

host = "live-data.haltian.com"
port_num = 1883

topics = ["cloudext/json/pr/fi/office/#"]
m = subscribe.simple(topics, hostname=host, port=port_num, retained=False, msg_count=2)
for a in m:
    print(a.topic)
    print(a.payload)