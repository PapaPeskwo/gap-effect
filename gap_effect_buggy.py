import time
import random
import winsound

# Define the duration of a study session in seconds
study_duration = 12

# Define the duration of a break in seconds
break_duration = 10

# Define the number of breaks to take during a study session
num_breaks = study_duration // (2 * break_duration)

# Define the main loop
def main_loop():
    for i in range(num_breaks):
        # Wait for a random amount of time
        #delay = random.uniform(0.5, 1.5) * break_duration
        #time.sleep(delay)
        

        # Play a beep sound to signal a break
        winsound.Beep(1000, 500)

        # Wait for the break duration, printing the remaining time
        for remaining_time in range(break_duration, 0, -1):
            # Sometimes the print statement is not printed, so a flush statement is added
            print(f"Take a break ({remaining_time} seconds remaining).", flush=True)
            time.sleep(1)
            if remaining_time == 1:
                # Play a higher pitched and longer beep sound to signal the end of the break
                winsound.Beep(1500, 800)

# Run the main loop
while True:
    print(f"Study for {study_duration} seconds.")
    time.sleep(study_duration)
    main_loop()
