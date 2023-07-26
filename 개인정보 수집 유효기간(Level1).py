# 연, 월, 일을 받아서 고유한 숫자로 바꾸는 함수입니다.
def change_to_date(year, month, date):
    return int(year) * 12 * 28 + int(month) * 28 + int(date)

# 주어진 조건에 따라 답을 찾는 함수입니다.
def solution(today, terms, privacies):
    answer = []  # 답을 저장할 리스트입니다.

    terms_dict = {}  # 조건을 저장할 딕셔너리입니다.
    for info in terms:  # 각 조건에 대해
        type_, month = info.split(' ')  # 정보를 분리하고
        terms_dict[type_] = change_to_date(0, month, 0)  # 딕셔너리에 저장합니다.

    # 현재 날짜를 숫자로 바꿉니다.
    today_date = change_to_date(*today.split('.'))

    # 각 개인 정보에 대해
    for i in range(len(privacies)):
        date, type_ = privacies[i].split(' ')  # 정보를 분리하고
        # 만료일을 계산합니다.
        due_date = change_to_date(*date.split('.')) + terms_dict[type_] - 1

        # 현재 날짜가 만료일보다 크면
        if today_date > due_date:
            answer.append(i + 1)  # 답 리스트에 추가합니다.

    return answer  # 답 리스트를 반환합니다.
