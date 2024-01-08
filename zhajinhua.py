import random

if __name__ == '__main__':
    poker = [(i, k) for i in range(2, 15) for k in range(4)]
    # print(poker)
    players = [[] for i in range(5)]
    for i in range(5):
        for j in range(3):
            t = random.randrange(0, len(poker))
            players[i].append(poker[t])
            del poker[t]
    # print(players)
    for i in players:
        i.sort()
    # print(players)
    scores = [[0, 0, i] for i in range(1, 6)]
    for i in range(5):
        t = players[i]
        if t[0][0] == t[1][0] and t[1][0] == t[2][0]:
            scores[i][0] = 5
            scores[i][1] = t[0][0]
            
        elif t[0][0] == t[1][0] - 1 and t[1][0] == t[2][0] - 1:
            if t[0][1] == t[1][1] and t[1][1] == t[2][1]:
                scores[i][0] = 4
                scores[1][1] = t[2][0]
                continue
            scores[i][0] = 3
            scores[i][1] = t[2][0]
            
        elif t[0][0] == t[1][0]:
            scores[i][0] = 2
            scores[i][1] = t[0][0]
            
        elif t[1][0] == t[2][0]:
            scores[i][0] = 2
            scores[i][1] = t[1][0]
            
        else:
            scores[i][0] = 1
            scores[i][1] = t[2][0]
    ans = sorted(scores, key = lambda x: (x[0], x[1]), reverse=True)
    # print(ans)
    print("获胜者为：")
    print(ans[0][2])
    