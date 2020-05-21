import os
import sys
import importlib

files = os.listdir('.')
module_file = [f.split('.')[0] for f in files if 'grupo' in f][0]

grupo = importlib.import_module(module_file)

grammars = [
    ['X:X Y\nX:e\nX:b\nX:lambda\nY:a\nY:d', True, ('bd$', 'X=>X Y=>b Y=>b d')]
]

for ix, grammar in enumerate(grammars):
    print('***** Resultados test gramática {} *****'.format(ix+1))

    try:
        g = grupo.Gramatica(grammar[0])

        isLL1 = g.isLL1()
        parseResult = g.parse(grammar[2][0])

        resultStr = ''
        if isLL1 != grammar[1]:
            resultStr = 'incorrecto'
        else:
            resultStr = 'correcto'

        print('El resultado del método isLL1 es {} !'.format(resultStr))
        print('Resultado entregado: ', isLL1)
        print('Resultado esperado: ', grammar[1])

        if parseResult != grammar[2][1]:
            resultStr = 'incorrecto'
        else:
            resultStr = 'correcto'

        print('El resultado del método Parse es {} !'.format(resultStr))
        print('Resultado entregado: ', parseResult)
        print('Resultado esperado: ', grammar[2][1])

    except Exception as e:
        print('''Se produjo una excepción al intentar leer el string
                 con la gramática !''')
        print(e)
    print('')
