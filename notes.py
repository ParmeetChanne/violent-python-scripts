# Sockets

"""
socket.gethostbyname(hostname) – This function takes a hostname such
as www.syngress.com and returns an IPv4 address format such as
69.163.177.2.

socket.gethostbyaddr(ip address) – This function takes an IPv4 address
and returns a triple containing the hostname, alternative list of
host names, and a list of IPv4/v6 addresses for the same interface
on the host.

socket.socket([family[, type[, proto]]]) – This function creates an
instance of a new socket given the family. Options for the socket
family are AF_INET, AF_INET6, or AF_UNIX. Additionally, the socket
can be specified as SOCK_STREAM for a TCP socket or SOCK_DGRAM for
a UDP socket. Finally, the protocol number is usually zero and is
omitted in most cases.

socket.create_connection(address[, timeout[, source_address]]) – This
function takes a 2-tuple (host, port) and returns an instance of a
network socket. Additionally, it has the option of taking a timeout
and source address.
"""

# Optparse

"""
In our first step, we accept the hostname and port from the user. For this, our
program utilizes the optparse library for parsing command-line options. The
call to optparse. OptionPaser([usage message]) creates an instance of an option
parser. Next, parser.add_option specifies the individual command line options for our script. The following example shows a quick method for parsing the
target hostname and port to scan.
"""

# Threading

"""
Depending on the timeout variable for a socket, a scan of each socket can take
several seconds. While this appears trivial, it quickly adds up if we are scanning
multiple hosts or ports. Ideally, we would like to scan sockets simultaneously
as opposed to sequentially. Enter Python threading. Threading provides a way
to perform these kinds of executions simultaneously. To utilize this in our
scan, we will modify the iteration loop in our portScan() function
"""

# Semaphore

"""
In order to allow a function to have complete control of the
screen, we will use a semaphore. A simple semaphore provides us a lock to prevent
other threads from proceeding. Notice that prior to printing an output, we
grabbed a hold of the lock using screenLock.acquire(). If open, the semaphore
will grant us access to proceed and we will print to the screen. If locked, we will
have to wait until the thread holding the semaphore releases the lock. By utilizing
this semaphore, we now ensure only one thread can print to the screen at
any given point in time
"""

# wigle.net

"""
A remaining database and open-source project, wigle.net, continues to allow
users to search for physical locations from an access point address. After registering
for an account, a user can interact with wigle.net with a little creative
Python scripting. Let us quickly examine how to build a script to interact with
wigle.net.
"""
# MAC address

"""
Let’s setup our sniffer for the MAC address of the wireless radio. Notice that we
are filtering for only MAC addresses that contain a specific set of three bytes for
the first three octets of the MAC address. The first three bytes serve as the Organizational
Unique Identifier (OUI), which specifies the device manufacturer.
You can further investigate this using the OUI database at http://standards.ieee.
org/cgi-bin/ouisearch.For this specific example, we will use the OUI d0:23:db
(the OUI for the Apple iPhone 4S product). If you search the OUI database,
you can confirm that devices with those 3 bytes belong to Apple.
"""
