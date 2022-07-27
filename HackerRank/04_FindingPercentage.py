"""

The provided code stub will read in a dictionary containing key/value pairs of
name:[marks] for a list of students. Print the average of the marks array for
the student name provided, showing 2 places after the decimal.


Input:

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Output:

56.00

To no ponto que meu ingles nao me ajuda a explicar o que caralhos que eu estou fazendo.
Puta que pariu melhora a curva de aprendizado, HackerRank.

"""

# Import decimal
from decimal import Decimal


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()


# Extract the values into a list: query_scores
query_scores = student_marks[query_name]

# Sum the scores in the list: total_scores
total_scores = sum(query_scores)

# Convert the floats to decimals and average the scores: avg
avg = Decimal(total_scores/3)

# Print the mean of the scores, correct to two decimals
print(round(avg,2))
