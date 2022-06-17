def print_servers(conn):
    print("Servers:")
    for server in conn.compute.servers():
        print server.items()
        print server['name']
        for p_address, p_info in server['addresses'].items():
                for pinfo in p_info:
                        print pinfo['OS-EXT-IPS-MAC:mac_addr'] + " " + pinfo['addr'] + " " + pinfo['OS-EXT-IPS:type']
        print " "

    



def print_networks(conn):
    print("Print Networks:")

    for network in conn.network.networks():
        print network['status']
        print network['subnet_ids']
        print network['id']
#        print network.items()
        print_ports_with(conn, network['id'])        
        print " "

def print_ports_with(conn, nid):
        for network in conn.network.ports():
                if (network['network_id']==nid):
                        print network['device_owner']
                        print network['network_id']
                        print network['fixed_ips']
                        print network['mac_address']
                        print_hosts_with(conn, network['mac_address'], network['fixed_ips'])
                
def print_hosts_with(conn, mac, subnet):
    for server in conn.compute.servers():
#        print server['name']
        for p_address, p_info in server['addresses'].items():
                for pinfo in p_info:
                        if (mac == pinfo['OS-EXT-IPS-MAC:mac_addr']):
                                print pinfo['OS-EXT-IPS-MAC:mac_addr'] + " " + pinfo['addr'] + " " + pinfo['OS-EXT-IPS:type']
                



def print_ports(conn):
    print("Print ports:")

    for network in conn.network.ports():
        print network['device_owner']
        print network['network_id']
        print network['fixed_ips']
        print network['mac_address']
   #     print network.items()
        print " "