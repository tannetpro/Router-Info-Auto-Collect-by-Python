#########SSH Device Show verssion collect  Script:#########

This Python script is designed to connect to network devices using SSH and retrieve 
their configuration using the 'show verssion' command. The script reads login 
credentials and device information from an Excel file, establishes SSH connections 
to the devices, and saves the configuration outputs in separate text files.


#######Requirements#########
Python 3.x
Pandas library (pip install pandas)
Paramiko library (pip install paramiko)

#########How to Use#########
Install the required dependencies using the provided requirements.txt file or manually using pip.

Prepare your Excel file ('TEST.xlsx') with the following columns: 'SN', 'Device', 'IP', 'username', and 'password'. Fill in the necessary login credentials and device information for each row.

Ensure that the Python script (show verssion collection.py) and the Excel file are in the same directory.

Run the script using the following command:

python ssh_backup_script.py

The script will read the Excel file, establish SSH connections to the devices, 
and retrieve their show verssion outputs. The output files will be saved in the 'C:/PyTest/Backup/' directory, 
with filenames in the format '{IP}_show verssion.txt'.



#########Important Notes#########

Make sure to keep the login credentials and device information in the Excel file secure, as hardcoding 
sensitive information in the script is not recommended.
The script uses the 'show running-config' command by default. 
You can modify the login_to_device function to execute other commands if needed.
Disclaimer
This script is provided as-is, without warranty or support. Use it at your own risk. 
The author is not responsible for any misuse, data loss, or damages caused by the script.


Connect me if require: youtube.com/tannetpro
