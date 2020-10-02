user_input = input()
q = []
for i in user_input.split():
		if i in q:
				q.pop(q.index(i))
		q.insert(0, i)
		if len(q) > 5:
				q.pop(-1)
		print(" ".join(q))
