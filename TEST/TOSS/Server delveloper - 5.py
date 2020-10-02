user_input = input()
user_input2 = input()

answer = []
a = 0
for i,j in zip(user_input.split(),user_input2.split()):
	if int(i) - int(j) - a >= 0:
		answer.append(str(int(i) - int(j) - a))
		a = 0
		continue
	a += int(j) - int(i)
	answer.append(str(0))
print(" ".join(answer))