"""constants for ems esp """

CONSTANTS_BOILER_POWER = {
    "boiler power sensor": {
        "value": "curBurnPow",
        "name": "current burner power",
        "icon": "mdi:square-inc-cash",
        "unit": "kW",
    }
}

CONSTANTS_SENSORS = {
    "return temp sensor": {
        "value": "retTemp",
        "name": "Return Temperature",
        "icon": "mdi:thermometer-chevron-up",
        "unit": "°C",
    },
    "flow temp sensor": {
        "value": "curFlowTemp",
        "name": "Current Flow Temperature",
        "icon": "mdi:thermometer-chevron-down",
        "unit": "°C",
    },
    "warm water flow sensor": {
        "value": "wWCurTmp",
        "name": "Current Warm Water Temperature",
        "icon": "mdi:thermometer-chevron-down",
        "unit": "°C",
    },
    "warm water sensor": {
        "value": "boilTemp",
        "name": "Current Boiler Temperature",
        "icon": "mdi:water-boiler",
        "unit": "°C",
    },
    "thermostat sensor": {
        "value": "thermostat_currtemp",
        "name": "Current Room Temperature",
        "icon": "mdi:home-thermometer",
        "unit": "°C",
    },
    "thermostat setting": {
        "value": "thermostat_seltemp",
        "name": "Current Set Temperature",
        "icon": "mdi:thermostat",
        "unit": "°C",
    },
    "warm water setting": {
        "value": "wWSelTemp",
        "name": "Current Warm Water Selected Temperature",
        "icon": "mdi:thermometer-high",
        "unit": "°C",
    },
    "burner power setting": {
        "value": "selBurnPow",
        "name": "Burner Max Power",
        "icon": "mdi:fire",
        "unit": "%",
    },
    "burner power sensor": {
        "value": "curBurnPow",
        "name": "Burner current modulation",
        "icon": "mdi:fire",
        "unit": "%",
    },
    "pump modulation sensor": {
        "value": "pumpMod",
        "name": "Pump Modulation",
        "icon": "mdi:rotate-left",
        "unit": "%",
    },
    "system pressure sensor": {
        "value": "sysPress",
        "name": "System Pressure",
        "icon": "mdi:water-percent",
        "unit": "bar",
    },
    "flow rate sensor": {
        "value": "wWCurFlow",
        "name": "Tapwater Flow Rate",
        "icon": "mdi:water-pump",
        "unit": "l/min",
    },
    "tap water mode": {
        "value": "tapwaterActive",
        "name": "Tap Water",
        "icon": "mdi:water-pump",
        "unit": None,
    },
    "warm water active mode": {
        "value": "wWActivated",
        "name": "Warm Water activated",
        "icon": "mdi:water-outline",
        "unit": None,
    },
    "3-way valve mode": {
        "value": "wWHeat",
        "name": "3-way valve",
        "icon": "mdi:valve",
        "unit": None,
    },
    "active heating mode": {
        "value": "heatingActive",
        "name": "Heating",
        "icon": "mdi:radiator",
        "unit": None,
    },
    "gas valve mode": {
        "value": "burnGas",
        "name": "gas valve",
        "icon": "mdi:gas-cylinder",
        "unit": None,
    },
    "boiler pump mode": {
        "value": "heatPmp",
        "name": "boiler pump",
        "icon": "mdi:rotate-left",
        "unit": None,
    },
    "boiler circulation pump mode": {
        "value": "wWCirc",
        "name": "boiler circulation pump",
        "icon": "mdi:rotate-left",
        "unit": None,
    },
    "fantilator mode": {
        "value": "fanWork",
        "name": "fantilator",
        "icon": "mdi:fan",
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
        "icon": "mdi:face-agent",
        "unit": None,
    },
}
