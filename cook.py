#! /usr/bin/env python

#
#  cook.py
#
#  Main file for the utility
#

import cmd

class CookCmd(cmd.Cmd):
    intro = '\nWelcome to the oFoamCook console! Type help or ? to list commands \n'
    prompt = '(cook) '

    def do_help(self, arg):
        'Displays this help'
        cmd.Cmd.do_help(self,arg)

    def do_exit(self, arg):
        'Exits the program'
        return -1

    def precmd(self, line):
        line = line.lower() 
        return line

import bounds

shell = CookCmd()

shell.cmdloop()
