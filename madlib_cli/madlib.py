import re

def play_madlib(path):
    template = read_template(path)
    stripped_template, parts = parse_template(template)
    print(
    """ Welcome to MADLIB!
    let's play a game!
    """)
    print(stripped_template)
    user_inputs = []
    for part in parts:
        user_input = input(f"Enter a {part}: ")
        user_inputs.append(user_input)
    madlib = merge(stripped_template, user_inputs)
    print(madlib)
    with open("assets/madlib.txt", "w") as file:
        file.write(madlib)

   
def read_template(path):
    try:
       with open(path) as file:
        return file.read().strip()
    except FileNotFoundError as err:
        print('file not found, kindly change the path!')
        print(err)
        raise FileNotFoundError
    
def parse_template(template):
   parts=re.findall(r'\{([^{}]+)\}',template) #Using this regex method to find the words between paranthesis in the template file.
   stripped = re.sub(r'\{([^{}]+)\}', '{}', template) # This regex method substitute the desired words.
   return (stripped, tuple(parts))

def merge(template,parts):
   try:
      return template.format(*parts)
   except KeyError as err:
      print(f'Error!,there is a missing key, {err} , in user input ')

play_madlib("assets/dark_and_stormy_night_template.txt")