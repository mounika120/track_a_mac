
#!/bin/bash

php -S "localhost:3000" &
curl "localhost:3000/config.php"

#curl "localhost:3000/addDevice.php?ip=192.168.0.106&port=1024&community=public&version=2"
curl "localhost:3000/addDevice.php?ip=192.168.0.106&port=1024&community=device_192_168_184_21&version=2"
curl "localhost:3000/addDevice.php?ip=192.168.0.106&port=1024&community=device_192_168_184_39&version=2"
curl "localhost:3000/addDevice.php?ip=192.168.0.106&port=10246&community=device_192_168_184_98&version=2"
curl "localhost:3000/addDevice.php?ip=192.168.0.106&port=1024&community=device_192_168_184_23&version=2"
curl "localhost:3000/addDevice.php?ip=192.168.0.106&port=1024&community=device_192_168_184_40&version=2"
curl "localhost:3000/addDevice.php?ip=192.168.0.106&port=1024&community=device_192_168_184_38&version=2"
curl "localhost:3000/addDevice.php?ip=192.168.0.106&port=1024&community=device_192_168_184_23&version=2"
curl "localhost:3000/addDevice.php?ip=192.168.0.106&port=1024&community=device_192_168_184_21&version=2"
