

# single line comment

"""
Program: Warehouse inventory control system
Functionality:
  -Register new items
    id (auto generated)
    title
    category
    price
    stock

  - Print all the items
  - Update the stock on the selected items

"""

from menu import print_menu
from items import Item

items = []
id_count = 1

def print_header(text):
    print("\n\n")
    print("*" * 50)
    print(text)
    print("*" * 50)

def print_all(header_text):
    print_header(header_text)
    print("-" * 71)
    print("id  | Item Title                | Category        | Price     | Stock")
    print("-" * 71)

    for item in items:
        print( str(item.id).ljust(3) + " | " + item.title.ljust(25) + " | " + item.category.ljust(15) + " | " + str(item.price).rjust(9) + " | " + str(item.stock).rjust(5))

 
def register_item():
    global id_count # importing the global variable, into fn scope

    print_header(" Register new item")
    title = input("Please input the title: ")
    category = input("Please input the category: ")
    price = float (input("Please input the price: "))
    stock = int(input("Please input the stock: "))

    # validations

    new_item = Item()
    new_item.id = id_count
    new_item.title = title
    new_item.category = category
    new_item.price = price
    new_item.stock = stock

    id_count += 1
    items.append(new_item)
    print("Item created!!!")

def update_stock():
  # Show the users all the items
  # ask for the desired id
  # get the element from the array with that id
  # ask fir the new stock
  # update the stock of the element
  print_all("Choose an item from the list")
  id = input("\nSelect an ID to update its stock: ")
  # find the element
  found = False
  for item in items:
      if(str(item.id) == id):
          stock = input("Please input new stock value: ")
          item.stock = int(stock)
          found = True

  if(not found):
    print(" ***** Error. ID does not exist. Try again.... *****")


      
      


# feed test data

i1 = Item()
i1.id = 1
i1.title = "Green"
i1.category ="Color"
i1.price = 1.99
i1.stock = 45
items.append(i1)

i2 = Item()
i2.id = 2
i2.title = "Yes"
i2.category ="Sign"
i2.price = 13.99
i2.stock = 11
items.append(i2)
id_count = 3



opc = ''
while(opc != 'x'):
    print("\n\n\n")
    print_menu()

    opc = input("Please select an option: ")

    #actions based on selected opc
    if (opc == "1"):
        register_item()

    elif(opc == "2"):
        print_all("List of all items")
    
    elif(opc == "3"):
        update_stock()

    if (opc != "x"):
      input("\n\nPress Enter to continue...")

    



