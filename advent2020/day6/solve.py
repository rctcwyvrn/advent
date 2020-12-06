from input import *

split = x.split("\n")

quizzes = []
q = []
for line in split:
    if line == "":
        quizzes.append(q)
        q = []
    else:
        q.append(line)
quizzes.append(q)

#total = 0
# for q in quizzes:
#     print(q, set("".join(q)))
#     total += len(set("".join(q)))

# print(total)

total = 0
for q in quizzes:
    running = set(q[0])
    for ans in q:
        print(running)
        running = running & set(ans)
    print(q,running)
    total+= len(running)
print(total)