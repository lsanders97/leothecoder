#Progam that implements a drive thru
food_type  = ''

def printBreakfast():
    print('  1. Chicken Biscut \n  2. Sausage Biscut\n  3. Sausage & Egg Biscut\n  4. Pancakes')

def printDinner():
    print('  1. Chicken Sandwhich \n  2. Burger \n  3. Salad\n  4. Chicken Wrap')

def breakfast(order):
    breakfast = {
        'Chicken Biscut' : 1,
        'Sausage Biscut' : 2,
        'Sausage & Egg Biscut' : 3,
        'Pancakes' : 4
             }
    
    price = 0
    total = 0
    for i in range(len(order)):
        if breakfast['Chicken Biscut'] ==  order[i]:
            price = 3.49
        elif breakfast['Sausage Biscut'] ==  order[i]:
            price = 3
        elif breakfast['Sausage & Egg Biscut'] ==  order[i]:
            price = 4.50 
        elif breakfast['Pancakes'] ==  order[i]:
            price = 2
        total += price 
    print('Your total is $'+ str(total))
    
def dinner(order):    
    dinner = {
        'Chicken Sandwhich' : 1,
        'Burger' : 2,
        'Salad' : 3,
        'Chicken Wrap' : 4
    }
    
    price = 0
    total = 0
    for i in range(len(order)):
        if dinner['Chicken Sandwhich'] ==  order[i]:
            price = 3.49
        elif dinner['Burger'] ==  order[i]:
            price = 3
        elif dinner['Salad'] ==  order[i]:
            price = 4.50 
        elif dinner['Chicken Wrap'] ==  order[i]:
            price = 2
        total += price 
    print('Your total is $'+ str(total))

print('Welcome to Leo\'s Dinner!')
food_type = input(' 1.Breakfast\n 2.Dinner\n')
if food_type == '1':
        print('Welcome to Leo\'s Dinner! Here is our breakfast menu.')
        printBreakfast()
elif food_type == '2':
    print('Welcome to Leo\'s Dinner! Here is our dinner menu.')
    printDinner()

order = []
while True:    
    x = int(input('What would you like to order?'))
    order.append(x)
    choice = input('Would you like to order anything else? Y/N\n').upper()
    if choice == 'N' and food_type == '1':
        breakfast(order)
        break
    elif choice == 'N' and food_type == '2':
        dinner(order)
        break
    elif choice != 'Y':
        print('Incorrect input. Enter either Y OR N.')
        break
