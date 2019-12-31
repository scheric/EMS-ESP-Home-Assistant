"""Support for ems-esp through MQTT."""
from homeassistant.components import mqtt
from homeassistant.core import callback
from homeassistant.helpers.entity import Entity
from homeassistant.util import slugify
import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA
import homeassistant.helpers.config_validation as cv
import logging

from homeassistant.const import (
    ATTR_ATTRIBUTION, CONF_NAME, CONF_PASSWORD, CONF_USERNAME)

import json

DOMAIN = "ems_esp"

from .constants import CONSTANTS_SENSORS_BOILER, CONSTANTS_BOILER_POWER, CONSTANTS_SENSORS_SENSORS, CONSTANTS_SENSORS_THERMOSTAT

CONF_BASE = "base_topic"
CONF_THERMOSTAT = "thermostat"
CONF_BOILER = "boiler"
CONF_SENSORS = "sensor"
CONF_SHOWER_DATA = "shower"
CONF_SOLAR_DATA = "solar"
CONF_HEATPUMP_DATA = "heatpump"
CONF_HEARTBEAT = "heartbeat"
CONF_MIXING_DATA = "mixer"

CONF_POWER = "boiler_power"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default="EMS_ESP"): cv.string,
    vol.Optional(CONF_BASE, default="home"): cv.string,
    vol.Optional(CONF_THERMOSTAT, default=True): cv.boolean,
    vol.Optional(CONF_BOILER, default=True): cv.boolean,
    vol.Optional(CONF_SENSORS, default=0): cv.positive_int,
    vol.Optional(CONF_SHOWER_DATA, default=False): cv.boolean,
    vol.Optional(CONF_SOLAR_DATA, default=False): cv.boolean,
    vol.Optional(CONF_HEATPUMP_DATA, default=False): cv.boolean,
    vol.Optional(CONF_HEARTBEAT, default=False): cv.boolean,
    vol.Optional(CONF_MIXING_DATA, default=False): cv.boolean,
    
    vol.Optional(CONF_POWER, default=0): vol.Coerce(float),
})

