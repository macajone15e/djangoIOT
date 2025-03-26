import json
import requests
import sys
import time
import datetime
import paho.mqtt.client as mqtt
from django.conf import settings
from datetime import date
from django.utils import timezone

from .models import Devices, Temperatures

client = mqtt.Client()

def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print('MQTT: Connected successfully')
        mqtt_client.subscribe('sensors')
    else:
        print('MQTT: Bad connection. Code:', rc)

def on_disconnect(mqtt_client, userdata, rc):
    print("MQTT: Disconnected, Code: ", rc)
    while not client.is_connected :
        time.sleep(5)
        doConnect()

def on_message(mqtt_client, userdata, msg):
    #print(f'Received message on topic: {msg.topic} with payload: {msg.payload}')
    data = json.loads(msg.payload)
    uid = data['id']
    #print("UID: " + uid)
    try:
        device = Devices.objects.get(uid=uid)
        #print("Device:" + device)
        device.lastSeenAt = timezone.now()
        device.save()
        #print("Device updated")
    except Exception as err:
        #print(f"An error occurred: {err}")
        device = Devices()
        device.uid = uid
        device.name = uid
        device.createdAt = timezone.now()
        device.lastSeenAt = timezone.now()
        device.save()
        #print("Device created: " + uid)

def doConnect():
    try:
        client.connect(
            host=settings.MQTT_SERVER,
            port=settings.MQTT_PORT,
            keepalive=settings.MQTT_KEEPALIVE
        )
    except:
        print("MQTT: could not connect")


client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
doConnect()
client.loop_start()