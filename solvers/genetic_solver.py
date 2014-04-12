import random
from .abstract import BasicSolver
from clint.textui import progress


class Darwin(BasicSolver):

    """a modification of RandomWalkWithRandomRestartSolver"""

    RESTARTS = 100
    STEPS_PER_RESTART = 1000

    def mutate(self, solution):
        """Modify the solution by swapping two timeslots.

        Very simple because we don't have to check anything.
        """
        solutions = [solution.copy()]
        # k1 = self.get_most_missed_sessions(solution)[0][0]
        for k1, _ in self.get_most_missed_sessions(solution)[:5]:
        # k1 = random.choice(list(solution.keys()))
            for _ in range(5):
                k2 = k1
                while k2 == k1:
                    k2 = random.choice(list(solution.keys()))

                v1 = solution[k1]
                v2 = solution[k2]

                # print("swapping {k1} -> {k2} ({v1} -> {v2})".format(
                #    k1=k1, k2=k2, v1=v1, v2=v2
                #))
                new_solution = solution.copy()
                new_solution[k1] = v2
                new_solution[k2] = v1
                solutions.append(new_solution)

        return solutions

    def solve(self, args=None):
        if args is None:
            args = {}
        iterations = int(args.get('--iterations')) // 1000
        best_solutions = [self.get_random_solution() for _ in range(5)]
        best_solution = max(*best_solutions, key=self.get_rank)

        for i in progress.bar(range(iterations)):
            breed = []
            for solution in best_solutions:
                breed.extend(self.mutate(solution))

            best_solution = max(*best_solutions, key=self.get_rank)
            best_solutions = sorted(breed, key=self.get_rank, reverse=True)[:5]

        return best_solution
