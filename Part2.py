import netmiko
from netmiko import ConnectHandler

# Define device parameters
device = {
    'device_type': 'cisco_ios',  
    'ip':   '192.168.122.2',
    'username': 'shawki',
    'password': 'telecomS144',  
    
}

# Create a connection instance
connection = ConnectHandler(**device)

# Define the commands you want to send
commands_to_send = ['show ip interface brief']  # replace with your commands

# Send commands and print output
for command in commands_to_send:
    output = connection.send_command(command)
    print(f'Output of {command}:')
    print(output)

# Disconnect from the device
connection.disconnect()

