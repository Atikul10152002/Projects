import sys
import time 

def prg(current, total):
    _len = 50
    filled = round(_len*current/total)
    bar = "=" * filled + "-" * (int( _len - filled)-1)
    sys.stdout.write(f"[{bar}]\r")
    sys.stdout.flush()





