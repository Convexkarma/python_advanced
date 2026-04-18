import random 

cards = ["jack","Queen","King"]
random.shuffle(cards)

while True: 
    try:    
         for card in cards :
            print (card)
    except KeyboardInterrupt:
         continue


'''
for i in range (len(cards)):       This an alternative way 
    print (cards[i])
'''
