def main():
    # write your code here
    current_time = int(input("What is the current time "))
    alarm_time = int(input("What time would you like set for the alarm "))
    Time_until_alarm = (alarm_time - current_time)
    
    print("Your alarm will go off in", (Time_until_alarm), "hours")
    return

    
    return


if __name__ == '__main__':
    main()