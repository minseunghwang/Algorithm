f = open('data/1223.txt','r',encoding='UTF-8').readlines()
t=101
s=f[1]
num_stack=[]
op_stack=[]
temp=[]
temp2=[]
for i in range(t):
    if i%2==0:
        num_stack.append(int(s[i]))
    else:
        op_stack.append(s[i])

while op_stack!=[]:
    print(op_stack)
    if op_stack[-1]=='*':
        temp2.append(num_stack.pop(-1))
        print(temp2)
    else:
        temp.append(num_stack.pop(-1))
        if op_stack!=[]:
            temp.append(op_stack.pop(-1))
    while temp2!=[]:
        temp_result=1
        while op_stack[-1]=='*':
            temp2.append(op_stack.pop(-1))
            temp2.append(num_stack.pop(-1))
            if op_stack==[]:
                break
        for j in range(0,len(temp2),2):
            temp_result*=temp2[j]
        temp2=[]
        temp.append(temp_result)
        if op_stack!=[]:
            temp.append(op_stack.pop(-1))
if num_stack!=[]:
    temp.append(num_stack.pop(-1))
ans=0
for k in range(0,len(temp),2):
    ans+=temp[k]

print("#{}".format(ans))