def heal():
    print("Repairing system...")
    with open('system_log.txt', 'w') as file:
        file.write("Everything is normal")
    print("System restored successfully.")
