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


Dictionarie = {
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

newitem=input("> ").title()

while newitem != "Quit":
    if(newitem in Dictionarie):
        Dictionarie[newitem]=Dictionarie[newitem]+1
        for item in Dictionarie:
            if(Dictionarie[item] >0 ):
                print("** "+  str(Dictionarie[item]) +" order of " + item+" have been added to your meal **")
   
    else:
        print("The order you want to order Not in  the menu, please order food from the menu ")
       

    newitem=input("> ").title()

   

