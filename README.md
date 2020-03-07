# clean mqtt to Home Assistant
Custom component for receiving MQTT values from xxx. I made this for clearing up the configuration.yaml files. 
 

# This project is in beta state

### my wishlist

- [ ] Add all received mqtt states.
  - [ ] icons 
  - [x] sensors


### How to use this

1. Create a `custom_components` folder located inside the Home Assistant `config` folder.
2. Copy the folder `xxx` into the `custom_components` folder. 
3. Add the yaml code below to your `configuration.yaml`

```yaml
sensor:
  - platform: xxx
    name: xx
```
4. reboot Home Assistant


## Notes: 
The thermostat sensors are not fully tested. 

