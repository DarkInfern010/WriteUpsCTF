import paramiko

# Static params
param = ["chall.heroctf.fr", 10024, "password123", "./getSSHKey"]

for i in range(1,251):
    
    # New Connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Manage connection (password for the first and SSHKey for other)    
    if i == 1:
        ssh.connect(param[0], param[1], "user"+str(i), param[2])
    else:
        ssh.connect(param[0], param[1], "user"+str(i), key_filename='./SSHKey')

    # manage commande (cat flag for the last and ./getSSHkey for other)
    if i == 250:
        stdin, stdout, stderr = ssh.exec_command("cat flag.txt")
        print(stdout.readlines())
    else:
        stdin, stdout, stderr = ssh.exec_command(param[3])
    
    # Create SSHKey file
    f = open("SSHKey", "w")
    for i in stdout.readlines():
        # Add line by line
        f.write(i.strip()+"\n")
    f.close()