
import pprint
def list_projects(conn):
    print("List Projects:")

    for project in conn.identity.projects():
        pprint.pprint(project)

def list_networks(conn):
    print("List Networks:")

    for network in conn.network.networks():
        pprint.pprint(network)
        print " "

def list_servers(conn):
    print("List Servers:")

    for server in conn.compute.servers():
        pprint.pprint(server) 
        print " "

def list_ports(conn):
    print("List Ports:")

    for network in conn.network.ports():
        pprint.pprint(network)
        print " "