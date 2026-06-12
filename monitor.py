def monitor():
    with open('system_log.txt', 'r') as file:
        status = file.read().strip()
        if status == "ERROR":
            return True
        return False
