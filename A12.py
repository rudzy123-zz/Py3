#Rudolf Musika
#CIS1400
#Chapter 12 Assignment
def main():

#phone Number is entered
    phoneNumber = (input("Enter  a 10 digit unformatted telephone number in the format ##########: "))
    if len(phoneNumber) ==10:
        print("The unformatted number is: ",phoneNumber)
        formaT(phoneNumber)
    else:
        print("That telephone number was NOT entered in unformated format ##########. ")

# The function below will configure the phone configuration into (XXX)XXX-XXXX
def formaT(Str):
# insert the left paren at position 0.
    Str = Str[:0]+"("+ Str[0:]
# Next, insert the right paren at position 4.
    Str = Str[:4] + ")" + Str[4:]
#Next, insert the hyphen at position 8.
    Str = Str[:8] + "-" + Str[8:]
    print("The formatted number is: ",Str)       
main()
