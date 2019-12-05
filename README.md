# androsploit.py
Este script, permite generar payloads a partir de Metasploit Framework de manera muy sencilla. Además, configura e inicia msfconsole automáticamente, también, corrige el error de conexión a la database de Metasploit.


Requiere python 3.
En caso de no tener python instalado, puede ejecutar:

Kali Linux:

apt-get install python -y

apt-get install python2 -y


Termux : 

pkg install python -y

pkg install python2 -y


Requiere Metasploit Framework
En caso de no tener Metasploit Framework instalado en el sistema, Androsploit puede instalarlo por usted. (Característica solo disponible para Termux)

El script Androsploit funciona en Kali Linux y Termux.

Descarga y uso :

git clone https://github.com/Syst3mFailure/androsploit

cd androsploit

python3 androsploit.py
