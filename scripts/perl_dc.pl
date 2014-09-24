#!/usr/bin/perl
use v5.14;
use warnings;
use autodie;
use IO::Socket::INET;

my $remote_host="10.22.24.228";
my $remote_port="511";

my $socket=IO::Socket::INET->new(
			PeerAddr => $remote_host,
			PeerPort => $remote_port,
			Type	 => SOCK_STREAM,
			);

print $socket "Why?\r\n";

my $answer= <$socket> =~ s/\R\z//r;

say "Got answer: $answer";

close($socket);