_LOGGER = logging.getLogger(__name__)
        #_LOGGER.error(f"sensor: {sensor}")

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up ems_esp sensors."""
    
    sensors = []
     
    #add thermostat sensors DONE
    if config[CONF_THERMOSTAT]:
        for sensor in CONSTANTS_SENSORS_THERMOSTAT:
            sensors.append(EMS_ESPSensor(config, CONSTANTS_SENSORS_THERMOSTAT[sensor].get("name"), CONSTANTS_SENSORS_THERMOSTAT[sensor].get("unit") , CONSTANTS_SENSORS_THERMOSTAT[sensor].get("icon"), CONSTANTS_SENSORS_THERMOSTAT[sensor].get("value"), CONSTANTS_SENSORS_THERMOSTAT[sensor].get("topic")))

    #add boiler sensors DONE
    if config[CONF_BOILER]:
        for sensor in CONSTANTS_SENSORS_BOILER:
            sensors.append(EMS_ESPSensor(config, CONSTANTS_SENSORS_BOILER[sensor].get("name"), CONSTANTS_SENSORS_BOILER[sensor].get("unit") , CONSTANTS_SENSORS_BOILER[sensor].get("icon"), CONSTANTS_SENSORS_BOILER[sensor].get("value"), CONSTANTS_SENSORS_BOILER[sensor].get("topic")))

    # add sensor sensors DONE
    if config[CONF_SENSORS]:
        for ammount in range(1, (config[CONF_SENSORS]+1)):
            for sensor in CONSTANTS_SENSORS_SENSORS:
                sensors.append(EMS_ESPSensor(config, CONSTANTS_SENSORS_SENSORS[sensor].get("name") + " " + str(ammount), CONSTANTS_SENSORS_SENSORS[sensor].get("unit") , CONSTANTS_SENSORS_SENSORS[sensor].get("icon"), CONSTANTS_SENSORS_SENSORS[sensor].get("value") + str(ammount), CONSTANTS_SENSORS_SENSORS[sensor].get("topic")))

    #add shower sensors
    if config[CONF_SHOWER_DATA]:
        for sensor in CONSTANTS_BOILER_POWER:
            #sensors.append(EMS_ESPSensor(config, CONSTANTS_BOILER_POWER[sensor].get("name"), CONSTANTS_BOILER_POWER[sensor].get("unit") , CONSTANTS_BOILER_POWER[sensor].get("icon"), CONSTANTS_BOILER_POWER[sensor].get("value"), CONSTANTS_BOILER_POWER[sensor].get("topic")))

    #add solar sensors
    if config[CONF_SOLAR_DATA]:
        for sensor in CONSTANTS_BOILER_POWER:
            #sensors.append(EMS_ESPSensor(config, CONSTANTS_BOILER_POWER[sensor].get("name"), CONSTANTS_BOILER_POWER[sensor].get("unit") , CONSTANTS_BOILER_POWER[sensor].get("icon"), CONSTANTS_BOILER_POWER[sensor].get("value"), CONSTANTS_BOILER_POWER[sensor].get("topic")))

    #add heatpump sensors
    if config[CONF_HEATPUMP_DATA]:
        for sensor in CONSTANTS_BOILER_POWER:
            #sensors.append(EMS_ESPSensor(config, CONSTANTS_BOILER_POWER[sensor].get("name"), CONSTANTS_BOILER_POWER[sensor].get("unit") , CONSTANTS_BOILER_POWER[sensor].get("icon"), CONSTANTS_BOILER_POWER[sensor].get("value"), CONSTANTS_BOILER_POWER[sensor].get("topic")))

    #add heartbeat sensors
    if config[CONF_HEARTBEAT]:
        for sensor in CONSTANTS_BOILER_POWER:
            #sensors.append(EMS_ESPSensor(config, CONSTANTS_BOILER_POWER[sensor].get("name"), CONSTANTS_BOILER_POWER[sensor].get("unit") , CONSTANTS_BOILER_POWER[sensor].get("icon"), CONSTANTS_BOILER_POWER[sensor].get("value"), CONSTANTS_BOILER_POWER[sensor].get("topic")))

    #add mixer sensors
    if config[CONF_MIXING_DATA]:
        for sensor in CONSTANTS_BOILER_POWER:
            #sensors.append(EMS_ESPSensor(config, CONSTANTS_BOILER_POWER[sensor].get("name"), CONSTANTS_BOILER_POWER[sensor].get("unit") , CONSTANTS_BOILER_POWER[sensor].get("icon"), CONSTANTS_BOILER_POWER[sensor].get("value"), CONSTANTS_BOILER_POWER[sensor].get("topic")))

    
    async_add_entities(sensors)


class EMS_ESPSensor(Entity):
    """Representation of a ems-esp sensor that is updated via MQTT."""

    def __init__(self, config, Name, Unit, Icon, Value, Topic):
        """Initialize the sensor."""

        self._base  = config[CONF_BASE]
        self._Name = config[CONF_NAME] + " "
        self._boiler_power = config[CONF_POWER]
        
        #self._topic = self._base + "/ems-esp/boiler_data"
        
        self._name = Name
        self._unit_of_measurement = Unit      
        self._icon = Icon      
        self._value = Value
        self._topic = self._base + Topic 
         
        self._state = None

    async def async_added_to_hass(self):
        """Subscribe to MQTT events."""

        @callback
        def message_received(message):
            """Handle new MQTT messages."""
            self._state = json.loads(message.payload)[self._value]

            self.async_schedule_update_ha_state()

        await mqtt.async_subscribe(self.hass, self._topic, message_received, 1)

    @property
    def name(self):
        """Return the name of the sensor supplied in constructor."""
        return self._Name + self._name

    @property
    def state(self):
        """Return the current state of the entity."""
        
        if self._name == "current boiler power":
            try:
                self._state = round(((self._boiler_power/100) * self._state),1)
            except TypeError:
                pass
        
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit_of_measurement of this sensor."""
        return self._unit_of_measurement

    @property
    def icon(self):
        """Return the icon of this sensor."""
        return self._icon
