def dfs(hp, dungeon, cnt,dungeons):
    global answer,visit
    if cnt == len(dungeons) and hp >= 0:
        answer = max(answer, cnt)
        return
    
    for dungeon_idx in range(len(dungeons)):
        if visit[dungeon_idx] == 1:
            continue
        
        if dungeons[dungeon_idx][0] <= hp:
            visit[dungeon_idx] = 1
            dfs(hp-dungeons[dungeon_idx][1],dungeons[dungeon_idx], cnt+1,dungeons)
            visit[dungeon_idx] = 0
        else:
            answer = max(answer, cnt)

def solution(k, dungeons):
    global visit,answer
    visit = [0] * len(dungeons)
    answer = 0
    for i,dungeon in enumerate(dungeons):
        if k>= dungeon[0]:
            visit[i] = 1
            dfs(k-dungeon[1],dungeon, 1,dungeons)
            visit[i] = 0
    return answer