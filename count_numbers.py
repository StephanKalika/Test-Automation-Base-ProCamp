sum = 0

with open('numbers.txt', 'r') as input:
   for line in input:
       try:
           num = float(line)
           sum += num
       except ValueError:
           print('{} is not a number!'.format(line))

print(f'Sum of all numbers: {sum}')