def solution(cap, n, deliveries, pickups):
  # 배달과 픽업 시간 리스트를 역순으로 바꿉니다.
  deliveries = deliveries[::-1]
  pickups = pickups[::-1]
  # 총 소요 시간을 저장하는 변수를 초기화합니다.
  answer = 0
  
  # 배달하고 픽업해야 하는 택배량을 저장하는 변수를 초기화합니다.
  have_to_deli = 0
  have_to_pick = 0
  
  # 각 택배에 대해
  for i in range(n):
      # 배달해야 하는 택배량과 픽업해야 하는 택배량을 각각 더합니다.
      have_to_deli += deliveries[i]
      have_to_pick += pickups[i]
  
      # 배달하고 픽업해야 하는 택배량이 있을 동안
      while have_to_deli > 0 or have_to_pick > 0:
          # 한 번에 배달하거나 픽업할 수 있는 만큼 택배량을 줄입니다.
          have_to_deli -= cap
          have_to_pick -= cap
          # 총 소요 시간에 (n - i) * 2를 더합니다.
          # 이는 택배를 배달하고 픽업하는 데 걸리는 시간을 계산하는 것으로 보입니다.
          answer += (n - i) * 2
  
  # 총 소요 시간을 반환합니다.
  return answer


# cap: 한 번에 배달하거나 픽업할 수 있는 최대 택배량
# n: 택배의 총 개수
# deliveries: 각 택배가 배달되는데 필요한 시간 리스트
# pickups: 각 택배를 픽업하는데 필요한 시간 리스트
