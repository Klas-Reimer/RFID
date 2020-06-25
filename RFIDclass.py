class RFID:
    RFIDcode = " "
    name = " "
    link = " "
    number = 0

    def __init__(self, RFIDcode, name,  link, number):
        self.RFIDcode = RFIDcode
        self.name = name
        self.link = link
        self.number = number

    def sayhello(self):
        print("hello - I am " + self.name)

    def giveRFID(self):
        print(self.RFIDcode)

# Create objects
ABCAA = RFID("ABCAA","Schorsch","www.google.de",3)
ABAAA = RFID("ABAAA","Peppa","www.youtube.de",2)

# Funtion aufrufen
ABAAA.sayhello()
ABAAA.giveRFID()

