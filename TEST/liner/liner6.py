def solution(directory, command):
    for com in command:
        if 'mkdir' in com:
            directory.append(com[6:])

        elif 'rm' in com:
            for dir in directory:
                if com[3:] in dir:
                    directory.remove(dir)
        elif 'cp' in com:
            c = com.split(' ')
            stack = []
            for dir in directory:
                if c[1] != dir and c[1] in dir:
                    f=dir.split('/')
                    while f:
                        if f[0] != c[1][1:]:
                            f.pop(0)
                        else:
                            break
                    stack.append(c[2]+('/'+'/'.join(f)))
            print(stack
                  )
            directory.append(''.join(stack))
    return directory

directory=[
    "/",
    "/hello",
    "/hello/tmp",
    "/root",
    "/root/abcd",
    "/root/abcd/etc",
    "/root/abcd/hello"
]

command = [
"mkdir /root/tmp",
"cp /hello /root/tmp",
"rm /hello"
]

# directory=[
# "/"
# ]
#
# command = [
# "mkdir /a",
# "mkdir /a/b",
# "mkdir /a/b/c",
# "cp /a/b /",
# "rm /a/b/c"
# ]
print(solution(directory, command))
