"""Support for ems-esp through MQTT."""
from homeassistant.components import mqtt
from homeassistant.core import callback
from homeassistant.helpers.entity import Entity
from homeassistant.util import slugify

import json

from .constants import CONSTANTS

DOMAIN = "ems_esp"


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up ems_esp sensors."""

    sensors = []
    for sensor in CONSTANTS:
        sensors.append(DSMRSensor(sensor))

    async_add_entities(sensors)


class DSMRSensor(Entity):
    """Representation of a ems-esp sensor that is updated via MQTT."""

    def __init__(self, sensor):
        """Initialize the sensor."""

        self._definition = CONSTANTS[sensor] #import data from constents
        
        self._name = self._definition.get("name")
        #self._entity_id = self._definition.get("entity")
        self._unit_of_measurement = self._definition.get("unit")        
        self._icon = self._definition.get("icon")        
        
        self._topic = "home/ems-esp/boiler_data"
        self._value = self._definition.get("value")
        
        self._state = None

    async def async_added_to_hass(self):
        """Subscribe to MQTT events."""

        @callback
        def message_received(message):
            """Handle new MQTT messages."""

            #self._state = message.payload
            
            self._state = json.loads(message.payload)[self._value]

            self.async_schedule_update_ha_state()

        await mqtt.async_subscribe(self.hass, self._topic, message_received, 1)

    @property
    def name(self):
        """Return the name of the sensor supplied in constructor."""
        return self._name

 #   @property
 #   def entity_id(self):
 #       """Return the entity ID for this sensor."""
 #       #return f"sensor.{self._entity_id}"
 #       return self._entity_id

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
