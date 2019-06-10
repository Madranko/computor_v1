import sys
import parser

# print ("This is the name of the script: ", sys.argv[0])
# print ("Number of arguments: ", len(sys.argv))
# print ("The arguments are: " , str(sys.argv))

if (len(sys.argv) == 2) :

    
    try:
        parser = parser.Parser(sys.argv[1])
    except expression as identifier:
        pass



# 5*X^0+4*X^1-9.3*X^2=1*X^0


# 1) ([+-]?\d+(\.\d+)?\*X\^[0-2][+-=])+[+-]?     ---------------------------> 5*X^0+4*X^1+4*X^2=  
# 2) ([+-]?\d+(\.\d+)?)   ---->      4 | 444.433 | +2.33 | -1232.23
# 3) \*?(X(\^[0-2])?)     ---->      X | *X | *X^0 | X^0
# 4) ([+-]?\d+(\.\d+)?)(\*?(X(\^[0-2])?))?    ---->  2 and 3 combined


# 5) ^[+-]?(\d+(\.\d+)?(\*?X(\^[0-2])?)?([+-]\d+(\.\d+)?(\*?X(\^[0-2])?)?)?)+=[+-]?(\d+(\.\d+)?(\*?X(\^[0-2])?)?([+-]\d+(\.\d+)?(\*?X(\^[0-2])?)?)?)+$  ----> complete regular expression (no)
