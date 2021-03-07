#!/usr/bin/python3.7

import re
def show_time_of_pid(line):
  # pattern = "(^[a-zA-Z\s]*)([\d\s]*)([\d\:]*)([^0-9]*)(\d*)(.*)" # use in re.sub()
  pattern = "(^[A-Za-z\s]{4})([\d\s]*)([\d\:]*)\D*(\d+)"
  result = re.search(pattern, line)
  #result = re.sub(pattern, "\\1\\2\\3 pid:\\5", line)
  return "{}{}{} pid:{}". format(result[1], result[2], result[3], result[4])

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440
