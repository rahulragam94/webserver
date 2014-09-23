<?php $users=new mysqli("localhost","root","kundi","users"); ?>
<!DOCTYPE html>
<head>
	<title>Signup for grapher</title>
	<meta name=viewport content="width=device-width, initial-scale=1">
	<link rel="stylesheet" type="text/css" href="theme.css">
</head>
<body>
<form method="post" action="signup.php" id="signup_form">
<br>Username<input type="text" name="username">
<?php
if($_POST["submitted"]){
if($_POST["username"]){
$username=$_POST["username"];
$users->multi_query("SELECT * FROM credentials WHERE username='$username';");
$query=$users->store_result()->fetch_row();
if($query){
echo "Username already exists";
}
else $i=1;
}
else echo "*Please enter username*";
} 
?>
</br>
<br>Password<input type="password" name="password"><br/>
Confirm password<input type="password" name="confirm_password">
<?php
if($_POST["submitted"]){
if($_POST["password"]){
$password=$_POST["password"];
if($_POST["confirm_password"]){
if($_POST["confirm_password"]!==$_POST["password"])	
echo "*Passwords don't match*";
else $i=$i+1;
} else echo "*Please confirm password*";
} else echo "*Please enter password*";
}
?>
</br>
<br>Email<input type="text" name="email">
<?php
if($_POST["submitted"]){
if($_POST["email"]){
$email=$_POST["email"];
$users->multi_query("SELECT * FROM credentials WHERE email='$email';");
$query=$users->store_result()->fetch_row();
if($query){
echo "Email already exists";
}
else $i=$i+1;
}
else echo "*Please enter email*"; 
}
?>
</br>
<input type="hidden" value="1" name="submitted" />
<input type="submit" value="Signup"/>
</form>
<?php
if($i==3){
echo $i;
$users->multi_query("INSERT INTO credentials VALUES ('$username','$password','$email'); ");
header("Location:signupsuccess.php");
}
?>
<?php $users->close(); ?>
</body>

