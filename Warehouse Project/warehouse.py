


"""

Program: Warehouse inventory control system
Funcionality:
    -Register new items
        id (auto generated)
        title
        category
        price
        stock
    -Print all the items
    -Update the stocks of a selected item
    -Print item with no stock
    -Remove items

    -Print Diffferent Categories
    -Print stock value (sum(price * stock))
    -register purcHASE
    -Register Sell
    -Log of events
        Time | Action | itemId
        12:20 | sell | 98


        1 - generate log string inside important function
        2 - add that string to logs array
        3 - save logs array
        4 - load logs array when system starts

"""

from menu import print_menu
from items import Item
import datetime
import pickle

items = []
logs = []
id_count = 1
items_file = "item.data"
logs_file = "logs.data"

def get_time():
    current_date = datetime.datetime.now()
    time = current_date.strftime("%X")
    return time

def remove_item():
    print_all("Choose an Item to Remove")
    id = input("\nSelect an ID to remove item: ")
    found = False
    for item in items:
        if(str(item.id) == id ):
            items.remove(item)
            print(" Item has been removed!")
            log_line = get_time() + " | Item Removal |" + id
            logs.append(log_line)
            save_log()



    if(not found):
        print("** Error, ID does not exist, try again **")




def save_items():
    #open creates/opens a file
    writer = open(items_file, "wb")#wb = write binary info
    pickle.dump(items, writer) #converts the object into binary and writes in on the file
    writer.close()#closes the file stream (to release the file)
    print("Data Saved!!")

def read_logs():

    try:
        reader = open(logs_file, "rb")#rb = open the file to Read Binary
        temp_list = pickle.load(reader) # read the binary and convert it the original object

        for log in temp_list:
            logs.append(log)

            print("Loaded: " + str(len(temp_list)) + " Events")
    except:
        #you get here if try black crashes
        print("Error: Data could not be loaded!")

def read_items():
    global id_count #import variable into function scope

    try:
        reader = open(items_file, "rb")#rb = open the file to Read Binary
        temp_list = pickle.load(reader) # read the binary and convert it the original object

        for item in temp_list:
            items.append(item)

            last = items[-1]
            id_count = last.id + 1
            print("Loaded: " + str(len(temp_list)) + " items")
    except:
        #you get here if try black crashes
        print("Error: Data could not be loaded!")

def print_header(text):
    print("\n\n")
    print("*"*80)
    print(text)
    print("*"*80)

def list_all_categories():
    print_header("List of all Categories")
    temp_list =[]
    for item in items:
        if (item.category not in temp_list):
            temp_list.append(item.category)
    print(temp_list)

def print_all(header_text):
    print_header(header_text)
    print("-"*70)
    print("ID |Item Title               |Category       | Price   | Stock")
    print("-"*70)
    for item in items:
        print( str(item.id).ljust(3) + "|" + item.title.ljust(25) + "|" + item.category.ljust(15) + "|" +
        str(item.price).rjust(9) + "|" + str(item.stock).rjust(6))


def register_item():
    global id_count #importing the global variable, into function scope

    print_header(" Regsiter new Item ")
    title = input("Please input the Title: ")
    category = input("Please input the Category: ")
    price = float(input("Please input the Price: "))
    stock= int(input("Please input the Stock: "))

    #validations

    new_item = Item()
    new_item.id = id_count
    new_item.title = title
    new_item.category = category
    new_item.price = price
    new_item.stock = stock


    id_count += 1
    items.append(new_item)
    print(" Item Created!! ")
    log_line = get_time() + " | Register New Item |" + id
    logs.append(log_line)
    save_log()


def print_stock_value():
    total = 0
    for item in items:
        total += (item.price * item.stock)

    print("Total Stock Value: " + str(total))

def update_stock():
    # show the user all the items
    #ask for the desired id
    #get the element from the array with that id
    #ask for the new stock
    #update the stock of the element
    print_all("Choose an Item from the list")
    id = input("\nSelect an ID to update its stock: ")
    #find the element
    found = False
    for item in items:
        if(str(item.id) == id ):
            stock = input("Please input new stock value: ")
            item.stock = int(stock)
            found = True

            #  add regustry to the log
            log_line = get_time() + " | Update |" + id
            logs.append(log_line)
            save_log()


    if(not found):
        print("** Error, ID does not exist, try again **")





read_items()
read_logs()

def save_log():
    writer = open(logs_file, "wb")#wb = write binary info
    pickle.dump(logs, writer) #converts the object into binary and writes in on the file
    writer.close()#closes the file stream (to release the file)
    print("Log Saved!!")



def register_purchase():
    """
    show the items
    ask for the user to select 1
    ask for the quantity in the irder (purchase)
    update the stock of the selected item
    """
    print_all("Choose an Item from the list")
    id = input("\nSelect an ID to purchase that Item: ")
    for item in items:
        if(str(item.id) == id ):
            stock = input("Please input Quantity of the item you wish to buy: ")
            item.stock += int(stock)
            print(item.stock)
            found = True
            log_line = get_time() + " | Purchase Made |" + id
            logs.append(log_line)
            save_log()

            print("Thank you for you purchase")

    if(not found):
        print("** Error, ID of Item  does not exist, try again **")

def register_sell():

    print_all("Choose an Item from the list")
    id = input("\nSelect an ID to sell that Item: ")
    for item in items:
        if(str(item.id) == id ):
            stock = input("Please input Quantity of the item you wish to sell: ")
            item.stock -= int(stock)
            print(item.stock)
            found = True
            print("Thank you for you purchase")
            log_line = get_time() + " | Sell Executed |" + id
            logs.append(log_line)
            save_log()

def print_log():

    for logs in logs_list:
        print(logs)


def list_nostock():
    print_header("List of Items with ZERO STOCK")
    for item in items :
        if (item.stock == 0):
            print(item.title)

opc = ''
while(opc != 'x'):
    print("\n\n\n")
    print_menu()


    opc= input("Please select an option:  ")

    # actions based on selected opc

    if(opc == "1"):
        register_item()
        save_items()
    elif(opc == "2"):
        print_all("List of all Items")
    elif(opc == "3"):
        update_stock()
        save_items()
    elif(opc == "4"):
        list_nostock()
    elif(opc == "5"):
        remove_item()
        save_items()
    elif(opc == "6"):
        list_all_categories()
    elif(opc == "7"):
        print_stock_value()
    elif(opc == "8"):
        register_purchase()
    elif(opc == "9"):
        register_sell()
    elif(opc == ""):
        print_log()




    if(opc != 'x'):
        input("\n\nPress Enter to continue...")
