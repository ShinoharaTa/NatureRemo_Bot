import requests
import discord
import configparser
import time
import threading

class NatureRemo:

    headers = {}

    def __init__(self, conf):
        self.headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer ' + conf['NatureRemoAccessToken']
        }

    def getStatus(self):
        request = requests.get('https://api.nature.global/1/devices', headers=self.headers)
        return request.json()

    def run(self):
        remo = NatureRemo(settings)
        while True:
            remoStatus = remo.getStatus()
            lastGetTime = remoStatus[0]['newest_events']['te']['created_at']
            temp = remoStatus[0]['newest_events']['te']['val']
            print(lastGetTime +" "+str(temp))
            time.sleep(20)

def remo_thread():
    remo.run()

conf_name = 'config.ini'
config = configparser.ConfigParser()
config.read(conf_name)
settings = config['Setting']

if __name__ == "__main__":
    remo = NatureRemo(settings)
    # remoStatus = remo.getStatus()
    # lastGetTime = remoStatus[0]['newest_events']['te']['created_at']
    # # lastGetTime = remoStatus[0]['created_at']
    # temp = remoStatus[0]['newest_events']['te']['val']
    # print(lastGetTime +" "+str(temp))
    # # time.sleep(20)

    # tw = twitter(settings)
    # manga = manga_wallet()
    # manga.load_config(settings)
    # manga.load_plugin()
    # rep = twitter_reply(settings, tw, manga)
    # dm = twitter_dm(settings, tw, manga)

    thread_1 = threading.Thread(target=remo_thread)
    # thread_2 = threading.Thread(target=job)
    # thread_3 = threading.Thread(target=thread_dm)

    thread_1.start()
    # thread_2.start()
    # thread_3.start()