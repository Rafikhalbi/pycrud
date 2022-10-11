from function import *

class systemCreate:
  def __init__(self) ->None:
    pass
  def execution_create(self):
    while(True):
      name = input('\n(?) Name: ')
      try:
        nik = int(
          input('(?) Nik: ')
          )
      except:
        exit('(!) Nik must number')
      print(
        '\n\t! example: 16-02-2000'
        )
      birth = input('(?) Birthday: ')
      location = input('(?) address: ')
      break
    save_data = open(f'data_crud/{nik}.txt','w')
    save_data.write(f'{name}|{nik}|{birth}|{location}')
    save_data.close()
    ptext(
      '(✓) Succes Tambahkan Data'
      )