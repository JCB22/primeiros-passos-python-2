# Get Operation vai nos permitir usar aquelas expressões que são
# Comumente usadas por alguns programas, como o -m para mandar mensagem
# No commit do git
import getopt
import sys

opts, args = getopt.getopt(sys.argv[1:],"f:m:", ["filename", 'message'])

# O opts só vai receber argumentos que tenham "-f" ou "-m" inseridos anteriormente
# ATENÇÃO: O opts tem que aparecer antes do args, senão o args vira prioridade ou algo
# do genero
# print(opts)
# print(args)

for opt, arg in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg

with open(filename, 'w+') as f:
    f.write(message)
