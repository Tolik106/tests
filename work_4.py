# Нужно реализовать функцию, принимающую список чисел. Вывести число,
# которое встречается чаще всего. Максимальное число голосов всегда уникально.
#
# В результате корректного выполнения задания будет выведен следующий результат:
#
# 1
# 2
# 1
# 2


times = 0


def vote(vote_1, vote_2):
    global times
    votes = []
    votes.append(vote_1)
    votes.append(vote_2)
    times += 1
    count = []
    for i in votes:
        count.append(votes.count(i))
        max_times = max(count)
        n = count.index(max_times)
        result = f"{votes[n]}"
    print(result)
    return (result)


if __name__ == '__main__':
    vote(1, 2)
    vote(2, 2)