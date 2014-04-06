from .random_solver import RandomSolver

_name_to_solver_dict = {
    "random": RandomSolver
}

def get_solver_by_name(name):
    return _name_to_solver_dict[name]