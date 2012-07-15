#! /usr/bin/env python

#
#  cook.py
#
#  Main file for the utility
#

from cmd2 import Cmd
from general.cmdUtils import query_yn

class CookCmd(Cmd):
    intro = '\nWelcome to the oFoamCook console! Type help or ? to list commands \n'
    prompt = '(cook) '
    
    def do_test(self, arg):
        query_yn('Do you like it?')

shell = CookCmd()
shell.cmdloop()
