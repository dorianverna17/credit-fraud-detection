file = open('credit_datasheet.csv')
file_write = open('credit_datasheet_head.csv', 'w')

number_of_lines = 70000
lines = []

for i in range(number_of_lines):
    line = file.readline()
    lines.append(line)

file_write.writelines(lines)
