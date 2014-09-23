<?php
if($_GET["logout"])
session_destroy();
setcookie("PHPSESSID","",0,"/");
header("Location:./")
?>
