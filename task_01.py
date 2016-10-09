#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A list of versus matchups for players"""


def get_matches(players):
    """Function takes one arg - a list of players names.
    Arg:
       players(list): A list of player names.
    Return:
       returns the newly created list of tuples.
    Examples:
    >>> import task_01
    >>> task_01.get_matches(['Victor', 'Alex', 'John'])
    [('Victor', 'Alex'), ('Victor', 'John'), ('Alex', 'John')]
    """
    player = []
    for myind1, myitem1 in enumerate(players):
        for myind2, myitem2 in enumerate(players):
            if myind1 < myind2:
                list1 = (myitem1, myitem2)
                player.append(list1)

    return player
