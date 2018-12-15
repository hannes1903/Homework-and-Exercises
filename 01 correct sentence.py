
a = 'hannes is good in pythoning'

def correct_text(text):
    text = text[0].upper() + text[1:]
    if not text.endswith ('.'):
        text += '.'
    return (text)

#print(text)

print (correct_text(a))

#text = text[0].upper() + text[1:]
#if not text.endswith('.'):
#    text += '.'

# print (text1)

# better with functions, as if I call from other file it would not be automatically executed, but would be imported and
# only executed when I want (eg by print later)

# function that does not return anything, is called procedure