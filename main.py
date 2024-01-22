#This is a mose code translator bot

#This is a dictionary of english to morse code
english_to_morse = {
#Alphabet   
    'A': '.-', 
    'B': '-...', 
    'C': '-.-.', 
    'D': '-..', 
    'E': '.', 
    'F': '..-.', 
    'G': '--.', 
    'H': '....', 
    'I': '..', 
    'J': '.---', 
    'K': '-.-', 
    'L': '.-..', 
    'M': '--', 
    'N': '-.', 
    'O': '---', 
    'P': '.--.', 
    'Q': '--.-', 
    'R': '.-.', 
    'S': '...', 
    'T': '-', 
    'U': '..-', 
    'V': '...-', 
    'W': '.--', 
    'X': '-..-', 
    'Y': '-.--', 
    'Z': '--..',

    #Numbers
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-','5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', 

#Punctuation
    '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', 
    '(': '-.--.', ':': '---...', ',': '--..--', '=': '-...-', 
    '!': '-.-.--', '.': '.-.-.-', '-': '-....-', '+': '.-.-.', 
    '"': '.-..-.', '?': '..--..', '/': '-..-.', ' ': ' ', 
    '\n': '\n'

}

#get user input
user_string = input ('Enter the text you want to translate: ')

#translate the text
def translate(text):
    #make the text uppercase
    text = text.upper()
    #create a variable to hold the morse code
    morse_string = ""
    #loop through each character in the text
    for char in text:
        try:
            if char == " ":
                morse_string += "   "
            else:
                morse_string += english_to_morse[char] + " "
        except KeyError:
            print("Sorry, that is an invalid character: " + char + ". Please try again.")

    #error handling for keyError chracters not in the dictionary
        
    

    return(morse_string) 



#output the translated text
print(translate(user_string))



    