import sys
from ofoam.exceptions import IncompleteData

## Implementation of Y/N prompt on commandline
## @return boolean
def query_yn(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.
    
    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is one of "yes" or "no".
    """
    valid = {"yes":True, "y":True, "ye":True,
             "no":False, "n":False}
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while 1:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return default
        elif choice in valid.keys():
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "\
                             "(or 'y' or 'n').\n")
 
def editDictionary(name, dictionary):
    
    while 1:
        print '   ' + name + '\n----------------------'
        for  (i, pair) in enumerate(dictionary.items()):
            print str(i) + ": " + pair[0] + " = " + pair[1]
        
        sys.stdout.write('\nChoose field to edit (q - quit) : ')
        key = ''
        try:
            choice = raw_input().lower()
            if choice.strip() == 'q':
                break
        
            key = dictionary.keys()[int(choice)]
        except:
            print '\n Illegal choice !!! \n'
            continue
        
        sys.stdout.write('\n ' + key + ' = ')
        value = raw_input()
        dictionary[key] = value;
        
def chooseFromDictionary(question, dictionary):
    sys.stdout.write('\n')
    key = None
    while 1:
        for  (i, key) in enumerate(dictionary.keys()):
            print str(i) + ": " + key
        
        
        try:
            sys.stdout.write(question)
            choice = raw_input().lower()
            if choice.strip() == 'q':
                raise IncompleteData('No option selected! (question: ' + question + ')')
                break
        
            key = dictionary.keys()[int(choice)]
            break
        except IncompleteData as e:
            raise e
        except:
            print '\n Illegal choice !!! \n'
            continue
    
    return dictionary[key]

def chooseFromList(question, l):
    sys.stdout.write('\n')
    while 1:
        for  (i, key) in enumerate(l):
            print str(i) + ": " + key
        
        key = ''
        try:
            sys.stdout.write(question)
            choice = raw_input().lower()
            if choice.strip() == 'q':
                raise IncompleteData('No option selected! (question: ' + question + ')')
                break
        
            key = l[int(choice)]
            break
        except IncompleteData as e:
            raise e
        except:
            print '\n Illegal choice !!! \n'
            continue
    return key
        
def askForFloat(question, default):
    choice = default

    try :
        sys.stdout.write(question + "[" +str(default) + "]")
        choice = float(raw_input())
        
    except:
        print 'Choosing default value \n'
            
    return choice

def setupFromOptions(options):
    result = {}
    for (option, values) in options.items():
        if isinstance(values, list):
            result[option] = chooseFromList('Choose ' + option + ' : ', values)
        if isinstance(values, float):
            result[option] = askForFloat('Set ' + option + ' : ', values)
    
    return result
        
