#coding: utf-8
import sys
import time


class StepTimer:
    """Интервальный таймер.

    Позволяет измерять время выполнения различных участков кода. Началом
    отсчета времени является момент создания экземпляра класса. При вызове
    метода print_info выводится сообщение с информацией о времени, прошедшем с
    момента предыдущего вызова метода print_info и с момента создания файла.
    """
    def __init__(self, name=None, out=sys.stdout):
        """
        :param str name: Имя таймера. Если указано, то выводится при каждом
            вызове print_info. Если не указано, то выводится порядковый номер
            вызова print_info.
        :param out: Поток, в который будут выводится сообщения. По умолчанию -
            sys.std.out.
        """
        self.name = name
        self.print_count = 0
        self.start_time = self.last_time = time.time()
        self.out = out

    def print_info(self, label=None):
        """Выводит в указанный поток (параметр out конструктора класса) текущие
        параметры таймера в следующем формате:
        <timer_name [1.234s. - step, 4.567s. - total]> или
        <print_number [1.234s. - step, 4.567s. - total]>, где 1.234s. - время,
        прошедшее с момента предыдущего вызова print_info, 4.567s. - время,
        прошедшее с момента создания таймера.
        """
        t = time.time()
        self.print_count += 1

        if self.name:
            self.out.write(u'<%s ' % self.name)
        else:
            self.out.write(u'<%d ' % self.print_count)

        self.out.write(u'[%s: %.3fs. - step, %.3fs. - total]' % (
            label or unicode(self.print_count),
            t - self.last_time,
            t - self.start_time
        ))

        if self.name:
            self.out.write(u'>')

        self.last_time = time.time()


class CallTimer:
    def __init__(self, name=None):
        self.name = name
        self.work_time = 0
        self.call_count = 0

    def __call__(self, func, *args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        self.work_time += time.time() - start_time
        self.call_count += 1
        return result

    def print_info(self, label=None):
        if self.name:
            sys.stdout.write(u'<%s ' % self.name)

        if label:
            sys.stdout.write(
                u'[%s: %.3f seconds, %d calls]' % (
                    label,
                    self.work_time,
                    self.call_count
                )
            )
        else:
            sys.stdout.write(
                u'[%.3f seconds, %d calls]' % (self.work_time, self.call_count)
            )

        if self.name:
            sys.stdout.write(u'>')

        sys.stdout.write(u'\n')
