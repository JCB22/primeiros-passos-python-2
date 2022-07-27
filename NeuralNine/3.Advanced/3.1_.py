def infinitesequence():
    result = 1
    while True:
        yield result
        result *= 5


values = infinitesequence()


# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))

# for x in values:
#     print(x)

for x in range(500):
    print(next(values))