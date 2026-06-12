def monitor():
    with open('system_log.txt', 'r') as file:
        status = file.read().strip()
        # If it's NOT "Everything is normal", it must be an error!
        if status != "Everything is normal":
            return True
        return False
