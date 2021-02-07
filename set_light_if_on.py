# set data only if light is already on
def set_entity(entity_id, light_data):
	if entity_id is not None and hass.states.is_state(entity_id, 'on'):
		light_data['entity_id'] = entity_id
		hass.services.call("light", "turn_on", light_data, False)

entity_id = data.get("entity_id")
light_data = {}
for k, v in data.items():
	light_data[k] = v

if isinstance(entity_id, str):
	set_entity(entity_id, light_data)
else:
	for entity in entity_id:
		set_entity(entity, light_data)
