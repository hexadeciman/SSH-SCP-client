from paramiko import SSHClient
from scp import SCPClient


def connectSSH(user, host, passwd):
	ssh = SSHClient()
	ssh.load_system_host_keys()
	ssh.connect(host, username=user, password=passwd)
	return ssh

def execCommand(connexion, command):
	stdin, stdout, stderr = connexion.exec_command(command)
	data = stdout.read()
	print data

user = 'INSERT YOUR USERNAME HERE'
password = 'INSERT YOUR PASS HERE'
host = 'INSERT THE HOST ADDRESS/ DOMAIN NAME'

ssh = connectSSH(user,host,password)

command = "ls"
execCommand(ssh,command)
