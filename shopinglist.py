"""shopinglist=[]
def add(shopinglist,item,price):
    shopinglist.append(item,price)
add(shopinglist,"Detol",123)
print(shopinglist)
"""
##user input
"""shopinglist=[]
def add(shopinglist,item,price):
    shopinglist.append((item,price))

item=input("Enter name of item:")
price=int(input("Enter price:"))
add(shopinglist,item,price)
print(shopinglist)"""

##Multiple input item
shoppinglist=[]
def add(shopinglist,item,price):
        shopinglist.append((item,price))

while(True):
    n=int(input("Enter choise:"))
    if(n==1):
        for i in range(0,2):
            item=input("Enter name of item:")
            price=int(input("Enter price:"))
            add(shoppinglist,item,price)
        print("shopinglist:",shoppinglist)
    elif(n==2):
        for item, price in shoppinglist:
            print(f"{item}: ${price}")
    elif(n==3):
        total_price = sum(price for _, price in shoppinglist)
        print(f"Total Price: ${total_price}")
    else:
        break