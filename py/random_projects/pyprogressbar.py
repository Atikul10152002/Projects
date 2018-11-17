import sys
import time 

def progress(current : int , total:int=100, _len:int=50):
    """
    PRAM :: current, total, _len
        current <int> :: the current progress of the program
        total   <int> :: the total length of the program
        _len	<int> :: the length of the progress bar


    Example Code and Usage: :
    
    total = 100
    num = 0
    while 1:

        time.sleep(.05)
        progress(num, total,10)
        if num >= total:
            break
        num += 1

    """
    filled = round(_len*current/total)
    bar = "=" * filled + "-" * (int( _len - filled))
    sys.stdout.write(f"[{bar}]\r")
    sys.stdout.flush()

    if current == total:
        sys.stdout.write("\nDone!\r\n")
        sys.stdout.flush()

progress()

if __name__ == "__main__":
    """
    Example Code and Usage ::
    """
    total = 100
    num = 0
    while 1:

        time.sleep(.05)
        progress(num, total,10)
        if num >= total:
            break
        num += 1
        


