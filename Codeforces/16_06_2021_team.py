number_of_problems = input()
implemented_solutions = 0
for _ in range(int(number_of_problems)):
    certainty = input().split(" ")
    if certainty.count("1") >= 2:
        implemented_solutions += 1
print(implemented_solutions)
