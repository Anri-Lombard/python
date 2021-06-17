import math
m_and_n = input().split(" ")
m, n = int(m_and_n[0]), int(m_and_n[1])

max_dominoes = math.floor(n*(m/2))

print(max_dominoes)
