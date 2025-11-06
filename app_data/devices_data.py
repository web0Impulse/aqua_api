devices_data = {
    0 : {
      'name': 'Air pump',
      'type': 'switch',
      'status': 1,
    },
    1 : {
      'name': 'Light',
      'type': 'switch',
      'status': 0,
    },
    2 : {
      'name': 'Temperature sensor',
      'type': 'sensor',
      'status': 22,
    },    
}

def serialize_all():
  return [devices_data[key] for key in devices_data]

def get_device_data(id: int):
    return devices_data.get(id)

def set_device_data(id: int, value: int):
    if id in devices_data:
        devices_data[id]['status'] = value