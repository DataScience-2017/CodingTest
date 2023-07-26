def change_to_date(year, month, date):
    return int(year) * 12 * 28 + int(month) * 28 + int(date)

def solution(today, terms, privacies):
    answer = []

    terms_dict = {}
    for info in terms:
        type_, month = info.split(' ')
        terms_dict[type_] = change_to_date(0, month, 0)

    today_date = change_to_date(*today.split('.'))

    for i in range(len(privacies)):
        date, type_ = privacies[i].split(' ')
        due_date = change_to_date(*date.split('.')) + terms_dict[type_] - 1

        if today_date > due_date:
            answer.append(i + 1)

    return answer
