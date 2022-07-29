

items = [
    {
        'code':"1",
        'name':'coca cola',
        'price':'5'
    },

    {
        'code':"2",
        'name':'cadbury',
        'price':'10'
    },

    {
        'code':"3",
        'name':'chips',
        'price':'2'
    },

    {
        'code':"4",
        'name':'krukure',
        'price':'2'
    },

    {
        'code':"5",
        'name':'diet coke',
        'price':'3'
    },

    {
        'code':"6",
        'name':'mineral water',
        'price':'1'
    },
    {
        'code':"7",
        'name':'Milkshake',
        'price':'5'
    },

    {
        'code':"8",
        'name':'peanuts',
        'price':'2'
    },

    {
        'code':"9",
        'name':'soda water',
        'price':'1'
    },

    {
        'code':"10",
        'name':'coffe',
        'price':'5'
    },

    {
        'code':"11",
        'name':'lassi',
        'price':'5'
    },

]
cart = []
is_quit = False
item = ''
bill = 0 

while is_quit == False:
    print("Welcome to the vending machine")
    for i in items:
        print(f"Item Name: {i['name']} - Price: {i['price']} - code: {i['code']}")
    query = input("Enter the code number of the item you want to get:   ")
    for i in items:
        if query == i['code']:
            item = i
    if item == '' :
        print('INVALID CODE')
        continue
    else:
        print(f"Great, {item['name']} will cost you {item['price']} dollars")
        cart.append(item['name'])
       
        print(f"This is your cart:{cart} ")
        bill = bill+int(item['price'])
        cont  = input("Press 'a' to continue or ESC for bill  :")
        if cont == "a":
            query = input("Enter the code number of the item you want to get: ")

            for i in items:
                if query == i['code']:
                    item = i
            if item == '':
                print('INVALID CODE')
                continue
            else:
                print(f"Great, {item['name']} will cost you {item['price']} dollars")
                cart.append(item['name'])
                print(f"This is your cart:{cart} ")
                bill = bill+int(item['price'])
                price = int(input(f"Enter {bill} dollars to purchase: "))

                if price == bill:
                    print(f"Thank you for buying here is your {item['name']}")
                else:
                    print(f"Please enter only {bill} dollars")
                    continue 
                                  
        else:
            price = int(input(f"Enter {bill} dollars to purchase: "))

            if price == bill:
                print(f"Thank you for buying here is your {item['name']}")
                
            else:
                print(f"Please enter only {bill} dollars")
                continue                     

    query = input("To quit the machine enter q and to continue buying enter anything: ")
    if query == 'q':
        is_quit = True
    else:
        is_quit = False