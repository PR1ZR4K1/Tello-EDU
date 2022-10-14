This repository contains three functional programs for fliying drones.

Install the requirements:
```python
pip install -r requirements.txt  
```

If you want to use the interactive drone flying program run this.  
Within the Tello-EDU directory.


```python
python drone_interactive.py
```

For the tello swarming capabilities you need to connect all tellos and the device you are running the progam on to the same network in my case I used a TP-Link router.

Use swarm_config.py to either create a unique ssid for individual tello or connect tellos to a central router.

To run swarm flying program run. After, getting everything connected to a router and setting rescan=True to get a new list of drone_ips related to your instance.
```
python star_fleet.py
``` 

Finally, refer to https://djitellopy.readthedocs.io/en/latest/tello/ 

For syntax of the commands used to control the drones.