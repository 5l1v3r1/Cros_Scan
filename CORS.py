#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Info: https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
# @s1kr10s

import commands
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

BLUE = '\033[94m'
RED = '\033[1;31m'
BOLD = '\033[1m'
GREEN = '\033[32m'
ENDC = '\033[0m'
Pwd = commands.getoutput("pwd")
test = "http://pwnd.com"

print BOLD+BLUE+"\n Cross-Origin Resource Sharing"+ENDC
opt = input("\n 1) Read file\n 2) Only host\n # ")

def connect(host):
	CORS = commands.getoutput("curl "+str(host)+" -H 'Origin: "+str(test)+"' -I ")

	if CORS.find("Access-Control-Allow-Origin: "+str(test)) != -1 or CORS.find("Access-Control-Allow-Credentials: true") != -1:
		print GREEN+" ☠ ☠ ☠ ☠  Vuln :) "+str(host)+" ☠ ☠ ☠ ☠"+ENDC
	else:
		print RED+" No Vuln :/ "+str(host)+ENDC

if opt == 1:
	urix = []
	files = file("listauri.txt","r")
	print BLUE+"\n Ejecutando...\n"+ENDC
	for uri in files:
		uri = uri.rstrip()
		urix.append(uri)

	for host in urix:
		connect(host)
else:
	host = raw_input("\n Input host [http://domain.com]: ")
	print BLUE+"\n Ejecutando...\n"+ENDC
	connect(host)

print BLUE+"\n Finalizado...\n"+ENDC

