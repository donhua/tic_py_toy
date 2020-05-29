import random
import os


def title_win(level: int = 0):
    """Возвращает сообщение о текущем уровне игрока"""
    return "Текущий ровень: " + str(level)


def random_int(x: list):
    """Возвращает два целых числа для задания с суммой до x: int"""
    assert len(x) == 2, "Недопустимое количество аргументов для интервала значений"
    assert x[1]-x[0] >= 0, "Недопустимый интервал начений"
    a = random.randint(x[0], x[1])
    b = random.randint(x[0], x[1]-a)
    ints = [a, b]
    assert x[0] <= sum(ints) >= x[1], "Недопустимое финишное значение"
    return ints


def finish_value(ints, x: list):
    """Принимает список с целыми числами, возвращает сумму"""
    a = sum(ints)
    assert x[0] <= a >= x[1], "Недопустимое финишное значение"


def num_sum(ints):
    """Принимает список с двумя целыми числами и преобразует в текст примера"""
    return str(ints[0]+"+"+ints[1]+"=")


def value_buttons(finished_value: int, number_buttons: int, x: list):
    """принимаеи финишное значение, количестко кнопок, максимально возможное финишное значение (по умолчанию 10)
       Возвращает список значений кнопок для вариантов ответа"""
    data = [i for i in range(x[0], x[1]+1)]
    assert x[0] <= finished_value >= x[1], "Недопустимое финишное значение"
    data.remove(finished_value)
    random.shuffle(data)
    data1 = data[:number_buttons-1]
    data1.append(finished_value)
    random.shuffle(data1)
    return data1


def list_img(n: int):
    """Возвращает список изображенйи для кнопок из дериктории с изображениями кнопок"""
    directory = os.getcwd() + "\\btn_image"
    files = os.listdir(directory)
    images = filter(lambda x: x.endswith('.png'), files)
    assert len(images) > 0, "Изображения кнопок отсутствуют"
    assert len(images) <= n, "Изображений кнопок меньше, чем возможное максимальное значение ответов"
    return images

def level_dif(level):
    """Реализует возможный интервал ответов"""
    if level == 0:
        return [0, 4]
    if level == 1:
        return [2, 6]
    if level == 2:
        return [3, 8]
    if level == 3:
        return [4, 10]
    return [0, 10]
