from function import *

class systemRead:
  def __init__(self) ->None:
    pass
  def execution_read(self,cursor):
    data = os.listdir('./data_crud')
    loop = 0
    ptext('=======================')
    ptext(
      '(!) Menampilkan Data Users:\n'
      )
    for data_users in data:
      try:
        file = open(f'./data_crud/{data_users}','r').read().splitlines()
        for user in file:
          name,nik,birthday,address = user.split('|')
          loop+=1
      except:
        exit(
          '(!) No File.'
          )
      print(
        f'({loop}) Name: {name}\n    Nik: {nik}\n    Birthday: {birthday}\n    Address: {address}\n'
        )