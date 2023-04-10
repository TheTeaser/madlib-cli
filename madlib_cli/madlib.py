import re

print(
    """ Welcome to MADLIB!
    let's play a game!
""")

   
def read_template(path):
    try:
       test1=open(path)
       return test1.read()
    except FileNotFoundError as err:
        print('file not found, kindly change the path!')
        print(err)

