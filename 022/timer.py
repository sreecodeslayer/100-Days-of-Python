import time
import webbrowser

def choose_time():
    print("How long would you like to set the timer for?")
    p_time = input("Please enter a time in minutes: ")
    return float(p_time)

def timer(p_time):
    time.sleep((p_time * 60))   
    alarm()
    
def alarm():
    try:
        webbrowser.open("https://cdn4.iconfinder.com/data/icons/ios7-active-2/512/Alarm.png")
        print("\n******** TIME UP ********\n")
    except KeyboardInterrupt:
        return False
    
if __name__ == "__main__":
    while True:
        p_time = choose_time()
        timer(p_time)