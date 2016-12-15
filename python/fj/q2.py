l = [ "a", "b", "c", "a", "a", "b", "a", "a" ]

results = {}

for i in l:
  if i not in results:
    results[i] = 1
  else:
    results[i] = results[i] + 1

for item in results.items():
  print("{0} ... {1}".format(item[0], item[1]))

