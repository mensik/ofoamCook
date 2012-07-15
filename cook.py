#! /usr/bin/env python

#
#  cook.py
#
#  Main file for the utility
#

from cmd2 import Cmd, make_option, options, Cmd2TestCase
from general.cmdUtils import query_yn

import ofoam

class CookCmd(Cmd):
    intro = '\nWelcome to the oFoamCook console! Type help or ? to list commands \n'
    prompt = '(cook) '
    
    problem = ofoam.Problem()
    
    @options([make_option('-v', '--verbose', action="store_true", help="verbose")])
    def do_load(self, arg, opts=None):
        '''Loads all oopenFoam structures in the current directory
        '''
        self.problem.loadBoundaries()
        if opts.verbose:
            print self.problem.boundaries
    
    def do_ask(self, arg):
        query_yn('Do you like it?')

shell = CookCmd()
shell.cmdloop()
