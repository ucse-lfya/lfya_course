import os
import sys
import importlib

files = os.listdir('.')
module_file = [f.split('.')[0] for f in files if 'grupo' in f][0]

grupo = importlib.import_module(module_file)

samples = [
    ('''SELECT c.first_name,
               c.last_name
        FROM customers AS c''', {'customers': ['first_name', 'last_name']}),
    ('''SELECT c.first_name,
               c.last_name
        FROM customers AS c
        WHERE c.id = 2''', {'customers': ['first_name', 'last_name', 'id']}),
    ('''SELECT DISTINCT c.first_name,
                        c.last_name,
                        p.number
        FROM customers AS c
            LEFT JOIN phones_numbers AS p ON
                c.id = p.customer_id
        ''', {'customers': ['first_name', 'id', 'last_name'],
              'phones_numbers': ['customer_id', 'number']})
    ]

for ix, sample in enumerate(samples):
    print('***** Resultados test parsing ejemplo {} *****'.format(ix+1))
    print(sample[0])
    print('-' * 3, ' Fin consulta ', '-' * 3)

    try:
        result = grupo.parse_select_statement(sample[0])

        if result != sample[1]:
            resultStr = 'incorrecto'
        else:
            resultStr = 'correcto'

        print('El resultado de la comprobación fue {} !'.format(resultStr))
        print('Resultado entregado: ', result)
        print('Resultado esperado: ', sample[1])

    except Exception as e:
        print('''Se produjo una excepción al intentar parsear el ejemplo y/o 
                 comprobar el resultado !''')
        print(e)
    print('')
