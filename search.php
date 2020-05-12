<?php
include_once('config.php');

if (empty($_GET)) {
    echo "It is False";
    }
else {
    $my_search_is = htmlspecialchars($_GET["mac"]);
    $sql = <<<EOF
              SELECT * FROM List WHERE MACS LIKE "%$my_search_is%" ORDER BY MACS;
EOF;
    $my_output_is = $db->query($sql);
    $data = array(); 
    while($row = $my_output_is->fetchArray(SQLITE3_ASSOC) ){
         #echo $row[1]. "|" . $row[2] . "|" . $row[3] . "|" . $row[4] . "\n";
         $data[] = $row['IP']. " | " . $row['VLANs'] . " | " . $row['PORT'] . " | " . "$my_search_is";
     
    }

$flag = count($data);
if($flag ==0){
    $count = $db->query('SELECT count(*) FROM info');
    while($check = $count->fetchArray(SQLITE3_ASSOC)) {
        $number_of_devices = $check['count(*)'];
        echo "wWe found no match in $number_of_devices devices"."\n";
     }
}

$my_result_is = array_unique($data);
$total = count($my_result_is);
$i=0;
while($i<$total){
    echo $my_result_is[$i]. "\n";
    $i++;
    }
}
$db->close();

?><?php
include_once('config.php');

if (empty($_GET)) {
    echo "It is False";
    }
else {
    $my_search_is = htmlspecialchars($_GET["mac"]);
    $sql = <<<EOF
              SELECT * FROM List WHERE MACS LIKE "%$my_search_is%" ORDER BY MACS;
EOF;
    $my_output_is = $db->query($sql);
    $data = array(); 
    while($row = $my_output_is->fetchArray(SQLITE3_ASSOC) ){
         #echo $row[1]. "|" . $row[2] . "|" . $row[3] . "|" . $row[4] . "\n";
         $data[] = $row['IP']. " | " . $row['VLANs'] . " | " . $row['PORT'] . " | " . "$my_search_is";
     
    }

$flag = count($data);
if($flag ==0){
    $count = $db->query('SELECT count(*) FROM info');
    while($check = $count->fetchArray(SQLITE3_ASSOC)) {
        $number_of_devices = $check['count(*)'];
        echo "No match was found in $number_of_devices devices"."\n";
     }
}

$my_outcome_is = array_unique($data);
$total = count($my_outcome_is);
$i=0;
while($i<$total){
    echo $my_outcome_is[$i]. "\n";
    $i++;
    }
}
$db->close();

?>