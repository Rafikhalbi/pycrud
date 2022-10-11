from function import *

class systemUpdate:
  def __init__(self) ->None:
    pass
  def execution_update(self,cursor):
    file = os.listdir('./data_crud',)
    loop=0
    ptext('=======================')
    for data_users in file:
      loop+=1 
      users = open(f'./data_crud/{data_users}','r').read()
      name = users.split('|')[0]
      ptext(
        f'({loop}) {data_users} => {name}'
        )
      # users = open(f'./data_crud/{data_users}')
      # name,nik,birthday,address = users.split('|')
    file_option = input(
      '\n(?) Input File: '
      )
    try:
      check = open(f'./data_crud/{file_option}','r').read()
      name,nik,birthday,address = check.split('|')
      ptext('=======================')
      ptext(
        '(!) previous data:\n',
        )
      print(
        f'(•) Name: {name}\n    Nik: {nik}\n    Birthday: {birthday}\n    Address: {address}\n'
        )
    except:
      exit(
        '(!) File Not Found.'
        )
    ptext('(*) Update Data')
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
    save_option = input(
      '(?) Update Data? (y/n): '
      )
    if(save_option in['y','Y']):
      save_data = open(f'data_crud/{nik}.txt','w')
      save_data.write(f'{name}|{nik}|{birth}|{location}')
      save_data.close()
      ptext(
        '(✓) Success Update Data'
        )
    else:
      exit(
        '(✓) Finished Program.'
        )