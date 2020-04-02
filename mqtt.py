import paho.mqtt.client as mqtt
import json
import time
import random
from datetime import datetime, timezone
import sqlite3 as sql

db = "observations.db"

with sql.connect(db) as con:
    c = con.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS observations (
            instant TEXT,
            topic TEXT
            value REAL,
            unit TEXT
        );""")


def on_connect(mqttc, obj, flags, rc):
    print("Connected with result code " + str(rc))
    mqttc.subscribe('foo/jeremy')


def on_message(mqttc, obj, msg):
    # print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    try:
        obs = json.loads(msg.payload)
        obs["instant"] = datetime.fromisoformat(obs["instant"]).astimezone(timezone.utc).isoformat()
        print(obs)

        with sql.connect(db) as con:
            c = con.cursor()
            c.execute(
                "INSERT INTO observations VALUES(?, ?, ?, ?)",
                (obs["instant"], msg.topic, obs["value"], obs["unit"])
            )

            print(c.execute("SELECT count(*) from observations").fetchall())

    except Exception as ex:
        print(msg.topic, msg.payload, ex)


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))
    pass


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)


def next_value_temperature(d):
    for i in range(d):
        x = random.uniform(-10.0, 50.9)
    return "%.1f" % x


def payload():
    random_temperature = next_value_temperature(1)
    msg = {
        "instant": datetime.now(timezone.utc).isoformat(),
        "value": random_temperature,
        "unit": "°C"
    }
    return msg


mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# mqttc.on_log = on_log
mqttc.connect("mqtt.eclipse.org", 1883, 60)
mqttc.loop_start()

while True:
    infot = mqttc.publish("foo/jeremy", json.dumps(payload()), qos=2)
    infot.wait_for_publish()
    time.sleep(5)
