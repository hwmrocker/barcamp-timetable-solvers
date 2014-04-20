from .random_solver import RandomSolver
from .random_solver import RandomWalkWithRandomRestartSolver
from .random_solver import HillClimber
from .genetic_solver import Darwin
#, Darwin1, Darwin2, Darwin3, Darwin4, Darwin5

_name_to_solver_dict = {
    "random": RandomSolver,
    "rwrs": RandomWalkWithRandomRestartSolver,
    "hill": HillClimber,
    "darwin": Darwin,
    # "darwin1": Darwin1,
    # "darwin2": Darwin2,
    # "darwin3": Darwin3,
    # "darwin4": Darwin4,
    # "darwin5": Darwin5,
}


def get_solver_by_name(name):
    return _name_to_solver_dict[name]


def all_solver_names():
    return list(_name_to_solver_dict.keys())
