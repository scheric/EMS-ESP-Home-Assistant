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

DOMAIN = "xxxx"

from .constants import [CONSTANTS IMPORT]

CONF_BASE = "base_topic"


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default="EMS_ESP"): cv.string,
    vol.Optional(CONF_THERMOSTAT, default=False): cv.boolean,
    vol.Optional(CONF_SENSORS, default=0): cv.positive_int,
    vol.Optional(CONF_POWER, default=0): vol.Coerce(float),
})

_LOGGER = logging.getLogger(__name__)
        #_LOGGER.error(f"sensor: {sensor}")

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up XXX sensors."""
    
    sensors = []
     
    #add thermostat sensors DONE
    if config[CONF_THERMOSTAT]:
        for sensor in CONSTANTS_SENSORS_THERMOSTAT:
            sensors.append(EMS_ESPSensor(config, CONSTANTS_SENSORS_THERMOSTAT[sensor].get("name"), CONSTANTS_SENSORS_THERMOSTAT[sensor].get("unit") , CONSTANTS_SENSORS_THERMOSTAT[sensor].get("icon"), CONSTANTS_SENSORS_THERMOSTAT[sensor].get("value"), CONSTANTS_SENSORS_THERMOSTAT[sensor].get("topic")))

    
    async_add_entities(sensors)


class EMS_ESPSensor(Entity):
    """Representation of a XXX sensor that is updated via MQTT."""

    def __init__(self, config, Name, Unit, Icon, Value, Topic):
        """Initialize the sensor."""

        self._base  = config[CONF_BASE]
        self._Name = config[CONF_NAME] + " "
        
        #self._topic = self._base + "/ems-esp/boiler_data"
        
        self._name = Name
        self._unit_of_measurement = Unit      
        self._icon = Icon      
        self._value = Value
        self._topic = self._base + Topic 
         
        self._in = None
        self._out = None

    async def async_added_to_hass(self):
        """Subscribe to MQTT events."""

        @callback
        def message_received(message):
            """Handle new MQTT messages."""
            self._in = json.loads(message.payload)[self._value]

            self.async_schedule_update_ha_state()

        await mqtt.async_subscribe(self.hass, self._topic, message_received, 1)

    @property
    def name(self):
        """Return the name of the sensor supplied in constructor."""
        return self._Name + self._name

    @property
    def state(self):
        """Return the current state of the entity."""
        
        self._out = self._in
        
        #calculation example
        if self._name == "current burner power":
            try:
                self._out = round(((self._boiler_power/100) * self._in),1)
            except TypeError:
                pass
        
        
        return self._out

    @property
    def unit_of_measurement(self):
        """Return the unit_of_measurement of this sensor."""
        return self._unit_of_measurement

    @property
    def icon(self):
        """Return the icon of this sensor."""
        return self._icon
