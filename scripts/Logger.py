#!/usr/bin/env python3
import datetime
import os
from termcolor import colored
from configparser import ConfigParser

os.chdir("..")
filePath = os.getcwd()

#config
config = ConfigParser()
config.read(filePath + '/config/Logger_config.ini')
enable_console_log = config.getboolean("Logger","enable_console_log")
enable_file_log = config.getboolean("Logger","enable_file_log")
set_log_level = config.getint("Logger","set_log_level")
File_Size_in_MB = config.getint("Logger","File_Size_in_MB")
File_prefix_name = config.get("Logger","File_prefix_name")

class Logger:
  """
  Logger module defines a logger class that can be used for logging information in a Python program. It supports writing logs to a file and displaying logs on the console. The logger class is implemented as a singleton class.

  Usage:
      The logger is initialized when the first instance of the class is created, and subsequent instances are not allowed. To get an instance of the logger class, use the `get_instance` method.

      To write logs to a file, set the `enable_file_log` parameter in the configuration file to `True`. The logs will be written to a file named `prefix_timestamp_count.log` in the `logs` directory. The `prefix` and `File_prefix_name` parameters can be set in the configuration file.

      To display logs on the console, set the `enable_console_log` parameter in the configuration file to `True`. The logs will be displayed with color-coded text, depending on the log level.

      The log level can be set using the `set_log_level` parameter in the configuration file. The log levels are, in order of increasing severity: `DISABLE`, `ERROR`, `TRACE`, `DEBUG`, `INFO`, and `ENABLE`.

      The `File_Size_in_MB` parameter in the configuration file sets the maximum size of each log file in megabytes. When a log file reaches this size, a new file with a new count is created.

      The logger class provides several methods for logging information at different log levels:
          - `trace`: for tracing program execution
          - `error`: for logging errors
          - `info`: for logging information messages
          - `debug`: for debugging the program

      The log level can be changed dynamically using the `update_log_level` method.

  Example:
        from logger import Logger

        logger = Logger.get_instance()

        logger.trace("Entering function foo")
        
        logger.error("Error in function foo")
        
        logger.info("Function foo completed successfully")
        
        logger.debug("Variable x = ", x)

        logger.update_log_level(Logger.__disable_log_level) # disable logging
        logger.update_log_level(Logger.__enable_log_level) # enable logging

        logger.enable_all_logs() # enable all logs
        
        logger.disable_all_logs() # disable all logs
  """
  __disable_log_level = 1
  __error_log_level = 2
  __trace_log_level = 3
  __debug_log_level = 4
  __info_log_level = 5
  __enable_log_level = 6
  
  __instance__ = None
    
  def __init__(self):
    """
    Initializes a new instance of the Logger class.
    """
    self.__fileCount = 1
    self.__current_log_level = set_log_level
    self.__prefix = filePath + "/logs/" + File_prefix_name + "_"
    self.__middle = str(self.timeStamp()) + "__" 
    self.__suffix = ".log"
    self.__filename = self.__prefix + self.__middle + str(self.__fileCount) + self.__suffix
    self.__filenameBackup = self.__prefix + self.__middle
    if enable_file_log:
      self.__file = open(self.__filename, 'w')
      
    if Logger.__instance__ is None:
      Logger.__instance__ = self
    else:
      raise Exception("You cannot create another instance of looger Class")
    

  @staticmethod
  def get_instance():
    """
    Gets the singleton instance of the Logger class.

    :return:
        The Logger instance.
    :rtype: Logger
    """
    if not Logger.__instance__:
      Logger()
    return Logger.__instance__
  
  
  def __del__(self):
    """
    Closes the log file.
    """
    if enable_file_log:
        self.__file.close()
        
          
  def enable_all_logs(self):
    """
    Enables logging for all log levels.
    
    :return: None
    
    """
    self.__current_log_level = Logger.__enable_log_level
    
    
  def disable_all_logs(self):
    """
    Disables logging for all log levels.
    
    :return: None
    """
    self.__current_log_level = Logger.__disable_log_level
  
  
  def get_current_log_level(self):
    """
    Gets the current log level used for filtering messages.
    
    Returns
    -------
    int
        The current log level used for filtering messages.
    """
    return self.__current_log_level
  
  
  def update_log_level(self, log_level_number):
    """    
    Updates the current log level used for filtering messages.
    
    :param log_level_number: The new log level number
    :type: int   
    :return: None
    """
    self.__current_log_level = log_level_number
    
    
  def timeStamp(self):
    """
    Gets the current timestamp.
    
    :return: The current timestamp
    :rtype: datetime.datetime
    """
    ct = datetime.datetime.now()
    return ct

  def __consoleLog(self, data, color):
    """
    Logs messages to the console.
    
    Parameters
    ----------
    data : str
        The message to log.
    color : str
        The color to use for the log message.
    """
    if enable_console_log:
      print(colored(data, color))
      

  def __fileLog(self, data):
    """
    Writes the provided data to the log file.

    :param data: The data to write to the log file.
    :type data: str

    :return: None
    """
    if enable_file_log:
      self.__file.write(data)
      file_size = os.path.getsize(self.__filename)
      if file_size > File_Size_in_MB * 1000000:
        self.__file.close()
        self.__fileCount += 1
        self.__filename = self.__filenameBackup + str(self.__fileCount) + self.__suffix
        self.__file = open(self.__filename,'w')

  def trace(self, *argv):
    """
    Log trace information to the file and console.

    :param *argv: The trace information to log.
    :type *argv: str,int,bool,float
    :return: None
    """
    if self.__current_log_level >= Logger.__trace_log_level:
      trace_data = str(self.timeStamp()) + " " + "[TRACE]" + " "
      for arg in argv:
        trace_data = trace_data + str(arg) + " "
      trace_data += "\r"
      self.__fileLog(trace_data)
      self.__consoleLog(trace_data, "yellow")

  def error(self, *argv):
    """
    Log error information to the file and console.

    :param *argv: The error information to log.
    :type *argv: str,int,bool,float
    :return: None
    """
    if self.__current_log_level >= Logger.__error_log_level:
      error_data = str(self.timeStamp()) + " " + "[ERROR]" + " "
      for arg in argv:
        error_data = error_data + str(arg) + " "
      error_data += "\r"
      self.__fileLog(error_data)
      self.__consoleLog(error_data, "red")

  def info(self, *argv):
    """
    Log info information to the file and console.

    :param *argv: The info information to log.
    :type *argv: str,int,bool,float
    :return: None
    """
    if self.__current_log_level >= Logger.__info_log_level:
      info_data = str(self.timeStamp()) + " " + "[INFO]" + " "
      for arg in argv:
        info_data = info_data + str(arg) + " "
      info_data += "\r"
      self.__fileLog(info_data)
      self.__consoleLog(info_data, "green")

  def debug(self, *argv):
    """
    Log debug information to the file and console.

    :param *argv: The debug information to log.
    :type *argv: str,int,bool,float
    :return: None
    """
    if self.__current_log_level >= Logger.__debug_log_level:
      debug_data = str(self.timeStamp()) + " " + "[DEBUG]" + " "
      for arg in argv:
        debug_data = debug_data + str(arg) + " "
      debug_data += "\r"
      self.__fileLog(debug_data)
      self.__consoleLog(debug_data, "magenta")
           