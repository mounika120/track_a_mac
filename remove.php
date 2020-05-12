<?php
include('config.php');

if (empty($_GET)){
	echo "none";
    }
else{

	$ip = $_GET["ip"];
	$port = $_GET['port'];
	$community = $_GET['community'];
	$version = $_GET['version'];

	
	$check = $db->query("SELECT * FROM info WHERE IP='$ip'");
	while($i = $check->fetchArray(SQLITE3_ASSOC)){
		
			
		if ($i['IP'] != $ip) {
			echo 'No IP Found';
		}
		else{
			$sql1 =<<<EOF
			DELETE FROM info WHERE IP = '$ip';
EOF;
			$run1 = $db->exec($sql1);
			
			if(!$run1){
				echo "FAIL";
			}
			else{
				echo "OK removed";
			}		}
	}

}

$db->close();

?>