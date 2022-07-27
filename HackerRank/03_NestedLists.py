if __name__ == '__main__':

    """
    _list = []


    n = int(input())
 
    for _ in range(n):
        _list = list(map(str, input()), map(float, input()))[:n]


    _list.remove(max(_list))
    print(max(_list))
    """

    marksheet = []
    for _ in range(0, int(input())):
        marksheet.append([input(), float(input())])

    second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
    print('\n'.join([a for a, b in sorted(marksheet) if b == second_highest]))
