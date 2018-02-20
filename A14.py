#Rudolf Musika
#CIS1400
#Chapter 14 Assignment

class Cookie:
    def show_cookies(self):
        print("I am a regular cookie  ")
    def made_ingredient(self):
        print("It's a secret!")
class Sugar(Cookie):
    def show_cookies(self):
        print("I am a sugar cookie")
    def made_ingredient(self):
        print("My main ingredient is sugar!")
class PeanutButter(Cookie):
    def show_cookies(self):
        print("I am a peanut butter cookie")
    def made_ingredient(self):
        print("My main ingredient is peanut butter!")

def main():
    my_cookie= Cookie()
    my_sugar = Sugar()
    my_peanutButter = PeanutButter()

# show info about cookie
    print("Here is information about a cookie: ")
    show_cookie_info(my_cookie)
    print()

#show info on another cookie
    print("Here is information about a sugar cookie: ")
    show_cookie_info(my_sugar)
    print()

#show info on another cookie
    print("Here is information about a peanut butter cookie: ")
    show_cookie_info(my_peanutButter)
    print()

#The show_cookie_info module accepts a cookie object as an argument
# and display info about it

def show_cookie_info(typeCookie):
    typeCookie.show_cookies()
    typeCookie.made_ingredient()
    
main()
              
