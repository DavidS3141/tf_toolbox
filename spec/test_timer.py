from ..timer import Timer

from time import sleep


def fsleep(t):
    sleep(0.01 * t)


def test_timer():
    timer = Timer()
    timer.start('a')
    fsleep(1)
    timer.start('b')
    fsleep(1)
    timer.start('c')
    fsleep(1)
    timer.stop('c')
    fsleep(1)
    timer.start('d')
    fsleep(1)
    timer.stop('d')
    fsleep(1)
    timer.start('c')
    fsleep(1)
    timer.stop('c')
    timer.start('e')
    fsleep(1)
    timer.stop('e')
    timer.stop('b')
    timer.start('c')
    fsleep(3)
    timer.stop('c')
    timer.stop('a')
    timer.start('b')
    fsleep(3)
    timer.stop('b')
    fsleep(3)
    timer.start('a')
    fsleep(2)
    timer.stop('a')
    timer.start('c')
    fsleep(2)
    timer.stop('c')
    timer.start('a')
    timer.start('d')
    fsleep(3)
    timer.stop_all()
    assert len(timer.get_current_timer()) == 0
    timer.create_plot('data/test_timer')
