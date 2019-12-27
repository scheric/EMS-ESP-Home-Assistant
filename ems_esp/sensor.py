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

DOMAIN = "ems_esp"

from .constants import CONSTANTS_SENSORS, CONSTANTS_BOILER_POWER

CONF_BASE = "base_topic"
CONF_POWER = "boiler_power"

DEFAULT_BASE = "home"
DEFAULT_NAME = "EMS_ESP"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    vol.Optional(CONF_BASE, default=DEFAULT_BASE): cv.string,
    vol.Optional(CONF_POWER, default=0): vol.Coerce(float),
})


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up ems_esp sensors."""
    
    sensors = []
    for sensor in CONSTANTS_SENSORS:
        sensors.append(EMS_ESPSensor(sensor, config, CONSTANTS_SENSORS[sensor].get("name"), CONSTANTS_SENSORS[sensor].get("unit") , CONSTANTS_SENSORS[sensor].get("icon"), CONSTANTS_SENSORS[sensor].get("value")))
        
    for sensor in CONSTANTS_BOILER_POWER:
        if config[CONF_POWER]:
            sensors.append(EMS_ESPSensor(sensor, config, CONSTANTS_BOILER_POWER[sensor].get("name"), CONSTANTS_BOILER_POWER[sensor].get("unit") , CONSTANTS_BOILER_POWER[sensor].get("icon"), CONSTANTS_BOILER_POWER[sensor].get("value")))

    async_add_entities(sensors)


class EMS_ESPSensor(Entity):
    """Representation of a ems-esp sensor that is updated via MQTT."""

    def __init__(self, sensor, config, Name, Unit, Icon, Value):
        """Initialize the sensor."""

        self._base  = config[CONF_BASE]
        self._Name = config[CONF_NAME] + " "
        self._boiler_power = config[CONF_POWER]
        
        self._topic = self._base + "/ems-esp/boiler_data"
        
        self._name = Name
        self._unit_of_measurement = Unit      
        self._icon = Icon      
        self._value = Value
         
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
