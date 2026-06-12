from monitor import monitor
from heal import heal

if monitor():
    print("System failure detected!")
    heal()
else:
    print("System is running normally.")
