def solution(snapshots, transactions):
    transaction = list(set(map(tuple,transactions)))
    snap = []
    for i in snapshots:
        snap.append(i[0])

    for i in transaction:
        if i[1] == 'SAVE':
            if i[2] not in snap:
                snapshots.append([i[2],'0'])
            for j in snapshots:
                if i[2] == j[0]:
                    j[1] = str(int(j[1]) + int(i[3]))
        elif i[1] == 'WITHDRAW':
            for j in snapshots:
                if i[2] == j[0]:
                    j[1] = str(int(j[1]) - int(i[3]))
    return snapshots



snapshots = [
      ["ACCOUNT1", "100"],
      ["ACCOUNT2", "150"]
]
transactions = [
      ["1", "SAVE", "ACCOUNT2", "100"],
      ["2", "WITHDRAW", "ACCOUNT1", "50"],
      ["1", "SAVE", "ACCOUNT2", "100"],
      ["4", "SAVE", "ACCOUNT3", "500"],
      ["3", "WITHDRAW", "ACCOUNT2", "30"]
]
print(solution(snapshots, transactions))