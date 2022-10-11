# system crud python

class System_crud:
  def __init__(self):
    pass
  def menu_tools(self,cursor='\n(•)\t>> '):
    while(True):
      cls()
      ptext(
        '\t[ S Y S T E M C R U D ]\n\n(1) Create Data\n(2) Read Data\n(3) Update Data\n(4) Delete Data\n(5) Exit Program'
        )
      option = input(
        cursor
        )
      match option:
        case '1':
          create_data = create.systemCreate.execution_create(self)
          option_back = input(
            '\n(?) Back To Menu (y/n): '
            )
          if(option_back in['y','Y']):
            pass
          else:
            exit(
              '(✓) Program Finished'
              )
        case '2':
          read_data = read.systemRead.execution_read(self,cursor)
          option_back = input(
            '(?) Back To Menu (y/n): '
            )
          if(option_back in['y','Y']):
            pass
          else:
            exit(
              '(✓) Program Finished'
              )
        case '3':
          update_data = update.systemUpdate.execution_update(self,cursor)
          option_back = input(
            '\n(?) Back To Menu (y/n): '
            )
          if(option_back in['y','Y']):
            pass
          else:
            exit(
              '(✓) Program Finished'
              )
        case '4':
          data = os.listdir('data_crud')
          loop=0
          for items in data:
            loop+=1
            for users in items.splitlines():
              check = open(f'./data_crud/{users}','r').read()
              name = check.split('|')[0]
              print(f'({loop}) {items} => {name}')
          file_option = input(
            '\n(?) Input File: '
            )
          try:
            check = open(f'./data_crud/{file_option}','r').read()
            name = check.split('|')[0]
          except:
            exit(
              '(!) File Not Found.'
              )
          delete_option = input(
            f'(?) Are You Sure Delete {file_option} => {name}? (y/n): '
            )
          if(delete_option in['y','Y']):
            os.remove(f'data_crud/{file_option}')
            ptext(
              '(✓) Remove Succes.'
              )
          else:
            pass
          option_back = input(
            '\n(?) Back To Menu (y/n): '
            )
          if(option_back in['y','Y']):
            pass
          else:
            exit(
              '(✓) Program Finished'
              )
        case '5':
          exit(
            '(✓) Program Finished'
            )
              
if __name__=='__main__':
  from function import *
  from utilities import create,read,update
  crud = System_crud()
  crud.menu_tools()