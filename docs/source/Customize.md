# Customize

Many things are customize through Logger_config.ini in config folder.


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