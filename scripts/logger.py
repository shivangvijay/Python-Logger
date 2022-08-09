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

class Logger:
  __disable_log_level = 1
  __error_log_level = 2
  __trace_log_level = 3
  __debug_log_level = 4
  __info_log_level = 5
  __enable_log_level = 6
  
  __instance__ = None
    
  def __init__(self):
    self.__fileCount = 1
    self.__current_log_level = set_log_level
    self.__prefix = filePath + "/logs/Simulation" + "_"
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
    if not Logger.__instance__:
      Logger()
    return Logger.__instance__
  
  def __del__(self):
      if enable_file_log:
          self.__file.close()
          
  def enable_all_logs(self):
    self.__current_log_level = Logger.__enable_log_level
    
  def disable_all_logs(self):
    self.__current_log_level = Logger.__disable_log_level
  
  def get_current_log_level(self):
    return self.__current_log_level
  
  def update_log_level(self, log_level_number):
    self.__current_log_level = log_level_number
    
  def timeStamp(self):
    ct = datetime.datetime.now()
    return ct

  def __consoleLog(self, data, color):
    if enable_console_log:
      print(colored(data, color))

  def __fileLog(self, data):
      if enable_file_log:
        self.__file.write(data)
        file_size = os.path.getsize(self.__filename)
        if file_size > 15 * 1000000:
          self.__file.close()
          self.__fileCount += 1
          self.__filename = self.__filenameBackup + str(self.__fileCount) + self.__suffix
          self.__file = open(self.__filename,'w')

  def trace(self, *argv):
    if self.__current_log_level >= Logger.__trace_log_level:
      trace_data = str(self.timeStamp()) + " " + "[TRACE]" + " "
      for arg in argv:
        trace_data = trace_data + str(arg) + " "
      trace_data += "\r"
      self.__fileLog(trace_data)
      self.__consoleLog(trace_data, "yellow")

  def error(self, *argv):
    if self.__current_log_level >= Logger.__error_log_level:
      error_data = str(self.timeStamp()) + " " + "[ERROR]" + " "
      for arg in argv:
        error_data = error_data + str(arg) + " "
      error_data += "\r"
      self.__fileLog(error_data)
      self.__consoleLog(error_data, "red")

  def info(self, *argv):
    if self.__current_log_level >= Logger.__info_log_level:
      info_data = str(self.timeStamp()) + " " + "[INFO]" + " "
      for arg in argv:
        info_data = info_data + str(arg) + " "
      info_data += "\r"
      self.__fileLog(info_data)
      self.__consoleLog(info_data, "green")

  def debug(self, *argv):
    if self.__current_log_level >= Logger.__debug_log_level:
      debug_data = str(self.timeStamp()) + " " + "[DEBUG]" + " "
      for arg in argv:
        debug_data = debug_data + str(arg) + " "
      debug_data += "\r"
      self.__fileLog(debug_data)
      self.__consoleLog(debug_data, "magenta")
           