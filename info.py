import requests
class Converter():
    def __init__(self,link):
            self.data= requests.get(link).json()
            self.currencies =self.data['rates']


    def convert(self, From_, To, amount):
            if From_ != 'USD':
                amount = amount / self.currencies[From_]
                amount = round(amount * self.currencies[To], 4)
                return str(str(amount)+'  $ USD')







