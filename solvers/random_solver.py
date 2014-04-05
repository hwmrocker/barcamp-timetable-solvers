from . import BasicSolver
from collections import defaultdict
import random
from clint.textui import progress

class RandomSolver(BasicSolver):
    def getRandomSolution(self, sessions, rooms, timeslots):
        user_to_slot = defaultdict(set)
        booked = defaultdict(list)
        room_names = list(rooms.keys())
        session_names = list(sessions.keys())
        timeslot_names = list(timeslots.keys())
        solution = {}

        def getRandomTimeslotRoomForUsers(users):
            blocked_timeslots = set()
            for user in users:
                blocked_timeslots = blocked_timeslots.union(user_to_slot[user])
            slots_to_choose_from = list(set(timeslot_names) - blocked_timeslots)
            if not slots_to_choose_from:
                # This set of users cannot give a talk together
                # We don't want to stop the building process yet
                # so we just return None, None
                return None, None
            timeslot_name = random.choice(slots_to_choose_from)
            room_name = room_names[len(booked[timeslot_name])]
            booked[timeslot_name].append(room_name)
            if len(booked[timeslot_name]) == len(room_names):
                # clean up, we cannot use this time slot anylonger
                timeslot_names.remove(timeslot_name)
            return timeslot_name, room_name

        while session_names:
            session_name = session_names.pop(
                random.randrange(0,len(session_names))
            )
            users = sessions[session_name]
            try:
                solution[session_name] = getRandomTimeslotRoomForUsers(users)
            except IndexError as e:
                # we have more sessions than timeslots
                break
        return solution

    def solve(self, sessions, rooms, timeslots, args=None):
        if args is None:
            args = {}
        iterations = int(args.get('--iterations', 10000))
        best_solution = self.getRandomSolution(sessions, rooms, timeslots)
        for i in progress.bar(range(iterations)):
            solution = self.getRandomSolution(sessions, rooms, timeslots)
            best_solution = max(best_solution, solution, key=self.get_rank)
        return best_solution