#A simple programs thats adds users
def createUser():
  print('Enter your username: ')
  userName=input()
  print('Create a password: ')
  password=input()
  while len(password)< 8  :
    
    if len(password) < 8 :
      print('Password is less than 8 characters!')
      print('Try again: ')
      password=input()
    else:
      print('Created successfully!')
  

