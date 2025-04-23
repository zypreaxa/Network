import tftpy

# Set the TFTP server directory to the one you just created
tftp_folder = "C:\\TFTP-Server"  # Make sure to use double backslashes \\

# Start the TFTP server
server = tftpy.TftpServer(tftp_folder)
print(f"Starting TFTP Server at 0.0.0.0:69 serving from {tftp_folder}")
server.listen("0.0.0.0", 69)