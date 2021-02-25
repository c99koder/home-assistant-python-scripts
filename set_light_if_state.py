# set data only if light is in a specific state
entity_id = data.get("entity_id")
if isinstance(entity_id, str) and "," in entity_id:
	entity_id = entity_id.split(",")

light_data = {}
for k, v in data.items():
	if k not in('old_state', 'new_state'):
		light_data[k] = v

entities = []
if isinstance(entity_id, str):
	if entity_id is not None and hass.states.is_state(entity_id, data['old_state']):
		entities.append(entity_id)
else:
	for entity in entity_id:
		if entity is not None and hass.states.is_state(entity.strip(), data['old_state']):
			entities.append(entity.strip())

if len(entities) > 0:
	light_data['entity_id'] = ','.join(entities)
	hass.services.call('light', 'turn_' + data['new_state'], light_data, False)
