# By Hitengupta-coding
import binascii
print('This is a text to hex and hex to text convertor.')
def tryagain():
    qt = input('Do you want to use more(y/n): ')

    if qt=="y":
        convert()

    elif qt=="n":
        print('Thanks for using our software, Goodbye')

    else:
        print('You entered invalid statement, try again')
        tryagain()

def convert():
    def thmode():
        text = input('Enter the text to be converted: ')
        hex_output = binascii.hexlify(text.encode()).decode()
        print(hex_output)

    def htmode():
        try:
            hex_string = input('Enter the hex to be converted: ')
            text = binascii.unhexlify(hex_string).decode()
            print(text)
        except:
            print('your hex is wrong!')
            htmode()


    def ask():
        mode = input("Enter 'TH' to convert text to hex OR Enter 'HT' to convert hex to text: ").lower()
        if mode == "th":
            thmode()

        elif mode == "ht":
            htmode()

        else:
            print('wrong statement, try again.')
            ask()

    ask()
    tryagain()

convert()
