import re
import math

class Computor:

    def __init__(self, equation):
        self.equation = equation
        self.reducedForm = ''
        self.polynomialDegree = 0
        self.discriminant = None
        self.solutions = {
            'first': None,
            'second': None
        }
        self.coefficients = {
            'a': 0,
            'b': 0,
            'c': 0
        }

    def makeReducedForm(self):
        self.addEqualPowers()
        for token in self.equation:
            value = self.makeReadableValue(token['value'])
            power = self.makeReadablePower(token['power'])
            self.reducedForm += value + power
        self.formatReducedForm()
        return self.reducedForm

    def addEqualPowers(self):
        powers = [token['power'] for token in self.equation]
        newEquation = []
        for i in range(0, max(powers) + 1):
            listOfEqualPowers = [item for item in self.equation if item['power'] == i]
            member = self.addPowers(listOfEqualPowers)
            if member['value']:
                newEquation.append(member)
        self.equation = newEquation

    def addPowers(self, equalPowers):
        if equalPowers:
            newValue = {'value': 0, 'power': equalPowers[0]['power']}
            for token in equalPowers:
                newValue['value'] += token['value']
        else:
            newValue = {'value': None, 'power': None}
        return newValue


    def getPolynomialDegree(self):
        powers = [token['power'] for token in self.equation]
        self.polynomialDegree = max(powers)
        return self.polynomialDegree


    def makeReadableValue(self, intVal):
        return str(intVal) if intVal <= 0 else '+' + str(intVal)

    def makeReadablePower(self, intPower):
        if intPower == 0:
            power = ''
        elif intPower == 1:
            power = '*X'
        else:
            power = '*X^' + str(intPower)
        return power

    def formatReducedForm(self):
        if self.reducedForm[0] == '+':
            self.reducedForm = self.reducedForm[1:]
        self.reducedForm = " ".join(self.reducedForm) + ' = 0'
        pattern = re.compile(r"(?:( (?=(\.|\^)))|((?<=(\.|\^)) ))|((?<=\d) (?=\d))")
        self.reducedForm = re.sub(pattern, '', self.reducedForm)

    def findDiscriminant(self):
        if self.polynomialDegree > 2:
            raise Exception("The polynomial degree is stricly greater than 2, I can't solve.")
        else:
            self.writeCoefficients()
            if self.polynomialDegree == 2:
                self.discriminant = self.coefficients['b']**2 - 4 * self.coefficients['a'] * self.coefficients['c']
        return self.discriminant

    def writeCoefficients(self):
        a = [item for item in self.equation if item['power'] == 2]
        b = [item for item in self.equation if item['power'] == 1]
        c = [item for item in self.equation if item['power'] == 0]
        self.coefficients['a'] = 0 if not a else a[0]['value']
        self.coefficients['b'] = 0 if not b else b[0]['value']
        self.coefficients['c'] = 0 if not c else c[0]['value']
        print('a:', self.coefficients['a'])
        print('b:', self.coefficients['b'])
        print('c:', self.coefficients['c'])

    def findSolutions(self):
        if self.discriminant:
            if self.discriminant >= 0:
                self.solutions['first'] = self.calcSolutionByDiscriminant(-1)
                self.solutions['second'] = self.calcSolutionByDiscriminant(1)
                # print('=======================')
                # print(self.solutions)
                # print('=======================')
                # pass  # todo: find solutions by discriminant
            else:
                pass  # todo: throw no solutions
        else:     # None
            pass  # todo: if polynomialDegree -> find one solution else  all the real numbers are solution
        return self.solutions

    def calcSolutionByDiscriminant(self, discrCoefficient):
        numerator = -1 * self.coefficients['b'] + discrCoefficient * math.sqrt(self.discriminant)
        denominator = 2 * self.coefficients['a']
        return numerator / denominator




















