#! /usr/bin/env python
import threading
from atexit import register
from random import randrange
from threading import Thread, Lock, currentThread
from time import sleep, ctime


class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)


lock = Lock()
loops = (randrange(2, 5) for x in range(randrange(3, 7)))
# print(list(loops))
remaining = CleanOutputSet()


def loop(nsec):
    myname = currentThread().name
    lock.acquire()
    remaining.add(myname)
    print('[%s] Started %s' % (ctime(), myname))
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(myname)
    print('[%s] Completed %s (%s secs)' % (ctime(), myname, nsec))
    print('    (remaining: %s )' % (remaining or "NONE"))
    lock.release()


def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()
        print(threading.enumerate())


@register
def _atexit():
    print('all DONE at:', ctime())


if __name__ == '__main__':
    _main()
