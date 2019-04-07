"""from pycipher import Playfair
print(Playfair("cdabefhgkijlmnoprqstuvzwxy").encipher("hello world"))

print(Playfair("cdabefhgkijlmnoprqstuvzwxy").decipher("IDOVNXLTRH"))
"""

from pycipher import ADFGVX
adfgvx = ADFGVX(key='PH0QG64MEA1YL2NOFDXKR3CVS5ZW7BJ9UTI8', keyword='GERMAN')
_ = adfgvx.encipher("Hello world!")
print(adfgvx.encipher("Hello world!"))
print(adfgvx.decipher(_))
