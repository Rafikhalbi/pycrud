import os 

def ptext(text):
  print(text)
  
def cls():
  if os.name == 'posix':os.system('clear')
  else:os.system('cls')