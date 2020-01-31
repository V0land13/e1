import random

tasks_list = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
task = random.choice(tasks_list)

#Классы для ввода одного символа
class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

getch = _Getch()
#Окончание описания классов для ввода одного символа

def letter_check(letter, cheched_word):
    #проверяет есть буква ли она в слове
    #Если есть возврашает True и список с номерами вхождений
    #Если нет возвращает False
    indexis = []
    if letter in cheched_word:
        counter = cheched_word.count(letter)
        if counter == 1:
            indexis.append(cheched_word.find(letter))
        elif counter == 2:
            indexis.append(cheched_word.find(letter))
            indexis.append(cheched_word.rfind(letter))
        else:
            for i in range(0, len(cheched_word)):
                if cheched_word[i] == letter:
                    indexis.append(i)
        return True, indexis
    else:
        return False, indexis

def game_visilica(checked_word):
    # program main function
    #print(checked_word)
    print('Слово загадано! У тебя будет 4 попытки чтобы его отгадать.')
    hiden_task = []
    for i in task:
        hiden_task.append('_')
    print('Загаданно слово: %s.' % ' '.join(hiden_task))
    error_summ = 0
    while error_summ < 4:
        if hiden_task.count('_') != 0:
            print('Осталось ', 4-error_summ, ' попыток. Введи букву:')
            il = getch()
            print(il)
            this_try = letter_check(il, checked_word)
            if this_try[0]:
                for ii in range(0, len(this_try[1])):
                    hiden_task[this_try[1][ii]] = il
                    print('Загаданно слово: %s.' % ' '.join(hiden_task))
            else:
                error_summ += 1
        else:
            return 'Поздравляем, Вы победили, загаданное слово {}!'.format(checked_word)
    return 'Все попытки изчерпаны, это поражение'

print(game_visilica(task))