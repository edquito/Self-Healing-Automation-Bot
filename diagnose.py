def diagnose(error_log):
    # This simulates an AI analysis
    # In a real scenario, you'd insert your OpenAI API call here
    print(f"AI Brain is analyzing: {error_log}...")
    
    if "connection" in error_log.lower():
        return "Restarting Database Service"
    elif "timeout" in error_log.lower():
        return "Flushing Cache and Refreshing Session"
    else:
        return "Running System Diagnostics"
