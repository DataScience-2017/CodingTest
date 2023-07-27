def solution(temperature, t1, t2, a, b, onboard):
    # onboard의 크기를 N으로 정의합니다. (탑승 상황이 기록된 리스트의 길이)
    N = len(onboard)
    # 온도를 조정하기 편하게 하기 위해 실외온도, t1, t2 모두 10을 더합니다.
    temperature += 10
    t1 += 10
    t2 += 10

    # INF를 정의합니다. 여기서는 매우 큰 값(10e4)으로 설정하여, 아직 계산되지 않은 dp 값이나, 온도 조정이 불가능한 경우를 나타냅니다.
    INF = 10e4
    # dp라는 2차원 리스트를 생성합니다. 이 리스트는 가능한 모든 온도(0~50)와 시간(0~N-1)에 대해 최소 비용을 저장합니다.
    dp = [[INF] * N for _ in range(51)]
    # 초기 상태, 즉 첫 날의 실외 온도에 대한 비용은 0입니다.
    dp[temperature][0] = 0

    # 각 날짜에 대해 dp 테이블을 업데이트합니다.
    for i in range(N - 1):
        # 가능한 모든 온도에 대해
        for t in range(51):
            # 현재 온도가 불가능한 경우 (비용이 INF인 경우) 건너뜁니다.
            if dp[t][i] == INF:
                continue
            # 온도를 1 올리거나, 그대로 유지하거나, 1 내리는 경우를 고려합니다.
            for dt in (1, 0, -1):
                nt = t + dt
                # 에어컨의 희망 온도를 결정하고, 이에 따른 비용을 계산합니다.
                if nt == temperature: dc = 0
                elif nt == t: dc = b
                elif t < temperature and dt == 1: dc = 0
                elif t > temperature and dt == -1: dc = 0
                else: dc = a

                # 희망 온도가 범위를 벗어나는 경우는 무시합니다.
                if nt < 0 or nt > 50:
                    continue
                # 승객이 탑승하고 있고 희망 온도가 허용 범위를 벗어나는 경우도 무시합니다.
                if (onboard[i + 1] == 1) and (nt > t2 or nt < t1):
                    continue

                # 다음 날의 희망 온도에 대한 비용을 업데이트합니다. 이전 비용과 현재 계산된 비용 중 작은 것을 선택합니다.
                dp[nt][i + 1] = min(dp[nt][i + 1], dp[t][i] + dc)

    # 모든 날짜에 대한 계산이 끝났으면, 마지막 날에 가능한 모든 온도 중 최소 비용을 찾습니다.
    answer = min(dp[i][-1] for i in range(51))
    return answer
