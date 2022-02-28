'''
Nested Lists
Given the names and grades for each student in a class of
students, store them in a nested list and print the name(s)
of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest
grade, order their names alphabetically and print each name
on a new line.

Input Format

The first line contains an integer, N, the number of
students. The subsequent 2N lines describe each student
over 2 lines.
- The first line contains a student's name.
- The second line contains their grade.
'''
def Nested_Lists(nlist):
    names = []
    scores = []

    for i in nlist:
        names.append(i[0])
        scores.append(i[1])
    
    lowestscore = min(scores)
    count = 0
    for i in range(len(scores)):
        if scores[i] == lowestscore:
            count += 1

    for j in range(count):
        names.pop(scores.index(min(scores)))
        scores.pop(scores.index(min(scores)))

    nlowestscore = min(scores)
    nworst_students = []
    for i in range(len(scores)):
        if scores[i] == nlowestscore:
            nworst_students.append(names[i])
    
    nworst_students.sort()

    for n in nworst_students:
        print(n)

if __name__ == '__main__':
    nlist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nlist.append([name, score])
    Nested_Lists(nlist)