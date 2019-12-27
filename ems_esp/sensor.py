"""Support for ems-esp through MQTT."""
from homeassistant.components import mqtt
from homeassistant.core import callback
from homeassistant.helpers.entity import Entity
from homeassistant.util import slugify
import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA
import homeassistant.helpers.config_validation as cv

from homeassistant.const import (
    ATTR_ATTRIBUTION, CONF_NAME, CONF_PASSWORD, CONF_USERNAME)

import json

from .constants import CONSTANTS

DOMAIN = "ems_esp"
CONF_BASE = "base_topic"
DEFAULT_BASE = "home"
DEFAULT_NAME = "EMS"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    vol.Optional(CONF_BASE, default=DEFAULT_BASE): cv.string,
})


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up ems_esp sensors."""
    
    sensors = []
    for sensor in CONSTANTS:
        sensors.append(DSMRSensor(sensor, config))

    async_add_entities(sensors)


class DSMRSensor(Entity):
    """Representation of a ems-esp sensor that is updated via MQTT."""

    def __init__(self, sensor, config):
        """Initialize the sensor."""

        self._definition = CONSTANTS[sensor] #import data from constents
        self._base  = config[CONF_BASE]
        self._Name = config[CONF_NAME] + " "
        
        self._name = self._definition.get("name")
        #self._entity_id = self._definition.get("entity")
        self._unit_of_measurement = self._definition.get("unit")        
        self._icon = self._definition.get("icon")        
        
        self._topic = self._base + "/ems-esp/boiler_data"
        self._value = self._definition.get("value") 
        
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
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit_of_measurement of this sensor."""
        return self._unit_of_measurement

    @property
    def icon(self):
        """Return the icon of this sensor."""
        return self._icon
