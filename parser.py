import re

class Parser :

    pattern = "^([+-]?\d+(\.\d+)?(\*?X(\^[0-2])?)?([+-]\d+(\.\d+)?(\*?X(\^[0-2])?)?)?)+=([+-]?\d+(\.\d+)?(\*?X(\^[0-2])?)?([+-]\d+(\.\d+)?(\*?X(\^[0-2])?)?)?)+$"
        #      ^[+-]?(\d+(\.\d+)?(\*?X(\^[0-2])?)?([+-]\d+(\.\d+)?(\*?X(\^[0-2])?)?)?)+=[+-]?(\d+(\.\d+)?(\*?X(\^[0-2])?)?([+-]\d+(\.\d+)?(\*?X(\^[0-2])?)?)?)+$

    def __init__(self, line) :
        self.line = line

    def parseLine(self) :
        self.line = "".join(self.line.split())
        print (self.line)
        if (self.lineIsValid()) :
            print("Olala")


    def lineIsValid(self) :
        if (re.fullmatch(self.pattern, self.line)) :
            return true
        else :
            raise Exception('Invalid argument')
