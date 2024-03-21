import netmiko
from netmiko import ConnectHandler
import logging

# Set up logging
logging.basicConfig(filename='netmiko.log', level=logging.INFO)
logger = logging.getLogger("netmiko")

# Define device parameters
device = {
    'device_type': 'cisco_ios', 
    'ip':   '192.168.122.2',
    'username': 'shawki',
    'password': 'telecomS144',  
    'secret' :  'telecomS144'
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
    logger.info(f'Output of {command}:\n{output}')

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
logger.info(f'Output of configuration commands:\n{output}')

# Define verification command
verification_command = 'show run brief' 

# Send verification command and print output
output = connection.send_command(verification_command)
print(f'Output of {verification_command}:')
print(output)
logger.info(f'Output of {verification_command}:\n{output}')

# Define the command to backup the configuration
backup_command = 'show running-config'

# Send the command and get the output
output = connection.send_command(backup_command)

# Log the output
logger.info(f'Routine Backup of configuration:\n{output}')

# Disconnect from the device
connection.disconnect()
