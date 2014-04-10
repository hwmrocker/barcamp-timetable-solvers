import random

from .abstract import BasicSolver
from clint.textui import progress


class RandomSolver(BasicSolver):
    def solve(self, sessions, rooms, timeslots, args=None):
        if args is None:
            args = {}
        iterations = int(args.get('--iterations', 100000))
        best_solution = self.get_random_solution(sessions, rooms, timeslots)
        for i in progress.bar(range(iterations)):
            solution = self.get_random_solution(sessions, rooms, timeslots)
            best_solution = max(best_solution, solution, key=self.get_rank)
        return best_solution


class RandomWalkWithRandomRestartSolver(BasicSolver):
    """Do a random walk with occasional random restart.
    
    Made by Johannes -- HAHA!
    """
    
    RESTARTS = 100
    STEPS_PER_RESTART = 1000
    
    def modify_swap(self, solution):
        """Modify the solution by swapping two timeslots.
        
        Very simple because we don't have to check anything.
        """
        
        k1 = random.choice(solution.keys())
        k2 = k1
        while k2 == k1:
            k2 = random.choice(solution.keys())
            
        v1 = solution[k1]
        v2 = solution[k2]


        #print("swapping {k1} -> {k2} ({v1} -> {v2})".format(
        #    k1=k1, k2=k2, v1=v1, v2=v2
        #))
        
        solution[k1] = v2
        solution[k2] = v1
        
        return solution
    
    
    methods = (modify_swap, )
    
    def modify(self, solution):
        """Do some small modification that can be good or not."""
        
        newsol = dict(solution)
        
        method = random.choice(self.methods)
        return method(self, newsol)
        
    
    def solve(self, sessions, rooms, timeslots, args=None):
        if args is None:
            args = {}
        iterations = int(args.get('--iterations')) / 100
        best_solution = self.get_random_solution(sessions, rooms, timeslots)
        for i in progress.bar(range(iterations)):
            solution = self.get_random_solution(sessions, rooms, timeslots)
            for j in xrange(self.STEPS_PER_RESTART):
                solution = self.modify(solution)
                best_solution = max(best_solution, solution, key=self.get_rank)
        return best_solution