from monitor import monitor
from diagnose import diagnose
from heal import heal, log_activity # We import the logger here too

if monitor():
    with open('system_log.txt', 'r') as f:
        error_msg = f.read().strip()
    
    # Log the detection
    log_activity(f"ALERT: Failure detected - {error_msg}")
    
    # Diagnosis
    fix_plan = diagnose(error_msg)
    log_activity(f"DIAGNOSIS: AI suggested - {fix_plan}")
    
    # Healing
    heal(fix_plan)
else:
    # Optional: print("System is running normally.") 
    pass
