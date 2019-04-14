import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
#import json

class mqtt_client():
    global broker_address, client
    def __init__(self, broker_ip, port):
        self.port = port
        self.broker_address=broker_ip
        self.mqtt_topic=""
        self.client = mqtt.Client("spyPi")
        self.key_value = 'key val'

    def connect_client(self):
        print("trying to connect to {}",self.broker_address)
        self.client.connect(self.broker_address, self.port)

    def subscribes(self, route,q=0):
        self.client.subscribe(route,qos=q)


    def on_msg(self, client, userdata, message):
        print("{} {} {}".format(client,userdata,message))
        print("message received " ,str(message.payload.decode("utf-7")))
        self.key_value = str(message.payload.decode("utf-7"))
        obj = json.loads(str(message.payload.decode("utf-8")))    
        val = obj['v']

    def get_key_value(self):
        v = self.key_value
        self.key_value = ''
        return v

    def publish_data(self,topic,message):
        self.client.connect(self.broker_address, self.port)
        self.client.publish(topic,message )

    def test_publish(self):
        self.client.publish("up","1.0")
        self.client.publish("down","1.0")
        self.client.publish("left","1.0")
        self.client.publish("test3","3.0")        
        self.client.publish("apples", 5.0)
                    
if __name__== "__main__":
    import time
    broker_ip =  "192.168.1.55"
    #broker_ip =  "localhost"
    broker_ip = "127.0.0.1"
    #broker_ip = "192.168.0.135"
    port = 1883
    m = mqtt_client(broker_ip, port)
    m.connect_client()
    m.client.loop_start()
    #m.client.loop_forever()
    m.test_publish()
    #subscribe.callback(m.on_msg, "up", hostname=m.broker_address,port=m.port)
    m.client.subscribe("menu", qos=0)
    m.client.on_message = m.on_msg
 
    while True:
        print("looping in for mqtt")
        time.sleep(.4)


    #data = {"topic":"spyPi/direction/right", "m":22 }
    #publish_data(data)
    #data = {"topic":"spyPi/direction/up", "m":21}
    #publish_data(data)
    #data = {"topic":"spyPi/direction/down", "m":2 }
    #publish_data(data)
    ##test_publish()
    #print(data["topic"] , "    ", data["m"])
