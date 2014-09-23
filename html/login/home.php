<!DOCTYPE html>
<head>
	<title>Home</title>
	<meta name=viewport content="width=device-width, initial-scale=1">
	<link rel="stylesheet" type="text/css" href="theme.css">
	<?php
	session_start();
	if(isset($_SESSION['username']))$username=$_SESSION["username"];
	else header("Location:index.php");
	echo "Welcome ".$username."!";
	?> 	 
</head>
<body>
<a href="logout.php">Logout</a>
</body>	
