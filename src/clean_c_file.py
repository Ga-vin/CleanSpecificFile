# -*-coding: gb18030 -*-

import os
import sys
import logger

DELETE_LIST = [".c", ".o", ".cpp"]

def parseDirs(objs):
    if not objs:
        print '[X] Directory is not specific. System will terminate.'
        return None

    files_list = []    
    for roots, dirs, files in os.walk(objs):
        if (roots) and (not dirs) and (files):
            if "." in roots:
                continue
                
            if len(files) >= 1:
                for item in files:
                    files_list.append("%s\\%s" % (roots, item))

    return files_list

def rmCFiles(objs, log_file = None, options = None):
    '''
    If the file exists in files list(objs), it will be deleted from hard ware.
    When the file will be deleted before, yes or no will be asked to confirm.
    '''
    if not objs:
        print '[X] The files list is None.'

        return False

    counter = 0
    total = calcCOFile(objs)
    for item in objs:
        if ("readme" in item.lower()) or (getSuffix(item) in DELETE_LIST):
            if options:
                ask = raw_input('<%s> will be deleted. Are you sure? <Y/y to confirm> #' % os.path.abspath(item))
                if ("y" == ask) or ("Y" == ask):
                    counter += 1
                    if log_file:
                        try:
                            log_file.writeToFile("[D]: %s" % os.path.abspath(item))
                            displayProgress(counter, total)
                            os.unlink(os.path.abspath(item))
                        except AttributeError, e:
                            print '<rmCFiles>: ', e
                    else:
                        displayProgress(counter, total)
                        os.unlink(os.path.abspath(item))
            else:
                counter += 1
                if log_file:
                    try:
                        log_file.writeToFile("[D]: %s" % os.path.abspath(item))
                        displayProgress(counter, total)
                        os.unlink(os.path.abspath(item))
                    except AttributeError, e:
                        print '<rmCFiles> : ', e
                    except WindowsError, e:
                        print '<rmCFiles> : ', e
                else:
                    displayProgress(counter, total)
                    os.unlink(os.path.abspath(item))

    return counter

def calcCOFile(objs):
    total = 0
    
    for item in objs:
        if (item[-2:] in DELETE_LIST) or ("readme" in item.lower()):
            total += 1

    return total

def getSuffix(obj):
    '''
    Return the suffix of specific file
    '''
    try:
        if not obj:
            return None

        return obj[obj.index('.') : ]
    except ValueError, e:
        print obj
        print '<getSuffix> : ', e

def displayProgress(left, total):
    '''
    Display percentage of total with numeric format.
    '''
    try:
        print '%d%%\b' % int((float(left) / float(total)) * 100.0)
    except ZeroDivisionError, e:
        print e
    except ValueError, e:
        print e
    

def main():
    argv = sys.argv
    if len(argv) < 2:
        print '[^~^] Usage FileName <dir1> <dir2>...\n\n'
        sys.exit(-1)

    if not os.path.isdir(argv[1]):
        print '[^~^] Argument is not a directory. System will terminate...\n\n'

        sys.exit(-2)

    dir_list = []
    log_file = logger.Logger("logger.txt")
    var = parseDirs(argv[1])
    if not var:
        print '[X] There is no one file in specific directory<%s>.' % argv[1]
        sys.exit(-1)

    print var
    counter = rmCFiles(var, log_file)
    print 'Total %d files has been deleted' % counter

if __name__ == "__main__":
    main()
