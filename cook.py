#! /usr/bin/env python

#
#  cook.py
#
#  Main file for the utility
#

from cmd2 import Cmd, make_option, options, Cmd2TestCase
from ofoam.cmdUtils import query_yn, chooseFromDictionary, askForFloat,\
    setupFromOptions

import ofoam
from ofoam.exceptions import IncompleteData

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
            
    def do_setup(self, arg, opts=None):
        '''Setup main solver and all other necessary files'''
        try:
            self.problem.loadBoundaries()
            self.problem.solver = chooseFromDictionary('Choose solver:', ofoam.solvers)()
            ## @todo Now only RAS model
            self.problem.raspFile = ofoam.rasproperties.cmdSetup()
            self.problem.turbulentModel = self.problem.raspFile.data[0][1]['RASModel']
            
            self.problem.variables = self.problem.solver.getDefaultVariables(self.problem.turbulentModel)
            
            linSolver = None
            for v in self.problem.variables:
                if linSolver != None and query_yn('Use previous solver for ' + v.name):
                    v.solver = linSolver
                else:
                    linSolver = ofoam.linSolvers.cmdSetup(v.name)
                    v.solver = linSolver
                
                v.relaxFactor = askForFloat('Set relax factor ', v.relaxFactor)
                v.resControl = askForFloat('Set residual control ', v.resControl)
            
            self.problem.nlSolverConf = setupFromOptions(ofoam.nLinSolvers.Options.options[self.problem.solver.nlSolver])
            
            self.problem.saveFvSolution()
            
        except IncompleteData as e:
            print e
        
    
    def do_ask(self, arg):
        query_yn('Do you like it?')

shell = CookCmd()
shell.cmdloop()
