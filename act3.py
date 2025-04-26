class india():
    def capital(self):
        print("Capital of india is Delhi")
    def language(self):
        print("Language of india is English")
    def type(self):
        print("India is developing country")
class USA():
    def capital(self):
        print("Capital of USA is Washington")
    def language(self):
        print("Language of USA is English")
    def type(self):
        print("USA is developed country")
a=india()
b=USA()
for country in (a,b):
    country.capital()
    country.language()
    country.type()
