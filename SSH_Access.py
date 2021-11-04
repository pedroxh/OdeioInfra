from netmiko import ConnectHandler
sandbox = {
             'device_type': 'cisco_xe',
             'host': '10.10.20.48',
             'username':'developer',
             'password': 'C1sco12345',
}
with open('Config-file') as file:
   config_lines = file.read().splitlines()
connect = ConnectHandler(**sandbox)
configure = connect.send_config_set(config_lines)
print(configure)
connect.disconnect()



