#! /usr/bin/env python

#
#  cook.py
#
#  Main file for the utility
#

from cmd2 import Cmd
from general.cmdUtils import query_yn

import ofoam

class CookCmd(Cmd):
    intro = '\nWelcome to the oFoamCook console! Type help or ? to list commands \n'
    prompt = '(cook) '
    
    problem = ofoam.Problem()
    
    def do_load(self, arg):
        'Loads all oopenFoam structures in the current directory'
        self.problem.loadBoundaries()
        if arg == 'v':
            print self.problem.boundaries
    
    def do_ask(self, arg):
        query_yn('Do you like it?')

shell = CookCmd()
shell.cmdloop()
