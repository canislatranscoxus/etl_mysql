'''
description: here we have a time to monitor the time of our process.

links:
    https://realpython.com/python-timer/
'''

import time


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer:

    def __init__(self):
        self._start_time = None


    def start(self):
        """Start a new timer"""

        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()


    def stop(self):
        """Stop the timer, and report the elapsed time"""

        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")


        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")

        hours  , rem     = divmod( elapsed_time, 3600 )
        minutes, seconds = divmod(rem, 60)
        print("{:0>2} h :{:0>2} m : {:05.2f} s".format(int(hours),int(minutes), seconds ))

        return elapsed_time