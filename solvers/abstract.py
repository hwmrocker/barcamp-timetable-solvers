from collections import defaultdict
import random


class BasicSolver(object):
    """BasicSolver is a basic "abstract" like class, that defines the interface"""

    def __init__(self, cmp_func):
        self.get_rank = cmp_func

    def solve(self, sessions, rooms, timeslots, args=None):
        """solve(self, sessions, rooms, timeslots, args=None)

        sessions        is a dict where the keys are the session names and the
                        and the values are lists of the session host.
                        {"session1": ["host1", "host2"], "session2": ["host1"]}

        rooms           is a dict where the keys are unique room identifiers
                        and the values are dicts that still need to be defined.
                        {"room1": ..., "room2": ...}

        timeslots       is a dict where the keys are unique timeslot identifiers
                        and the values are dict that still need to be defined.
                        {"timeslot1": ..., "timeslot2": ...}

        desires         is a dict where the keys are unique names of guests
                        and the values are lists of sessions ordered by the
                        importance. The most important sessions appear first
                        (have a smaller index). The list contains only sessions
                        where the user is interested in.
                        {
                            "user1": [
                                "important session",
                                "less important session",
                                ...,
                                "least important session"
                            ],
                            "user2": ["important session"]
                        }

        returns a solution
                        a solution is a dict where the keys are session_names
                        and the values are tuples of timeslot_names and room_names
                        {"session1": ("timeslot1", "room2"),
                         "session2": ("timeslot2", "room2")}
        """
        raise NotImplemented("You need to implemt the solve function before you use it")

    def get_random_solution(self, sessions, rooms, timeslots):
        """get_random_solution(self, sessions, rooms, timeslots)

        Helper function that returns a random solution for a timetable.
        It is guaranteed that there are not two talks by the same person
        in the same timeslot. But it is not guaranteed that one person is
        able to present all of his talks.

        The parameters session, rooms, and timeslots should have the same
        internal structure like, those you get from the solve function.

        returns a solution
        """
        user_to_slot = defaultdict(set)
        booked = defaultdict(list)
        room_names = list(rooms.keys())
        session_names = list(sessions.keys())
        timeslot_names = list(timeslots.keys())
        solution = {}

        def get_random_timeslot_room_for_users(users):
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
                random.randrange(0, len(session_names))
            )
            users = sessions[session_name]
            try:
                solution[session_name] = get_random_timeslot_room_for_users(users)
            except IndexError:
                # we have more sessions than timeslots
                break
        return solution
