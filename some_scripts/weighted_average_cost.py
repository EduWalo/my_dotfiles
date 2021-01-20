import os
import time
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


##########################

# productos almacenados
stock = {
        "Manzanas":15
}
cppstock = {
        "Manzanas":1
}

# add item to stock
def add_item():
    clear()# clear console
    show_stock()
    print("ADD NEW PRODUCT\n")
    print("Enter the product name:\n>",end='>')
    name=input() 
    stock[name]=0
    cppstock[name]=0
    print("Add product successfulliy")
    time.sleep(.200)


# add item to stock with a initial units and the price
def add_item_complete():
    run_temp=True
    while run_temp:
        clear()# clear console
        show_stock()
        print("ADD NEW COMPLETE PRODUCT!!\n")
        print("Enter the product name:\n>",end='>')
        name=input() 
        print("Enter product quantity\n>",end='#')
        try:
            unit=float(input())
            print("Enter the TOTAL purchase price\n>",end='$')
            price=float(input())
            run_temp=False
        except:
            print("character error!")
            time.sleep(.200)


    stock[name]=unit
    cpp_temp = price/unit
    cppstock[name]=cpp_temp
    print("Add product successfulliy")
    time.sleep(.200)

# remove item to stock
def remove_item():
    clear()# clear console
    show_stock()
    print("REMOVE A PRODUCT\n")
    print("Enter the product name:\n>",end='>')
    name=input() 
    stock.pop(name,None)
    cppstock.pop(name,None)

# sell units of item
def sell_units():
    clear()
    show_stock()
    print("SELL UNITS\n")
    print("Enter the product name\n>",end='>')
    name=input()
    try:
        print("Enter the number of units to sell\n>",end='#')
        unit_sold=float(input())

        if name in stock:
            if stock[name] >= unit_sold:
                stock[name]-=unit_sold
            else:
                print ("units not enoug!!!\n\tthere are {0} but you try to extract {1}".format(stock[name],unit_sold))
        else:
            print ('The Product {0} does exist!!! :('.format(name))
    except:
        print("character error!!")
        time.sleep(.200)


# add units to item in the stock with a price
# NOTA: el precio que se ingresa es le precio total 
#       ejemplo: compre 15 manzanas a $15 en total, 
#       osea que cada manzana me costo 1
#       por ende el precio que debo ingresar a la funcion
#       es de 15 ->> add_unit_to('Manzana',15,15)
def add_unit_to():
    run_temp=True
    while run_temp:
        clear()# clear console
        show_stock()
        print("ADD NEW UNITS TO PRODUCT!!\n")
        print("Enter the product name:\n>",end='>')
        name=input() 
        print("Enter product quantity\n>",end='#')
        try:
            units=float(input())
            print("Enter the TOTAL purchase price\n>",end='$')
            total_price=float(input())
            run_temp=False
        except:
            print("character error!")
            time.sleep(.200)

    if name in stock:
        # calcular el cpp
        cpp_new = (stock[name]*cppstock[name] + units*total_price)/(stock[name]+units)
        
        # si está el item proceda a agregar unidades y se almacena el nuevo cpp
        stock[name]+=units
        cppstock[name]=cpp_new
    else:
        print ('The Product {0} does exist!!! :('.format(name))

    time.sleep(5)

# print all stock
def show_stock():
    cont=0
    print( '..{0:=^45}..'.format(''))
    print( '|<|{0: ^43}|>|'.format('STOCK'))
    print( '..{0:=^45}..'.format(''))

    for item in stock:
        print('|#| {0:.<25}${1:.<10}${2:.<8}'.format(item, stock[item], cppstock[item]))
        print(('{0: <48}-').format('-'))

    print("##")

# print menu
def show_menu():
    menu_items = [
            "Add empty product",
            "Add product with units and price",
            "Remove product", 
            "Add units to product", 
            "Sold units",
            "Exit"
    ]
    cont =0
    print( '|{0:=^41}|'.format("MENU") )
    for itm in menu_items:
        cont+=1
        print ('|[{0}] {1:.<37}|'.format(cont,itm))



def run():
    running = True # the continue interacition
    option_selecct = 0
    switcher = {
            1: lambda : add_item(),
            2: lambda : add_item_complete(),
            3: lambda : remove_item(),
            4: lambda :add_unit_to(),
            5: lambda : sell_units(),
            
    }
    while running:
        clear()
        show_stock()
        show_menu()
        print("\n\tSELECT SOME OPTION:\n>",end='>')
        try:
            option_select = int(input())
            if option_select != 6:
                 switcher.get(option_select, "Invalid option")() 
                 #time.sleep(2)
            else:
                running = False
                print("Bye!!")
        except:
            print("Error character!!")
        time.sleep(.20)

        # switch implement

