N, M = map(int, input().split())  # N : num of idol, M : num of quiz

# Using Dictionary
team_mem, mem_team = {}, {}

for i in range(N):
    team_name, member = input(), int(input())
    team_mem[team_name] = []
    for j in range(member):
        member_name = input()
        team_mem[team_name].append(member_name)
        mem_team[member_name] = team_name

for i in range(M):
    name, q = input(), int(input())
    if q:
        print(mem_team[name])
    else:
        for mem in sorted(team_mem[name]):
            print(mem)
