import re

print('''
        * * * * * * * * * * * * * * * * * *  * * * * * * * * * * * * * * * * * * * * * * * * 
        ** * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * **  
        ** Hello legend, this is a game where you have to enter some words to define how a  **
        ** story goes using your own words, so please choose your words carefully, and     **
        ** unleash the power of your imagination!!                                         **
        ** * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * **
        * * * * * * * * * * * * * * * * * *  * * * * * * * * * * * * * * * * * * * * * * * * 
          ''')

def read_template(path):
    '''this function reads the file 
       using the path provided and
       returns its content if it exists
       otherwise it raises and error
      '''
    try:
        with open(path, mode='r') as f: 
            res = f.read()
            print(res)  
            return res
    except FileNotFoundError:      
        raise FileNotFoundError("The file path {} does not exist.".format(path))
         



def parse_template(template):
    '''this function takes the file content and 
    removes the parts inside of curly brackets
    then return them in a tuple
    '''

    pattern = r'\{(\w+)\}'
    stripped = re.sub(pattern, '{}', template)
    parts = tuple(re.findall(pattern, template))
    return stripped, parts

    
def merge(template, input):
    '''this function merges the game template with the user input and returns
    the template filled with the input
    '''
    result = f"{template.format(*input)}"
    return result

def ourgame():
     '''
    this function returns the whole game script with the added parts from the user and prints it,
    it also writes the in a new text file
    '''
     our_game_text = read_template("assets/madlib.txt")
     filterd , parts = parse_template(our_game_text)
     print(parts)
     values = list()
     for part in parts:
        values.append(input(f"\n please enter a {part}\n"))
     with open("madlib.txt",'w') as file:
        game = merge(filterd,(tuple)(values))
        file.write(game)
        print(game)

if __name__ =="__main__":
      ourgame() 
     
     

