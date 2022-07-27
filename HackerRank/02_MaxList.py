

if __name__ == '__main__':
    i = int(input("Insira a quantidade de competidores"))
    lis = list(map(int, input(f'escreva a pontuação de todos os concorrentes, dividindo os por espaço.').split()))[:i]

    lis.remove(max(lis))

    print(f'{max(lis)} foi a pontuação de quem ficou em segundo!')
