 #!/usr/bin/perl
use v5.14;
use warnings;
use autodie;
use IO::Socket::INET;
my $remote_host = "10.22.24.228";
 # replace with real remote host
my $remote_port = "511";
 # replace with service name or portnumber
my $socket = IO::Socket::INET–>new(
PeerAddr => $remote_host,
PeerPort => $remote_port,
Type => SOCK_STREAM,
);
# send something over the socket; netstuff likes CRLFs
# daytime doesn't take input, but use on other servers
print $socket "Why don't you call me anymore?\r\n";
# read the remote answer,
my $answer = <$socket> =~ s/\R\z//r;
say "Got answer: $answer";
# and terminate the connection when we're done.
close($socket);

