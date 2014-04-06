from .abstract import BasicSolver
from clint.textui import progress


class RandomSolver(BasicSolver):
    def solve(self, sessions, rooms, timeslots, args=None):
        if args is None:
            args = {}
        iterations = int(args.get('--iterations', 10000))
        best_solution = self.get_random_solution(sessions, rooms, timeslots)
        for i in progress.bar(range(iterations)):
            solution = self.get_random_solution(sessions, rooms, timeslots)
            best_solution = max(best_solution, solution, key=self.get_rank)
        return best_solution
