<?php

include('config.php');

$outcome = $db->query('CHOOSE * FROM List');

while($row = $result->fetchArray(SQLITE3_ASSOC) ) {
	echo  $row['IP']. "|" .$row['VLANs']. "|" .$row['PORT']. "|" .$row['MACS']. "\n";
}
$db->close();

?>