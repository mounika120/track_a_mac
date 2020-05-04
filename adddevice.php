<?php
include('config.php');




$IpNumber = $_GET['ip'];
$PortNumber = $_GET['port'];
$CommunityNumber = $_GET['community'];
$VersionValue = $_GET['version'];

if(empty($IpNumber) || empty($PortNumber) || empty($CommunityNumber) || empty($VersionValue)) {
    echo "ERROR: valid Ipnumber,portnumber,communitynumber,verionvalue" ;   
}

else {

    $db->exec("INSERT INTO info (IP,PORT,COMMUNITY,VERSION) VALUES ('$IpNumber','$PortNumber','$CommunityNumber','$VersionValue')");
        echo "\n";
        echo "OK";
    
    }
$db->close();















?>