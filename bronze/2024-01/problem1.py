# n = 5
# s = 2 - 1
# types = [0, 1, 1, 0, 1]
# values = [1, 1, 2, 1, 1]
n = 6
s = 4 - 1
types = [0, 1, 1, 1, 0, 1]
values = [3, 1, 2, 1, 1, 1]

power = 1
direction = 1
breaks = set()

# may need to track (s, direction, power) in a visited set to avoid infinite loop
while s >= 0 and s < n and len(breaks) < n:
  print(s, direction, power, breaks)
  if types[s] == 0:
    power += values[s]
    direction *= -1
    s += direction * power
    continue

  if power >= values[s]:
    breaks.add(s)
  s += direction * power

print('result', breaks)
