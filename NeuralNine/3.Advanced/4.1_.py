import sys

# Agora você vai ter que clicar no terminal e escrever "python3 4.1_.py" e o que for que você
# escrever vai ser considerado um argv, dividindo cada argv por espaço, incluindo o nome do arquivo
# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])

# Agora se você não cortar os argvs você nao vai ter que se preocupar com
# A limitação no exemplo acima, porque tudo que você adicionar vai fazer parte
# De uma sequência
# print(sys.argv)

filename = sys.argv[1]
message = sys.argv[2]
with open(filename, 'w+') as f:
    f.write(message)