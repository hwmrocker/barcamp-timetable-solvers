from .random_solver import RandomSolver
from .random_solver import RandomWalkWithRandomRestartSolver

_name_to_solver_dict = {
    "random": RandomSolver,
    "rwrs": RandomWalkWithRandomRestartSolver,
}


def get_solver_by_name(name):
    return _name_to_solver_dict[name]

def all_solver_names():
    return _name_to_solver_dict.keys()