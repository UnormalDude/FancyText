#MADE BY JOHN CUNNINGTON
#THIS CODE IS A CUSTOM MODULE TO ALLOW FOR EASIER CHANGING OF FORMATTING OF A PYTHON SCRIPT WHILE BEING EXTREMELY MINIMAL. NO OTHER LIBRARIES ARE NEEDED

def text_edit(name):

    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white' ] #List of available colors
    color_codes = ['31', '32', '33', '34', '35', '36', '37'] #The ANSI codes that correlate

    if name in colors: #If the color name is available 
        index = colors.index(name) #Get the index of the color
        code = color_codes[index] #Get the correlated ANSI code
        return f"\033[{code}m" #Plug it into the format here
        
    elif name == "italic":
        return "\x1B[3m"
    
    elif name == "bold":
        return "\033[1m"
    
    elif name == "title":
        return "\033[1m\x1B[3m"
    
    elif name == "reset": #Return text to default
        return "\033[0m"

    #COLORS-----------------------------------------------------------------------------

    else:
        return "" #return nothing if the arg does not exist in the code
