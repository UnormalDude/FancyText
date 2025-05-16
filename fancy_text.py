#MADE BY JOHN CUNNINGTON
#THIS CODE IS A CUSTOM MODULE TO ALLOW FOR EASIER CHANGING OF FORMATTING OF A PYTHON SCRIPT WHILE BEING EXTREMELY MINIMAL. NO OTHER LIBRARIES ARE NEEDED

def text_edit(name):

    colors = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white' ] #List of available colors
    color_codes = ['30', '31', '32', '33', '34', '35', '36', '37'] #The ANSI codes that correlate

    if name in colors: #If the color name is available 
        index = colors.index(name) #Get the index of the color
        code = color_codes[index] #Get the correlated ANSI code
        return f"\033[{code}m" #Plug it into the format here
    

    elif name == "slow_blink":
        return "\033[5m"
    
    elif name == "blink":
        return "\x1b[6m"
        
    elif name == "italic":
        return "\x1B[3m"
    
    elif name == "bold":
        return "\033[1m"
    
    elif name == "title":
        return "\033[1m\x1B[3m"
    
    elif name == "reset": #Return text to default
        return "\033[0m"

    else:
        return "" #return nothing if the arg does not exist in the code

def background_color(color):
    colors = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    color_ids = ['40', '41', '42', '43', '44', '45', '46', '47']
    if color in colors:
        index = colors.index(color)
        code = color_ids[index]
        return f'\033[{code}m'
    else:
        return ''