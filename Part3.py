import netmiko
from netmiko import ConnectHandler

# Define device parameters
device = {
    'device_type': 'cisco_ios',  
    'ip':   '192.168.122.2',
    'username': 'shawki',
    'password': 'telecomS144',  
    'secret'  : 'telecomS144'

}

# Create a connection instance
connection = ConnectHandler(**device)

# Enter enable mode
connection.enable()


# Define the commands you want to send
commands_to_send = ['show ip interface brief'] 

# Send commands and print output
for command in commands_to_send:
    output = connection.send_command(command)
    print(f'Output of {command}:')
    print(output)

# Define configuration commands
config_commands = [
    'interface loopback 0',
    'ip address 11.11.11.11 255.255.255.255',
    'no shut',
    'exit',
    'do write memory'
]  

# Send configuration commands and print output
output = connection.send_config_set(config_commands)
print('Output of configuration commands:')
print(output)

# Define verification command
verification_command = 'show ip interface brief' 

# Send verification command and print output
output = connection.send_command(verification_command)
print(f'Output of {verification_command}:')
print(output)

# Disconnect from the device
connection.disconnect()