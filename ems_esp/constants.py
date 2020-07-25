"""constants for ems esp """

MQTT_TOPICS = [
    "/ems-esp/boiler_data", #0
    "/ems-esp/heartbeat",  #1
    "/ems-esp/tapwater_active ", #2
    "/ems-esp/heating_active ", #3
    "/ems-esp/thermostat_data", #4
    "/ems-esp/mixing_data", #5
    "/ems-esp/sm_data", #6
    "/ems-esp/hp_data", #7
    "/ems-esp/sensors", #8
    "/ems-esp/start", #9
]
    

CONSTANTS_BOILER_POWER = {
    "boiler power sensor": {
        "value": "curBurnPow",
        "topic": MQTT_TOPICS[0],
        "name": "current burner power",
        "icon": "mdi:water-boiler",
        "unit": "kW",
    }
}

CONSTANTS_SENSORS_SENSORS = {
    "active heating mode": {
        "value": "temp_",
        "topic": MQTT_TOPICS[8],
        "name": "extra thermometer",
        "icon": "mdi:thermometer-high",
        "unit": None,
    },
}

CONSTANTS_SENSORS_THERMOSTAT = {
    "thermostat set sensor": {
        "value": "seltemp",
        "topic": MQTT_TOPICS[4],
        "name": "thermostat set temp",
        "icon": "mdi:thermostat",
        "unit": "°C",
    },
    "thermostat current sensor": {
        "value": "currtemp",
        "topic": MQTT_TOPICS[4],
        "name": "Current Room Temperature",
        "icon": "mdi:home-thermometer",
        "unit": "°C",
    },
    "thermostat mode sensor": {
        "value": "mode",
        "topic": MQTT_TOPICS[4],
        "name": "thermostat mode",
        "icon": "mdi:thermostat",
        "unit": None,
    },
}

CONSTANTS_SENSORS_BOILER = {
    "return temp sensor": {
        "value": "retTemp",
        "topic": MQTT_TOPICS[0],
        "name": "Return Temperature",
        "icon": "mdi:thermometer-chevron-up",
        "unit": "°C",
    },
    "flow temp sensor": {
        "value": "curFlowTemp",
        "topic": MQTT_TOPICS[0],
        "name": "Current Flow Temperature",
        "icon": "mdi:thermometer-chevron-down",
        "unit": "°C",
    },
    "warm water flow sensor": {
        "value": "wWCurTmp",
        "topic": MQTT_TOPICS[0],
        "name": "Current Warm Water Temperature",
        "icon": "mdi:thermometer-chevron-down",
        "unit": "°C",
    },
    "warm water sensor": {
        "value": "boilTemp",
        "topic": MQTT_TOPICS[0],
        "name": "Current Boiler Temperature",
        "icon": "mdi:water-boiler",
        "unit": "°C",
    },
    "warm water setting": {
        "value": "wWSelTemp",
        "topic": MQTT_TOPICS[0],
        "name": "Current Warm Water Selected Temperature",
        "icon": "mdi:thermometer-high",
        "unit": "°C",
    },
    "burner power setting": {
        "value": "selBurnPow",
        "topic": MQTT_TOPICS[0],
        "name": "Burner Max Power",
        "icon": "mdi:fire",
        "unit": "%",
    },
    "burner power sensor": {
        "value": "curBurnPow",
        "topic": MQTT_TOPICS[0],
        "name": "Burner current modulation",
        "icon": "mdi:fire",
        "unit": "%",
    },
    "pump modulation sensor": {
        "value": "pumpMod",
        "topic": MQTT_TOPICS[0],
        "name": "Pump Modulation",
        "icon": "mdi:rotate-left",
        "unit": "%",
    },
    "system pressure sensor": {
        "value": "sysPress",
        "topic": MQTT_TOPICS[0],
        "name": "System Pressure",
        "icon": "mdi:water-percent",
        "unit": "bar",
    },
    "flow rate sensor": {
        "value": "wWCurFlow",
        "topic": MQTT_TOPICS[0],
        "name": "Tapwater Flow Rate",
        "icon": "mdi:water-pump",
        "unit": "l/min",
    },
    "tap water mode": {
        "value": "tapwaterActive",
        "topic": MQTT_TOPICS[4],
        "name": "Tap Water",
        "icon": "mdi:water-pump",
        "unit": None,
    },
    "warm water active mode": {
        "value": "wWActivated",
        "topic": MQTT_TOPICS[0],
        "name": "Warm Water activated",
        "icon": "mdi:water-outline",
        "unit": None,
    },
    "3-way valve mode": {
        "value": "wWHeat",
        "topic": MQTT_TOPICS[0],
        "name": "3-way valve",
        "icon": "mdi:valve",
        "unit": None,
    },
    "gas valve mode": {
        "value": "burnGas",
        "topic": MQTT_TOPICS[0],
        "name": "gas valve",
        "icon": "mdi:gas-cylinder",
        "unit": None,
    },
    "boiler pump mode": {
        "value": "heatPmp",
        "topic": MQTT_TOPICS[0],
        "name": "boiler pump",
        "icon": "mdi:rotate-left",
        "unit": None,
    },
    "boiler circulation pump mode": {
        "value": "wWCirc",
        "topic": MQTT_TOPICS[0],
        "name": "boiler circulation pump",
        "icon": "mdi:rotate-left",
        "unit": None,
    },
    "fantilator mode": {
        "value": "fanWork",
        "topic": MQTT_TOPICS[0],
        "name": "fantilator",
        "icon": "mdi:fan",
        "unit": None,
    },
    "ignition mode": {
        "value": "ignWork",
        "topic": MQTT_TOPICS[0],
        "name": "Ignition",
        "icon": "mdi:flash",
        "unit": None,
    },
    "boiler service code": {
        "value": "ServiceCode",
        "topic": MQTT_TOPICS[0],
        "name": "Service Code",
        "icon": "mdi:face-agent",
        "unit": None,
    },
}
#CONSTANTS_SENSORS_BOILER not added sensors
    #"wWComfort": "Eco",
    #"wWDesiredTemp": 70,
    #"selFlowTemp": 39,
    #"wWCircPump": 0,
    #"switchTemp": 0,
    #"flameCurr": 26.2,
    #"heating_temp": 60,
    #"pump_mod_max": 90,
    #"pump_mod_min": 50,
    #"wWStarts": 6630,
    #"wWWorkM": 10059,
    #"UBAuptime": 583905,
    #"burnStarts": 11899,
    #"burnWorkMin": 142146,
    #"heatWorkMin": 132087,
    #"ServiceCodeNumber": 200
