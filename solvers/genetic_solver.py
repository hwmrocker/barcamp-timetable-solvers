import random
from .abstract import BasicSolver


class Darwin(BasicSolver):
    """a genetic modified version of RandomWalkWithRandomRestartSolver"""

    INITIAL_BREED = 5
    NUMBER_OF_SOLUTIONS_TO_KEEP = 5
    NUMBER_OF_MUTATIONS = 5
    CHANGE_WORST = 5

    def mutate(self, solution):
        """Modify the solution by swapping two timeslots.

        Very simple because we don't have to check anything.
        """
        solutions = [solution.copy()]
        # k1 = self.get_most_missed_sessions(solution)[0][0]
        for k1, _ in self.get_most_missed_sessions(solution)[:self.CHANGE_WORST]:
        # k1 = random.choice(list(solution.keys()))
            for _ in range(self.NUMBER_OF_MUTATIONS):
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
        breed = [self.get_random_solution() for _ in range(self.INITIAL_BREED)]
        best_solutions = sorted(breed, key=self.get_rank,
            reverse=True)[:self.NUMBER_OF_SOLUTIONS_TO_KEEP]
        best_solution = max(*best_solutions, key=self.get_rank)

        # for i in progress.bar(range(iterations)):
        for i in range(iterations):
            breed = []
            for solution in best_solutions:
                breed.extend(self.mutate(solution))

            best_solutions = sorted(breed, key=self.get_rank,
                reverse=True)[:self.NUMBER_OF_SOLUTIONS_TO_KEEP]
            best_solution = max(*best_solutions, key=self.get_rank)
            yield best_solution

        # return best_solution


class Darwin1(Darwin):
    INITIAL_BREED = 100
    NUMBER_OF_SOLUTIONS_TO_KEEP = 5
    NUMBER_OF_MUTATIONS = 5
    CHANGE_WORST = 5


class Darwin2(Darwin):
    INITIAL_BREED = 50
    NUMBER_OF_SOLUTIONS_TO_KEEP = 5
    NUMBER_OF_MUTATIONS = 10
    CHANGE_WORST = 5


class Darwin3(Darwin):
    INITIAL_BREED = 50
    NUMBER_OF_SOLUTIONS_TO_KEEP = 5
    NUMBER_OF_MUTATIONS = 5
    CHANGE_WORST = 10


class Darwin4(Darwin):
    INITIAL_BREED = 150
    NUMBER_OF_SOLUTIONS_TO_KEEP = 15
    NUMBER_OF_MUTATIONS = 15
    CHANGE_WORST = 15


class Darwin5(Darwin):
    INITIAL_BREED = 150
    NUMBER_OF_SOLUTIONS_TO_KEEP = 15
    NUMBER_OF_MUTATIONS = 15
    CHANGE_WORST = 10
