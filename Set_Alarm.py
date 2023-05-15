def set_alarm(employed, vacation):
    # The SetAlarm recieves 2 paramaters: Employed and Vaccation
    # Employed is when you are employed and true when you are in vaccation
    # The function should return true when you are employed and not on vacation otherwise it should return false
   
    return employed and not vacation






"""
Write a function named setAlarm which receives two parameters. The first parameter, employed, is true whenever you are employed and the second parameter, vacation is true whenever you are on vacation.

The function should return true if you are employed and not on vacation (because these are the circumstances under which you need to set an alarm). It should return false otherwise. Examples:

setAlarm(true, true) -> false
setAlarm(false, true) -> false
setAlarm(false, false) -> false
setAlarm(true, false) -> true

"""
