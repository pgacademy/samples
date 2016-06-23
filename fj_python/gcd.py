import sys

m, n = int(sys.argv[1]), int(sys.argv[2])

if n < m:
  m, n = n, m

while n != 0:
  m, n = n, m % n

print(m)

