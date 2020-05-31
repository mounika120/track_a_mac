# track_a_mac

The aim with this project is to create a solution that allows us to track where MAC numbers connect to our network.
This will be done by probing the network switches periodically, and retrieving their ForwardingTables.
Using the collected information, we want to have a solution that we can search for a specific MAC address. 
If a match is found,the response should return what switches,vlans and ports are aware of the MAC address, and identify what port is the connection port.
(If no VLAN is used, then use VLAN ID as 1) 
To detect the connection port, the MAC number should be the only MAC on that port.
