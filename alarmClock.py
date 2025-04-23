import time
import datetime
import pygame
import os

def validate_time_format(t):
    try:
        datetime.datetime.strptime(t, "%H:%M:%S")
        return True
    except ValueError:
        return False

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "Jammin Bread - Casa Rosa's Tulum Vibes.mp3"
    
    if not os.path.exists(sound_file):
        print(f"Sound file '{sound_file}' not found!")
        return

    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("\nTime to wake up!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running = False
        else:
            print(f"Current time: {current_time}", end="\r")
            time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time in (HH:MM:SS) format: ")
    while not validate_time_format(alarm_time):
        print("Invalid time format. Please use HH:MM:SS.")
        alarm_time = input("Enter the alarm time in (HH:MM:SS) format: ")

    set_alarm(alarm_time)
