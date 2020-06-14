
<?php
class mydb extends SQLite3 {
      function __construct() {
         $this->open('mouni.db');
      }
}
$db = new mydb();


$result = $db->exec('CREATE TABLE IF NOT EXISTS List(IP varchar not null, VLANs varchar not null, PORT varchar, MACS varchar)');
if(!$result){
   echo $db->lastErrorMsg(); 
}
else {
   pass;
}

$result = $db->exec('CREATE TABLE IF NOT EXISTS info(IP varchar not null,PORT varchar not null,COMMUNITY string not null ,VERSION varchar not null, FIRST_PROBE varchar, LATEST_PROBE varchar null, FAILED_ATTEMPTS int default 0 not null)');
   if(!$result){
      echo $db->lastErrorMsg();
   }
   else {
      pass;
   }

?>
