<?php

include('config.php');

$result = $db->query('SELECT * FROM List');

while($row = $result->fetchArray(SQLITE3_ASSOC) ) {
	echo  $row['IP']. "|" .$row['VLANs']. "|" .$row['PORT']. "|" .$row['MACS']. "\n";
}
$db->close();

?>
