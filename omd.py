def step2_umbrella():
    print(
        'Утка-маляр не спешила домой до дождя и хорошенько'
        ' назюзюкалась в баре. '
        'Поздравляю, вы споили утку.'
    )


def step2_no_umbrella():
    print(
        'Утка-маляр быстро опрокинула пару пинт и убежала домой до дождя. '
        'Поздравляю, вы испортили утке веселый вечер.'
    )


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
