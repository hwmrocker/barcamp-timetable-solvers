# from .random_solver import RandomSolver
# from .random_solver import RandomWalkWithRandomRestartSolver
# from .random_solver import HillClimber
from .genetic_solver import Darwin

_name_to_solver_dict = {
    "random": RandomSolver,
    "rwrs": RandomWalkWithRandomRestartSolver,
    "hill": HillClimber,
    "darwin": Darwin,
}


def get_solver_by_name(name):
    return _name_to_solver_dict[name]


def all_solver_names():
    return list(_name_to_solver_dict.keys())
