import datetime as dt


def win_no_full(count_level, count_life, count_ball):
    with open('results.txt', encoding='utf-8') as f:
        information = f.read()
    with open('results.txt', 'w', encoding='utf-8') as f:
        print(count_life, count_ball)
        date = str(dt.datetime.now().date())
        time = str(dt.datetime.now().time())[:-7]
        tab = '\t' * 6
        print(date, time)
        f.write(information)
        f.write('\n')
        f.write('-' * 80 + '\n')
        f.write(f"<{date}> {time}\tИгрок прошел игру, но набрал не полное количество очков."
                f"\n{tab}Количество пройденных уровней: {count_level}."
                f"\n{tab}Количество жизней по окончанию игры: {count_life}."
                f"\n{tab}Количество набранных очков: {count_ball}.\n")
        f.write('-' * 80 + '\n\n')


def win_full(count_level, count_life, count_ball):
    with open('results.txt', encoding='utf-8') as f:
        information = f.read()
    with open('results.txt', 'w', encoding='utf-8') as f:
        print(count_life, count_ball)
        date = str(dt.datetime.now().date())
        time = str(dt.datetime.now().time())[:-7]
        tab = '\t' * 6
        print(date, time)
        f.write(information)
        f.write('\n')
        f.write('-' * 80 + '\n')
        f.write(f"<{date}> {time}\tИгрок прошел игру полностью."
                f"\n{tab}Количество пройденных уровней: {count_level}."
                f"\n{tab}Количество жизней по окончанию игры: {count_life}."
                f"\n{tab}Количество набранных очков: {count_ball}.\n")
        f.write('-' * 80 + '\n\n')


def lose(count_level, count_life, count_ball):
    with open('results.txt', encoding='utf-8') as f:
        information = f.read()
    with open('results.txt', 'w', encoding='utf-8') as f:
        print(count_life, count_ball)
        date = str(dt.datetime.now().date())
        time = str(dt.datetime.now().time())[:-7]
        tab = '\t' * 6
        print(date, time)
        f.write(information)
        f.write('\n')
        f.write('-' * 80 + '\n')
        f.write(f"<{date}> {time}\tИгрок потерял все жизни и проиграл."
                f"\n{tab}Количество пройденных уровней: {count_level}."
                f"\n{tab}Количество жизней по окончанию игры: {count_life}."
                f"\n{tab}Количество набранных очков: {count_ball}.\n")
        f.write('-' * 80 + '\n\n')