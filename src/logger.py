# -*- coding: gb18030 -*-
## =================================================
## File name: logger.py
## =================================================
## Function : Logger the running details of program
##            in the process of whole project
## =================================================
## Author   : Gavin.Bai
## =================================================
## Time     : 2016.01.25
## =================================================
## Version  : (C) v1.0
## =================================================

import os
import time
import sys
import datetime

class FileNotReadyError(Exception):
    __information = ''
    def __init__(self, strp):
        self.__information = '<FileNotReadyError>: %s' % strp

    def getError(self):
        return self.__information

class DirNotExistError(Exception):
    __information = ''
    def __init__(self, strp):
        self.__information = '<DirNotExistError>: %s' % strp

    def getError(self):
        return self.__information

class Logger(object):
    '''
    The new class which is used to record the whole process of the program
    which is running
    '''
    def __init__(self, file_name = 'logger.txt', file_mode = 'a+'):
        self.__file_name    = file_name
        self.__file_mode    = file_mode
        self.__file_abspath = ''
        self.__file_obj     = None

        try:
            log_file_path = os.path.abspath('..') + '\\log'
            if not os.path.exists(log_file_path):
                raise DirNotExistError("<__init__> for logger")
            log_file_path += '\\' + self.__file_name
            self.__file_abspath = log_file_path
            self.__file_obj = open(self.__file_abspath, self.__file_mode)
            if self.__file_obj:
                self.__file_obj.write(str(datetime.datetime.today()) + '%4s' % ' ' + 'Open file successfully' + '\n')
        except IOError, e:
            print '[*] Open file fail: %s' % e
            sys.exit(0)

    def getFileName(self):
        '''
        Return the name of logger file
        '''
        return self.__file_name

    def setFileName(self, file_name):
        '''
        Set the name of logger file
        '''
        if (self.__file_name != file_name) and (self__file_name):
            if self.__file_obj:
                self.__file_obj.close()
                self.__file_abspath = ''
                self.__file_name    = file_name
                self.__file_abspath = os.path.abspath('..') + '\\log\\' + file_name
                self.__file_obj     = open(self.__file_file_abspath, self.getFileMode())
                if not self.__file_obj:
                    raise FileNotReadyError("setFileName fail")
            return True
        else:
            return False

    def getFileMode(self):
        '''
        Return the mode of the logger file
        '''
        return self.__file_mode

    def setFileMode(self, file_mode):
        '''
        Set the mode of the logger file
        '''
        if (self.__file_mode != file_mode) and (file_mode):
            self.__file_mode = file_mode

    def writeToFile(self, contents):
        '''
        Write contents to file which has been ready for
        '''
        if not self.__file_obj:
            raise FileNotReadyError("writetToFile not ready")
        self.__file_obj.write(str(datetime.datetime.today()) + '%4s' % ' ' + str(contents) + '\n')

    def closeFile(self):
        '''
        Close current opened file
        '''
        if not self.__file_obj:
            raise FileNotReadyError("closeFile not ready")
        self.__file_obj.write(str(datetime.datetime.today()) + '%4s' % ' ' + 'It will be closed' + '\n')
        self.__file_obj.close()

    def clearFile(self):
        '''
        Clean all contents of the file
        '''
        if not self.__file_obj:
            raise FileNotReadyError("clearFile not ready")
        self.__file_obj.truncate(0)
        self.__file_obj.flush()
        return True

def main():
    try:
        logger = Logger()
        logger.clearFile()
    except FileNotReadError, e:
        print e.getError()
    except DirNotExistError, e:
        print e.getError()
    logger.writeToFile("Hello WOrld")
    logger.closeFile()

if __name__ == "__main__":
    main()

    
