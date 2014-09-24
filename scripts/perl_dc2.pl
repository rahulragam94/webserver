use IO::Socket::INET;

# auto-flush on socket
$| = 1;

# create a connecting socket
my $socket = new IO::Socket::INET (
    PeerHost => '10.22.24.159',
    PeerPort => '511',
    Proto => 'tcp',
);
die "cannot connect to the server $!\n" unless $socket;
print "connected to the server\n";
$socket->recv($response, 1024);
print "received response: $response\n";
$response =~ m/\$Lock (.+) Pk/;
my $lock =$1;
my $key =$lock;
my $len=length($lock);
my $i=1;
$socket->send('$Supports UserCommand NoGetINFO NoHello UserIP2 QuickList ZPipe IP64 IPv4|');
$socket->recv($response, 1024);
print "received response: $response\n";
#=pod 
while($i<$len){
	substr($key,$i,1)=substr($lock,$i,1) ^ substr($lock,$i-1,1) ;
	$i++;
}
substr($key,0,1)=substr($lock,0,1) ^ substr($lock,$len-1,1) ^ substr($lock,$i-2,1) ^ 5;
$i=0;
while(i<$len){
	substr($key,$i,1)=((substr($key,$i,1)<<4)&240)|((substr($key,$i-1,1)>>4)&15) ;
	$i++;
} 
$socket->send('$COL<'.$key.'>|$ValidateNick <yoyoyolad>|');
$socket->recv($response, 1024);
print "received response: $response\n";
#=cut
$socket->send('$MyINFO $ALL PPK $ $Cable;$$0$|');
$socket->send('$GetNickList|');
$socket->recv($response, 1024);
print "received response: $response\n";
$socket->send('$GetINFO avj PPK|');
$socket->recv($response, 1024);
print "received response: $response\n";
$socket->close();
