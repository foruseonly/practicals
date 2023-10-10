<?php
$client=new SoapClient("http://localhost:8080/PracticalFirst/NewWebService?WSDL");
$t1=$client->operation1();
echo"time as string",$t1->return;
$t2=$client->operation2();
echo"time elapsed",$t2->return;
?>