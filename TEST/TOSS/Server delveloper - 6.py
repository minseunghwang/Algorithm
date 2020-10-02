user_input = input()
table = user_input.split(';')
print(table)
matrix = []
for i in table:
	temp = []
	for j in i.split():
		temp.append(int(j))
	matrix.append(temp)

for i in matrix:
	for j in i:

