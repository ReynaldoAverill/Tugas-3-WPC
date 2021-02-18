import paho.mqtt.client as mqtt #import the client1
import time
import random

broker_address="io.adafruit.com"
clientId="Reynaldo Publish" #ID client yang mengirim data
username= "Reynaldo_Averill" #username adafruit
password= "aio_BiWQ24stwQmqN3Ka5PEvMTR82yMm" #token
topic = "sensorsuara" # ganti sesuai key sensor yang mau kalian masukin

#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("hai") #create new instance
client.username_pw_set(username, password)
client.connect(broker_address) #connect to broker
i=0
while True:
    #publish
    client.publish(username+"/feeds/"+topic,i)
    i=random.choice([0,1])
    time.sleep(10)