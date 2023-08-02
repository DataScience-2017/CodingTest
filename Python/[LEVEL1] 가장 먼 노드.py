from collections import deque

def solution(n, edge):
    answer = 0
    # 연결된 노드 정보 그래프
    graph =[[] for _ in range(n+1)]
    # 각 노드의 최단거리 리스트
    distance = [-1] *(n+1)
    
    # 연결된 노드 정보 추가
    for e in edge :
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    # BFS를 위한 queue, 출발노드 =1
    queue = deque([1])
    # 출발노드의 최단거리를 0으로
    distance[1] = 0
    
    # BFS 수행
    while queue :
        now = queue.popleft() # 현재 노드
        
        # 현재 노드에서 이동할 수 있는 모든 노드 확인
        for i in graph[now]:
            if distance[i]== -1: # 아직 방문하지 않은 노드면,
                queue.append(i) # queue에 추가
                distance[i] = distance[now]+1 # 최단거리 갱신
                
    # 가장 멀리 떨어진 노드 개수 구하기                
    for d in distance:
        if d == max(distance):
            answer += 1
            
    return answer


**BFS (Breadth-First Search)**는 그래프 자료구조에서 사용되는 탐색 알고리즘 중 하나로, 너비 우선으로 그래프를 탐색하는 방법입니다. 출발 노드에서 시작하여 인접한 노드를 모두 탐색한 후, 그 인접한 노드들의 인접한 노드를 탐색하는 식으로 단계별로 탐색을 진행합니다.

구체적인 알고리즘 설명:

graph 변수에는 노드들 간의 연결 정보를 저장한 그래프가 생성됩니다.
distance 변수는 각 노드까지의 최단 거리를 저장하는 리스트입니다. 최단 거리를 찾기 위해 -1로 초기화합니다.
노드 연결 정보를 바탕으로 graph를 만듭니다. 양방향으로 연결되어 있기 때문에 두 노드를 모두 추가합니다.
BFS를 위한 큐인 queue를 생성합니다. 출발 노드는 1로 설정합니다.
출발 노드의 최단 거리를 0으로 설정하고, BFS를 시작합니다.
BFS를 수행하면서 각 노드까지의 최단 거리를 계산하고, distance 리스트에 갱신해 나갑니다.
모든 노드를 탐색한 뒤, 가장 멀리 떨어진 노드의 개수를 구합니다.
이 알고리즘을 이용하여 주어진 그래프에서 출발 노드인 1부터 다른 노드까지의 최단 거리를 구한 뒤, 가장 먼 거리에 있는 노드의 개수를 반환하는 것이 이 코드의 목표입니다.
