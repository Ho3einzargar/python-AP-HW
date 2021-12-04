from datetime import datetime
from math import sin, cos, sqrt, atan2, radians
import csv

class MedadRangi():
    def __init__(self, name, price, count, builtCountry, factoryName):
        self.coordinate = (35.74317403843504, 51.50185488303431)
        self.discount = 10

        self.name = name
        self.price = price
        self.count = count
        self.builtCountry = builtCountry
        self.factoryName = factoryName


    def final_price(self):
        totalPrice = self.count * self.price
        finalPrice = totalPrice * (100 - self.discount)/100
        singlePriceWithDiscount = finalPrice/self.count
        print('signle price is '+ str(self.price) + '\n' + 'signle price with discount '+ str(singlePriceWithDiscount))

    def welcome(self):
        now = datetime.now()
        current_hour = int(now.strftime("%H"))

        if  current_hour>=6 and current_hour<12:
            print('good morning')
        elif  current_hour>=12 and current_hour<18:
            print('good evenning')
        else:
            print('good night')


    def calculate_distance(self, coordinate):
        

        # approximate radius of earth in km
        R = 6373.0

        lat1 = radians(self.coordinate[0])
        lon1 = radians(self.coordinate[1])
        lat2 = radians(coordinate[0])
        lon2 = radians(coordinate[1])

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c

        print("distanse is: ", distance, 'km')

    def load_csv(self):
        with open('seri-4/eggs.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar=',')
            print(spamreader)
            for row in spamreader:
                print(row)


x = MedadRangi('pencil', 4500, 5, 'iran', 'kale')

x.load_csv()