import re

class Parser :

    fullPattern = "^([+-]?\d+(\.\d+)?(\*?X(\^[0-2])?)?([+-]\d+(\.\d+)?(\*?X(\^[0-2])?)?)?)+=([+-]?\d+(\.\d+)?(\*?X(\^[0-2])?)?([+-]\d+(\.\d+)?(\*?X(\^[0-2])?)?)?)+$"
    tokenPattern = "([+-]?\d+(\.\d+)?(\*?X(\^[0-2])?)?)"

    def __init__(self, line) :
        self.line = line

    def parseLine(self) :
        self.line = "".join(self.line.split())
        if (self.lineIsValid()) :
            self.line = self.line.replace("*", "")
            # self.mooveRightSideToLeft()
            self.parseLineOnTokens(self.line)
            # print(self.line)


    def lineIsValid(self) :
        if (re.fullmatch(self.fullPattern, self.line)) :
            return True
        else :
            raise Exception('Invalid argument')

    def parseLineOnTokens(self, line) :
        result = re.findall(self.tokenPattern, line)
        print(result)
        # print(result.start())
        # print(result.end())


    def mooveRightSideToLeft(self) :
        splitedLine = self.line.split("=")
        rightSide = splitedLine[1]
        leftSide = splitedLine[0]
        


# +4*X^1-9.3*X^2=-4*X^1-9.3*X^2




# (\d(\.\d)?(\*X(\^[0-2])?)?)