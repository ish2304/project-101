import time 
seconds = input("Enter the number of seconds: ")
def countDown_timer(seconds):
    while seconds>0:
        mins = int(seconds/60)
        secs = int(seconds%60)
        timer = f'{mins}:{secs}'
        print(timer)
        seconds = seconds-1
    print("time is up")
countDown_timer(int(seconds))