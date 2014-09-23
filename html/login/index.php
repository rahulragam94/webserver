<!DOCTYPE html>
<head>
	<title>Grapher Login </title>
	<link rel="stylesheet" type="text/css" href="theme.css">
	<meta name=viewport content="width=device-width, initial-scale=1">
</head>
<body>
	<form method="post" action="index.php" name="login_form" >
	<br>Username<input type="text" name="username"/></br>
	<br>Password<input type="password" name="password"/></br>
	<input type="hidden" value="1" name="submitted"/>
	<input type="submit" value="Login"/>
	</form>
	<a href="signup.php">Signup</a>
	<?php
	$username=$_POST["username"];
	$password=$_POST["password"];
	if($_POST["submitted"]){
		if($username&&$password){
			$users=new mysqli("localhost","root","kundi","users");
			$users->multi_query("SELECT * FROM credentials WHERE username='$username' AND password='$password';");																			
			$query=$users->store_result()->fetch_row();
			if($query){
				session_start();
				$_SESSION['username']=$username;
				header("Location:home.php");
				echo "Login Success";
			}
			else echo "Login failed";
			}
		}
	?>
		
</body>
