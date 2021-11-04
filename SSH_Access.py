from netmiko import ConnectHandler
sandbox = {
             'device_type': 'cisco_xe',
             'host': 'sandbox-iosxe-latest-1.cisco.com',
             'username':'developer',
             'password': 'C1sco12345',
  #Username e Password são os do Cisco Sandbox always-on lab
  #Arquivo 'Config-file' é um TXT que definimos os comandos que iremos dar após conectar o device
}
with open('Config-file') as file:
   config_lines = file.read().splitlines()
connect = ConnectHandler(**sandbox)
configure = connect.send_config_set(config_lines)
print(configure)
connect.disconnect()



