import heapq
from math import inf

def solution(n, paths, gates, summits):
 
    # 간선 정보 정리 (양방향)
    # 그래프를 구성하기 위해 비어있는 리스트를 만들고, 
    # 입력받은 모든 경로를 두 지점 간의 양방향으로 표시합니다.
    graph = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])

    # 산봉우리 판별
    # 산봉우리 여부를 저장할 리스트를 만들고,
    # 입력받은 산봉우리의 위치를 True로 표시합니다.
    is_summit = [False] * (n + 1)
    for summit in summits:
        is_summit[summit] = True

    # gate를 모두 시작 위치로 설정
    # 각 지점에서의 최단 거리를 무한대(inf)로 초기화한 후,
    # 게이트의 위치에서의 거리는 0으로 설정합니다.
    # 그리고 이를 힙에 삽입합니다.
    distance = [inf] * (n + 1)
    queue = []
    for gate in gates:
        distance[gate] = 0
        heapq.heappush(queue, [0, gate])

    # 다익스트라 알고리즘
    # 힙에서 최소 거리의 지점을 추출하면서,
    # 그 지점에서의 거리가 이미 저장된 거리보다 크거나,
    # 해당 지점이 산봉우리라면 무시하고 다음으로 넘어갑니다.
    # 그렇지 않다면, 해당 지점과 연결된 모든 지점에 대해
    # 거리를 갱신하고, 갱신된 지점을 다시 힙에 삽입합니다.
    while queue:
        d, i = heapq.heappop(queue)
        if distance[i] < d or is_summit[i]:
            continue
        for j, dd in graph[i]:
            dd = max(distance[i], dd)
            if distance[j] > dd:
                distance[j] = dd
                heapq.heappush(queue, [dd, j])

    # 결과 반환
    # 모든 산봉우리에 대해,
    # 거리가 가장 짧은 산봉우리와 그 거리를 반환합니다.
    # 만약 거리가 같은 산봉우리가 여러 개라면,
    # 산봉우리의 번호가 작은 것을 반환합니다.
    result = [-1, inf]
    for summit in sorted(summits):
        if distance[summit] < result[1]:
            result[0] = summit
            result[1] = distance[summit]
    return result
