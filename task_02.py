#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_02"""

import getpass
import authentication


def login(username, maxattempts=3):
    """Function takes two parameters.
    Arg:
       username(str): A string representing the username of the log in user.
       maxattempts(int, optional): Maximum number of promted attempts before the
       function returns False. Defaults to 3.
    Return:
       returns True or False depends on authentification.
    Examples:
       >>> import task_02
       >>> task_02.login('mike', 4)
       Please enter your password:
       Incorrect username or password. You have 3 attempts left.
       Please enter your password:
       Incorrect username or password. You have 2 attempts left.
       Please enter your password:
       Incorrect username or password. You have 1 attempts left.
       Please enter your password:
       Incorrect username or password. You have 0 attempts left.
       False
    """
    authenticated = False
    prompt = 'Please enter your password: '
    userinput = "Incorrect username or password. You have" ' {} '  "attempts"
    counter = 1
    while counter <= maxattempts:
        password = getpass.getpass(prompt)
        message = authentication.authenticate(username, password)
        if message:
            authenticated = True
            break
        else:
            print userinput.format(maxattempts - counter)
            counter += 1

    return authenticated
