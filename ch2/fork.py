#!/usr/bin/python3
import os
import sys
ret = os.fork()
if ret == 0:
    print(f"子プロセス: pid = {os.getpid()}, 親プロセス: pid = {os.getppid()}")
    exit()
elif ret > 0:
    print(f"子プロセス: pid = {ret}, 親プロセス: pid = {os.getpid()}")
    exit()
sys.exit(1)
