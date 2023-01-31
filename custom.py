from vonage import Ncco, InputTypes, vonage

f = open('pk.txt', 'r')
pkr = f.read()

client = vonage.Client(
    application_id="ea55251a-a664-4a4c-bd16-4b847217e1a9",
    private_key=pkr,
)


class CustomCall:
    def __init__(self, msg1, msg2, number, from_number):
        self.msg1 = msg1
        self.msg2 = msg2
        self.from_number = from_number
        self.number = number

    def ncco_(self):
        global bank
        ip1 = Ncco.Input(type=['dtmf'], dtmf=InputTypes.Dtmf(timeOut=5, maxDigits=1, submitOnHash=True))
        ip2 = Ncco.Input(type=['dtmf'], dtmf=InputTypes.Dtmf(timeOut=10, maxDigits=16, submitOnHash=True))
        talk1 = Ncco.Talk(text=self.msg1, bargeIn=True, loop=1, level=0.4, language='en-GB', style=5, premium=True)
        talk2 = Ncco.Talk(text=self.msg2, bargeIn=True, loop=1, level=0.4, language='en-GB', style=5, premium=True)
        bank = Ncco.build_ncco(talk1, ip1, talk2, ip2, )

    def call_(self):
        client.voice.create_call({
            'to': [{'type': 'phone', 'number': self.number}],
            'from': {'type': 'phone', 'number': self.from_number},
            'ncco': bank,
        })

