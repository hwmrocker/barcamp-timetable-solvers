
class BasicSolver(object):
    def __init__(self, cmp_func):
        self.get_rank = cmp_func

    def solve(self, sessions, rooms, timeslots, args=None):
        raise NotImplemented("You need to implemt the solve function before you use it")