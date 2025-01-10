
if __name__ == '__main__':
    team1_name = 'Мастера кода'
    team2_name = 'Волшебники данных'
    team1_num = 5
    team2_num = 6
    score_1 = 40
    score_2 = 42
    team1_time = 1552.512
    team2_time = 2153.31451
    tasks_total = 82
    time_avg = 45.2
    print("В команде %s участников: %s ! " % (team1_name, team1_num))
    print("В команде %s участников: %s ! " % (team2_name, team2_num))
    print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))
    print("Команда {0} решили задач:{1}!".format(team1_name, score_1))
    print("Команда {0} решила задач:{1}!".format(team2_name, score_2))
    print("{0} решили задачи за {1} c!".format(team1_name, team1_time))
    print("{0} решили задачи за {1} c!".format(team2_name, team2_time))

    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = f'победа команды {team1_name}!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = f'победа команды {team2_name}!'
    else:
        result = 'Ничья!'
    print(f'Результат битвы:{result}!')

    tasks_total = score_1 + score_2
    time_avg = round((team1_time + team2_time) / tasks_total, 1)
    print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")