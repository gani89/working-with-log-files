# in first part, we are writing specific lines that contain specific error log lines from log file into new file

input_file = open('log_file.txt')
output_file = open('error_lines.txt', 'w')

for line in input_file:
    if 'changed state to down' in line:
        output_file.write(line)

input_file.close()
output_file.close()

################################################################################3333

# in second part, finding and saving into new file interface numbers from that specific error log lines
import re

with open('error_lines.txt', 'r') as myfile:
  data = myfile.read().split()         # converting file to list

output_file2 = open('error_interfaces.txt', 'w') # creating new file to save interface numbers

pattern = re.compile(r'\bG.*\d') # search pattern for new list

for line in data:
    if pattern.search(line) != None:
        output_file2.write(line + ' ')

output_file2.close()
myfile.close()

################################################################################3333

# in third part, finding top-N interfaces

from collections import Counter

with open('error_interfaces.txt', 'r') as myfile:
    words = myfile.read().split()

counter = Counter(words)
top_three = counter.most_common(3)

print('Here are the top 3 interfaces with most flaps:')
print(*list(top_three), sep='\n')

myfile.close()
