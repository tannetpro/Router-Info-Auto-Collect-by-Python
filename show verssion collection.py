import pandas as pd
import paramiko

# Read the Excel file
df = pd.read_excel('C:/PyTest/Backup/TEST.xlsx')

# Define the desired column names and row indices
selected_columns = ['SN', 'Device', 'IP', 'username', 'password']
selected_rows = [0, 1, 2, 3, 4, 5, 6, 7]

# Select the desired columns and rows from the DataFrame
selected_data = df[selected_columns].iloc[selected_rows]

# Convert the selected data to a list
values = selected_data.values.tolist()

# Create the login credentials dictionary from the extracted data
login_credentials = {}
for row in values:
    ip = row[2]  # Assuming IP is at index 2
    username = row[3]  # Assuming username is at index 3
    password = row[4]  # Assuming password is at index 4

    login_credentials[ip] = {
        'username': username,
        'password': password
    }

# Function to login to the device using SSH
def login_to_device(ip, username, password):
    try:
        # Create SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the device
        ssh_client.connect(ip, username=username, password=password)

        # Execute the 'show version' command
        stdin, stdout, stderr = ssh_client.exec_command('show version')

        # Read the command output
        output = stdout.read().decode()

        # Save the output to a file with the IP name
        filename = f"C:/PyTest/Backup/{ip}_show_version.txt"
        with open(filename, 'w') as file:
            file.write(output)

        # Close the SSH connection
        ssh_client.close()

        print(f"Logged in successfully to {ip}. 'show version' output saved to {filename}")
    except paramiko.AuthenticationException:
        print(f"Authentication failed for {ip}")
    except paramiko.SSHException as e:
        print(f"SSH error occurred for {ip}: {str(e)}")
    except Exception as e:
        print(f"Error occurred for {ip}: {str(e)}")

# Loop through the selected data and login to each device
for row in values:
    ip = row[2]  # Assuming IP is at index 2
    username = row[3]  # Assuming username is at index 3
    password = row[4]  # Assuming password is at index 4

    if ip in login_credentials:
        stored_username = login_credentials[ip]['username']
        stored_password = login_credentials[ip]['password']

        if username == stored_username and password == stored_password:
            login_to_device(ip, username, password)
        else:
            print(f"Invalid credentials for {ip}")
    else:
        print(f"No login credentials found for {ip}")
