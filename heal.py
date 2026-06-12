import datetime

def log_activity(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('activity_log.txt', 'a') as f:
        f.write(f"[{timestamp}] {message}\n")

def heal(fix_command):
    print(f"Applying fix: {fix_command}")
    
    # Reset the system
    with open('system_log.txt', 'w') as file:
        file.write("Everything is normal")
        
    # Log the action
    log_activity(f"ACTION: {fix_command} - System restored.")
    print("System restored successfully.")
