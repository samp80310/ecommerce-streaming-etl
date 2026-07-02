import json
import time
import yaml

from kafka import KafkaProducer

from event_generator import generate_order

with open("config/config.yaml") as file:
    config = yaml.safe_load(file)

producer = KafkaProducer(
    bootstrap_servers=config["kafka"]["bootstrap_servers"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

topic = config["kafka"]["topic"]

print("Starting Producer...")

while True:

    order = generate_order()

    producer.send(topic, value=order.model_dump(mode="json"))

    print(order.model_dump_json(indent=2))

    time.sleep(config["producer"]["delay_seconds"])