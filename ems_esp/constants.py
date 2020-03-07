"""constants for [xxxxx] esp """

MQTT_TOPICS = [
    "/ems-esp/boiler_data", #0
    "/ems-esp/heartbeat",  #1
    "/ems-esp/tapwater_active ", #2
]
    
CONSTANTS_SENSORS_SENSORS = {
    "active heating mode": {
        "value": "temp_",
        "topic": MQTT_TOPICS[8],
        "name": "extra thermometer",
        "icon": "mdi:thermometer-high",
        "unit": None,
    },
}

