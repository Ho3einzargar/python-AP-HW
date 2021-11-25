PriceBuy = int(input())
PriceCurrent = int(input())
Count = int(input())

PriceBuyValidator = True
PriceCurrentValidator = True
CountValidator = True

if PriceBuy < 1000 or PriceBuy > 100000 or PriceBuy % 10 != 0 :
    PriceBuyValidator = False

if PriceCurrent < 1000 or PriceCurrent > 100000 or PriceCurrent % 10 != 0 :
    PriceCurrentValidator = False

if Count < 50 or Count > 5000 :
    CountValidator = False


if not(PriceBuyValidator) or not(PriceCurrentValidator) or not(CountValidator):
    print('Invalid Input')

else :
    if PriceBuy > PriceCurrent:
        lossPercent = ((PriceBuy - PriceCurrent) * 100 / PriceBuy * -1).__round__(2)
        lossPrice = PriceCurrent * Count

        print('Loss')
        print("%.2f" % lossPercent)

        if lossPrice < 10000000 and  lossPercent > -20:
            print('Chance')
        elif lossPrice >= 10000000 or  lossPercent <= -20:
            print('under the coverage')


    else:
        profitPercent = (((PriceCurrent - PriceBuy) * 100) / PriceBuy).__round__(2)
        profitPrice = PriceCurrent * Count

        print('Profit')
        print('+', end='')
        print("%.2f" % profitPercent)

        if profitPrice > 5000000 and  profitPercent > 20:
            print('Lucky')
        elif profitPrice <= 5000000 or  profitPercent <= 20:
            print('Normal')
        

        


