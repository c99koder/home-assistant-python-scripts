# Home Assistant Python Scripts
Helper scripts for [Home Assistant](https://www.home-assistant.io/) automations

## color_cycle
Cycles to the next color in an array of values

Example:
```yaml
service: python_script.color_cycle
data:
  entity_id: light.living_room
  colors:
    - red
    - green
    - [0,0,255]
    - orange
    - purple
```

## set_light_if_on
Sets values on a light only if the light is already on

Example:
```yaml
service: python_script.color_cycle
data:
  entity_id:
    - light.living_room
    - light.kitchen
    - light.bedroom
  rgb_color: [255,255,255]
```