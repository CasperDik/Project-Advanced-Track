from chapter11_section4.Cards import Card

x = Card(1,12)
y = Card(1,1)

print(x.compare(y))             #Ace lowest
print(x.cmp(y))                 #Ace highest
