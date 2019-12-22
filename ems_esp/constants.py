"""constants for ems esp """

CONSTANTS = {
    "return temp sensor": {
        "value": "retTemp",
        "name": "Return Temperature",
        "icon": "mdi:flash",
        "unit": "°C",
    },
    "flow temp sensor": {
        "value": "curFlowTemp",
        "name": "Current Flow Temperature",
        "icon": "mdi:flash",
        "unit": "°C",
    },
    "warm water flow sensor": {
        "value": "wWCurTmp",
        "name": "Current Warm Water Temperature",
        "icon": "mdi:flash",
        "unit": "°C",
    },
    "warm water sensor": {
        "value": "boilTemp",
        "name": "Current Boiler Temperature",
        "icon": "mdi:flash",
        "unit": "°C",
    },
    "thermostat sensor": {
        "value": "thermostat_currtemp",
        "name": "Current Room Temperature",
        "icon": "mdi:flash",
        "unit": "°C",
    },
    "thermostat setting": {
        "value": "thermostat_seltemp",
        "name": "Current Set Temperature",
        "icon": "mdi:flash",
        "unit": "°C",
    },
    "warm water setting": {
        "value": "wWSelTemp",
        "name": "Current Warm Water Selected Temperature",
        "icon": "mdi:flash",
        "unit": "°C",
    },
    "burner power setting": {
        "value": "selBurnPow",
        "name": "Burner Max Power",
        "icon": "mdi:flash",
        "unit": "%",
    },
    "burner power sensor": {
        "value": "curBurnPow",
        "name": "Burner current power",
        "icon": "mdi:flash",
        "unit": "%",
    },
    "pump modulation sensor": {
        "value": "pumpMod",
        "name": "Pump Modulation",
        "icon": "mdi:flash",
        "unit": "%",
    },
    "system pressure sensor": {
        "value": "sysPress",
        "name": "System Pressure",
        "icon": "mdi:flash",
        "unit": "bar",
    },
    "flow rate sensor": {
        "value": "wWCurFlow",
        "name": "Tapwater Flow Rate",
        "icon": "mdi:flash",
        "unit": "l/min",
    },
    "tap water mode": {
        "value": "tapwaterActive",
        "name": "Tap Water",
        "icon": "mdi:flash",
        "unit": None,
    },
    "warm water active mode": {
        "value": "wWActivated",
        "name": "Warm Water activated",
        "icon": "mdi:flash",
        "unit": None,
    },
    "3-way valve mode": {
        "value": "wWHeat",
        "name": "3-way valve",
        "icon": "mdi:flash",
        "unit": None,
    },
    "active heating mode": {
        "value": "heatingActive",
        "name": "Heating",
        "icon": "mdi:flash",
        "unit": None,
    },
    "gas valve mode": {
        "value": "burnGas",
        "name": "gas valve",
        "icon": "mdi:flash",
        "unit": None,
    },
    "boiler pump mode": {
        "value": "heatPmp",
        "name": "boiler pump",
        "icon": "mdi:flash",
        "unit": None,
    },
    "boiler circulation pump mode": {
        "value": "wWCirc",
        "name": "boiler circulation pump",
        "icon": "mdi:flash",
        "unit": None,
    },
    "fantilator mode": {
        "value": "fanWork",
        "name": "fantilator",
        "icon": "mdi:flash",
        "unit": None,
    },
    "ignition mode": {
        "value": "ignWork",
        "name": "Ignition",
        "icon": "mdi:flash",
        "unit": None,
    },
    "boiler service code": {
        "value": "ServiceCode",
        "name": "Service Code",
        "icon": "mdi:flash",
        "unit": None,
    },
}

'''
  - platform: mqtt
    state_topic: 'home/ems-esp/boiler_data'
    name: 'Return temperature'
    unit_of_measurement: '°C'
    value_template: '{{ value_json.retTemp }}'
'''
