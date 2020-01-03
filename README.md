# EMS ESP Home Assistant
Custom component for receiving mqtt values from ems-esp. I made this for clearing up the configuration.yaml files. 
 

# This project is in beta state

### my wishlist

- [ ] Add all received mqtt states.
  - [x] icons 
  - [x] sensors
  - [ ] switches
  - [ ] scripts
  - [ ] climate
  - [ ] binary sensors
  - [x] optional kW calculation
  
- [x] Add boiler/thermostat/solar/ect. topic toggler in .yaml
- [ ] thermostat
- [x] boiler
- [ ] sensor
- [ ] shower
- [ ] solar
- [ ] heatpump
- [ ] heartbeat
- [ ] mixer
- [x] boiler power calculator
- [ ] Add sending topics
- [x] Add configurable topic
- [ ] Create configurable data sets.
- [x] Add configurable name.
- [ ] Add to Home Assistant.


### How to use this

1. Create an `custom_components` folder located inside the Home Assistant `config` folder.
2. Copy the folder `ems-esp` into the `custom_components` folder. 
3. Add the yaml code below to your `configuration.yaml`
```yaml
sensor:
  - platform: ems_esp
    name: EMS
    base_topic: home
    thermostat: false
    boiler: false
    sensor: 2
    shower: false
    solar: false
    heatpump: false
    heartbeat: false
    mixer: false
    boiler_power: 30
```
4. reboot Home Assistant


## Notes: 
The thermostat sensors are not fully tested. 

