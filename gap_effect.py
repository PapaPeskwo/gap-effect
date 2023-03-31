import random, time, winsound, os

break_duration = 10

def main_loop(study_duration):
    time.sleep(study_duration)
    winsound.Beep(1000, 500)
    os.system('cls' if os.name == 'nt' else 'clear') 
    print("Take a break (10 seconds).", flush=True)
    time.sleep(break_duration)
    winsound.Beep(1500, 500)
    os.system('cls' if os.name == 'nt' else 'clear') 
    print("Back to studying!", flush=True)

# Run the main loop
while True:
    # Generate a random duration between 2 and 4 minutes (inclusive)
    study_duration = random.randint(2, 4) * 60

    print(f"Study for {study_duration} seconds.") 
    time.sleep(study_duration)
    if study_duration > 0: 
        main_loop(study_duration)
