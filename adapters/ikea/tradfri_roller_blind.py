import json
from adapters.base_adapter import Adapter
from devices.switch.blind_percentages_switch import BlindSwitch

class TradfriRollerBlind(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.blindswitch = BlindSwitch(devices, 'dimmer', 'position')
        self.blindswitch.add_level('Stop', 'stop')
        self.devices.append(self.blindswitch)

    def handleCommand(self, alias, device, device_data, command, level, color):
        if (command.upper() == "SET LEVEL"):
            return {
            'topic': device_data['friendly_name'] + '/set',
            'payload': json.dumps({
                "position": int(100-level)
            })
            }
        elif (command.upper() == "ON"):
            return {
            'topic': device_data['friendly_name'] + '/set',
            'payload': json.dumps({
                "state": "close"
            })
            }
        elif (command.upper() == "OFF"):
            return {
            'topic': device_data['friendly_name'] + '/set',
            'payload': json.dumps({
                "state": "open"
            })
            }
        else:
            command="stop"
            return {
            'topic': device_data['friendly_name'] + '/set',
            'payload': json.dumps({
                "state": "stop"
            })
            }
