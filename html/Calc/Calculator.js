var current=0.0;
var operation="+";
function showNum(digit)
{
	display=document.getElementById("Calcdisplay");
	display.value=display.value+digit;
}
function addnum()
{
	displayUpdate();
	operation="+";
}
function multnum()
{
	displayUpdate();
	operation="*";
}
function divnum()
{
	displayUpdate();
	operation="/";
}
function subnum()
{
	displayUpdate();
	operation="-";
}
function equals()
{
	display=document.getElementById("Calcdisplay");
	if(display==null)
		document.write("error");
	else
		current=eval("current"+operation+display.value);
	display.value=current;
	current=0;
	operation="+";
}
function displayUpdate()
{	
	//document.write("1");
	display=document.getElementById("Calcdisplay");
	if(display==null)
		document.write("error");
	else
		current=eval("current"+operation+display.value);
	display.value=null;
}