import sys
import time


class StepTimer:
    def __init__(self, name=None):
        self.name = name
        self.print_count = 0
        self.start_time = self.last_time = time.time()

    def print_info(self, label=None):
        t = time.time()
        self.print_count += 1
        if self.name:
            sys.stdout.write('[' + self.name + ']')
        print u'[%s: %.3fsec., %.3fsec.]' % (label or unicode(self.print_count),
                                            t - self.last_time,
                                            t - self.start_time)
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
