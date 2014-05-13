#coding: utf-8
import sys
import time


class StepTimer:
    """Интервальный таймер.

    Позволяет измерять время выполнения различных участков кода. Началом
    отсчета времени является момент создания экземпляра класса. При вызове
    метода print_info() выводится сообщение с информацией о времени, прошедшем
    с момента предыдущего вызова метода print_info() и с момента создания
    файла.
    """
    def __init__(self, name=None, out=sys.stdout):
        """
        :param str name: Имя таймера. Если указано, то выводится при каждом
            вызове print_info(). Если не указано, то выводится порядковый номер
            вызова print_info().
        :param out: Поток, в который будут выводится сообщения. По умолчанию -
            sys.std.out.
        """
        self.name = name
        self.print_count = 0
        self.start_time = self.last_time = time.time()
        self.out = out

    def print_info(self, label=None):
        """Выводит в указанный поток (параметр out конструктора класса) текущие
        параметры таймера в следующих форматах:

        [label: 1.234s. - step, 4.567s. - total] - класс создан без имени,
        в print_info() передан label;

        [1: 1.234s. - step, 4.567s. - total] - класс создан без имени,
        в print_info() не передавался label, вместо label выводится порядковый
        номер вызова print_info();

        <timer_name [label: 1.234s. - step, 4.567s. - total]> - при создании
        экземпляра класса было указано имя, в print_info() был передан label;

        <timer_name [1: 1.234s. - step, 4.567s. - total]> - при создании
        экземпляра класса было указано имя, в print_info() не передавался
        label, вместо label выводится порядковый номер вызова print_info().
        """
        t = time.time()
        self.print_count += 1

        if self.name:
            self.out.write(u'<%s ' % self.name)

        self.out.write(u'[%s: %.3fs. - step, %.3fs. - total]' % (
            label or unicode(self.print_count),
            t - self.last_time,
            t - self.start_time
        ))

        self.out.write(u'>\n' if self.name else u'\n')

        self.last_time = time.time()


class CallTimer:
    """Таймер измерения времени выполнения какой-либо функции и подсчета
    количества вызовов этой функции.
    """
    def __init__(self, name=None, out=sys.stdout):
        self.name = name
        self.work_time = 0
        self.call_count = 0
        self.out = out

    def __call__(self, func, *args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        self.work_time += time.time() - start_time
        self.call_count += 1
        return result

    def print_info(self, label=None):
        if self.name:
            self.out.write(u'<%s ' % self.name)

        self.out.write(
            u'[%s: %.3f seconds, %d calls]' % (
                label or unicode(self.print_count),
                self.work_time,
                self.call_count
            )
        )

        self.out.write(u'>\n' if self.name else u'\n')
