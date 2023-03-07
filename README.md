# Python-Logger
When developing a software application, it is essential to have a logging mechanism in place that records information about the application's behavior. Logging provides valuable insights into the performance and behavior of an application, and it is a necessary tool for debugging and troubleshooting issues.

This Python logging module provides a robust and flexible framework for logging messages from a Python application. The module provides various classes and methods that allow you to customize logging behavior, such as formatting log messages, filtering log records based on their severity, and routing log messages to different handlers.

This Python Logger designed to be as simple to use and easy to customize.

## Suported platforms:
#### Developements and tests are done under the following OSs :
- Ubuntu 14.04, 16.04, 18.04 and 20.04
- Windows 10
- Linux, FreeBSD, OpenBSD, Solaris, AIX
- macOS 

## Features:- 
- Simple Integration.
- Designed by using ***singleton design pattern*** for easy to use.
- Easily Customizable and Flexible. 
- Custom formatting.  
- Rollover Mechanism, Uses can defined the file size, after which the new file generated with same name with +1 count number.
- Console logging (colors supported) and File logging with human readble timestamp.
- Log filtering - log levels can be modified in runtime as well as in compile time.
- Very Fast, Small and Simple Logger.


## Install

``$ git clone https://github.com/shivangvijay/Python-Logger.git `` <br />


```{warning}
Under Development to convert this Module as Library
```

# Usage

Step 1: – Add import Logger <br />
Step 2:- Use it. 

<!-- ![alt text](https://github.com/shivangv6/Logger/blob/main/images/Example.png?raw=true)

Output:- 

![alt text](https://github.com/shivangv6/Logger/blob/main/images/output_example.png?raw=true) -->

Refer examples.py to explore more way to use.

## Customize

Many things are customize through Logger_config.ini in config folder.

<!-- ![alt text](https://github.com/shivangv6/Logger/blob/main/images/config.png?raw=true) -->

1. enable_console_log (bool) :- If required make true, otherwise false
2. enable_file_log (bool) :-  If required make true, otherwise false
3. File_Size_in_MB (int) :- After which the new file generated with same name with +1 count number (Rollover Mechanism).
4. File_prefix_name (str) :- Prefix of File name.
5. set_log_level (int):- ranges [1-6] Refer below for the mapping of log level and the number
    - disable_log_level = 1
    - error_log_level = 2
    - trace_log_level = 3
    - debug_log_level = 4
    - info_log_level = 5
    - enable_log_level = 6
  
Currently I added only 4 levels (ERROR, TRACE, DEBUG, INFO) but other levels or severity can be added easily. 

# Contribution

## GitHub

Please fill bug reports and feature requests here: https://github.com/shivangvijay/Python-Logger/issues <br />
Fork the repository, make some changes and submit them with pull-request 

## Contact
Email ID:- shivangvijay@gmail.com, I will answer any questions and requests.




