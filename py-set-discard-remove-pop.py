# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
numbers = set()

for x in (raw_input().split(' ')):
  numbers.add(int(x))

for x in range(int(raw_input())):
  cmd = raw_input().split(' ')
  if cmd[0] == 'pop':
    numbers.pop()
  elif cmd[0] == 'remove':
      numbers.remove(int(cmd[1]))
  else:
    numbers.discard(int(cmd[1]))

print sum(numbers)