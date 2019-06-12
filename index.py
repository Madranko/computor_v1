import sys

# print ("This is the name of the script: ", sys.argv[0])
# print ("Number of arguments: ", len(sys.argv))
# print ("The arguments are: " , str(sys.argv))

colors = {'fail': '\033[91m', 'success': '\033[92m'}

def solveEquation(equation):
    import parser
    import computor

    if equation:
        print('=================================================')
        print('Input:', equation)
        parser = parser.Parser(equation)

        try:
            parsedLine = parser.parseLine()
        except Exception as error:
            print(error)
            return

        computor = computor.Computor(parsedLine)
        try:
            reducedForm = computor.makeReducedForm()
        except Exception as error:
            print(error)
            return

        degree = computor.findPolynomialDegree()
        print('Reduced form:', reducedForm)
        print('Polynomial degree:', degree)
        print('Coefficients:')
        print(' A:', computor.coefficients['c'])
        print(' B:', computor.coefficients['b'])
        print(' C:', computor.coefficients['a'])

        try:
            discriminant = computor.findDiscriminant()
            if discriminant != None: print('Discriminant:', discriminant)
        except Exception as error:
            print(error)
            return

        solutions = computor.findSolutions()
        print(solutions['comment'])
        if solutions['first'] != None: print('X1:', solutions['first'])
        if solutions['second'] != None: print('X2:', solutions['second'])

if len(sys.argv) > 1:
    if sys.argv[1] == '-f':
        for file in sys.argv[2:]:
            try:
                with open(file, 'r') as fp:
                    for line in fp:
                        solveEquation(line.strip())
            except FileNotFoundError:
                print(colors['fail'] + file + ": File not found")
    else:
        solveEquation(sys.argv[1])
