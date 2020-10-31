# Morse code conversion
A small snippet to convert text into morse code.
Created the core of it working on another project, but thought this could be useful for others too.

## Dictionary
```
CHARACTERS = {'A': '.- ',     'B': '-... ',   'C': '-.-. ', 
              'D': '-.. ',    'E': '. ',      'F': '..-. ',
              'G': '--. ',    'H': '.... ',   'I': '.. ',
              'J': '.--- ',   'K': '-.- ',    'L': '.-.. ',
              'M': '-- ',     'N': '-. ',     'O': '--- ',
              'P': '.--. ',   'Q': '--.- ',   'R': '.-. ',
              'S': '... ',    'T': '- ',      'U': '..- ',
              'V': '...- ',   'W': '.-- ',    'X': '-..- ',
              'Y': '-.-- ',   'Z': '--.. ',   ' ': ' ',        
              '0': '----- ',  '1': '.---- ',  '2': '..--- ',
              '3': '...-- ',  '4': '....- ',  '5': '..... ',
              '6': '-.... ',  '7': '--... ',  '8': '---.. ',
              '9': '----. '}
```

## Function
```
#Input should be string
def encode(msg):
    m_msg=''
    for char in msg:        
        m_msg += CHARACTERS[char.upper()]    
    return m_msg
```