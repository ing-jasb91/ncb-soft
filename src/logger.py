import logging
from logging.config import fileConfig
from os import path, makedirs

class Logger :
    """
    Logger class for logging several and save in file with format
    A .cfg file is an initialization file
    """
    def __init__(self, logConfig) :
        """
        :param logConfig: point to the .cfg configuration file to read the parameters
        """
        self.logConfig = logConfig

    def logConfigFile(self) :
        fileConfig(self.logConfig)

        return logging.getLogger()
        
    def log_error(self, msg) :
        logSev = self.logConfigFile()
        logSev.error(msg)

    def log_warning(self, msg) :
        logSev = self.logConfigFile()
        logSev.warning(msg)

    def log_info(self, msg):
        logSev = self.logConfigFile()
        logSev.info(msg)

    def log_debug(self, msg):
        logSev = self.logConfigFile()
        logSev.debug(msg)
    
# logNCB = Logger('.cfg/logging.cfg')

# logNCB.log_info('Different')

# logError = Logger('.cfg/error.cfg')

# logError.log_error('This is a message error')
# logError.log_info('Try info on error')

