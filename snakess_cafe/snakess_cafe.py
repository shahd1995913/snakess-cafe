print("**************************************")
print("**    Welcome to the Snakes Cafe!   **")
print("**    Please see our menu below.    **")
print("**")
print("** To quit at any time, type ""quit"" **")
print("*************************************")

print("""
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears


***********************************
** What would you like to order? **
***********************************
""")


dict = {
  "Coffee": 0,
  "Tea": 0,
  "Pie": 0,
  "Unicorn Tears":0,
  "Cake":0,
  "Ice Cream":0,
   "A Literal Garden":0,
  "Meat Tornado":0,
  "Salmon":0,
   "Cake":0,
  "Spring Rolls":0,
  "Wings":0,
   "A Literal Garden":0,
  "Meat Tornado":0,
  "Steak":0,
   "Cookies":0,
}                      

newitem=input("Please Insert New Item :").title()
while newitem != "Quit":
    if(newitem in dict):
        dict[newitem]=dict[newitem]+1
        for item in dict:
            if(dict[item] >0 ):
                print("** "+  str(dict[item]) +" order of " + item+" have been added to your meal **")
   
    else:
        print("the item you ordered is not on the menu but we will get it for you")
        dict[newitem] = 1  
        print("**"+  str(dict[newitem]) +" order of " + newitem+" have been added to your meal ** ")

    newitem=input("Please Insert New Item :").title()

   

