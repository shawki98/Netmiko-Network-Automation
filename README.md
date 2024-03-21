# Netmiko-Network-Automation
Five part implimentation for network configuration using Netmiko, written in python

Part 1: Setting Up the Environment
The first step was to set up the environment. This involved installing Netmiko, a Python library that simplifies the process of connecting to network devices via SSH. The installation was done using pip, the Python package installer.
Next, access to a network device was ensured. For this project, a Cisco router was connected to a cloud network via a virtual bridge interface (virbr0) using GNS3, a network simulator. The router’s FastEthernet0/0 interface was assigned an IP address of 192.168.122.2/24, and it was connected to the cloud network, which had an IP address of 192.168.122.1/24.

Part 2: Connecting to a Device
The next step was to create a Python script to connect to the network device using Netmiko. The script used the ConnectHandler function from Netmiko to establish an SSH connection to the device. The device parameters (device type, IP address, username, password, and secret) were defined in the script. The username was set to ‘shawki’.
Once the connection was established, the script was used to retrieve device information. It executed the command ‘show ip interface brief’ on the device, and the output was displayed. This command provides a summary of the interfaces on the device, including their IP addresses and status.

Part 3: Configuring the Network Device
The script was then extended to send configuration commands to the device. These commands were used to configure a loopback interface with an IP address and to save the configuration. The loopback interface is a virtual interface used for testing and management purposes.
After sending the configuration commands, the script verified the configuration changes by executing appropriate show commands. The output of these commands provided information about the current configuration of the device, allowing for verification of the changes.

Part 4: Automating Tasks
A routine task was identified for automation. This task was to backup the configuration of the device. The script was written to automate this task by sending the command ‘show running-config’ to the device and logging the output. This command displays the current configuration of the device.
Logging was implemented in the script using the logging module in Python. The operations were logged to a file named ‘netmiko.log’. This log file serves as a record of the operations performed by the script.

Part 5: Error Handling and Reporting
Error handling was added to the script to manage exceptions. The script was designed to catch and handle specific exceptions related to connection timeouts and authentication errors. If any of these exceptions were raised, an error message was logged.
Finally, a report was generated that includes the commands executed, the changes made, and any errors encountered. This report is essentially the ‘netmiko.log’ log file. The log file contains a record of all the operations performed by the script, including the output of each command and any errors encountered.
