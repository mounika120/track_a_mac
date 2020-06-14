# track_a_mac

The aim with this project is to create a solution that allows us to track where MAC numbers connect to our network.
This will be done by probing the network switches periodically, and retrieving their ForwardingTables.
Using the collected information, we want to have a solution that we can search for a specific MAC address. 
If a match is found,the response should return what switches,vlans and ports are aware of the MAC address, and identify what port is the connection port.
(If no VLAN is used, then use VLAN ID as 1) 
To detect the connection port, the MAC number should be the only MAC on that port.


-------------------------
#### Instructions to run the app using Docker
1. Install docker engine on machine
2. Execute `./docker-build-run.sh` to build and run docker image
    * This script will execute `docker build -t track-a-mac .` command to build a 
    new docker image from docker file and installs the required packages to run track-a-mac application
    * This script will run the built docker image from previous step using `docker run -it --rm --name track-a-mac -p 8000:8000 track-a-mac --add-host=docker:0.0.0.0`
3. Execute `./addDevices.sh` to initialize config.db and register sample ip's
    * More ips can be added using `curl "localhost:8000/addDevice.php?ip=127.0.0.1&port=1024&community=public&version=2"`
4. Running backend script:
    * `docker exec -it track-a-mac ./backend.py`
5. Running snmp simulator
    * `docker exec -it testuser@track-a-mac su testuser`
    * Execute snmpsim `snmpsim-command-responder --data-dir=./data --agent-udpv4-endpoint=127.0.0.1:1024`
    * testuser is created on the creation of container, so using test user to execute snmpsim-command-responder. testuser has to be created, 
    because of incapabilities of snmp to run as root.
6. Pulling the ubuntu installed packages
    * `docker exec track-a-mac dpkg --get-selections | grep install > myPackages`
7. Pulling python installed packaged
    * `docker exec track-a-mac pip list > pythonPkts`
