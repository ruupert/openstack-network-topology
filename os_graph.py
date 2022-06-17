def add_networks(conn, graph):

    for network in conn.network.networks():
#        print network['status']
#        print network['subnet_ids']
#        print network['id']
#        print network.items()
        add_ports_with(conn, network['id'], graph)        
#        print " "

def add_ports_withaa(conn, nid, graph):
        for network in conn.network.ports():
                if (network['network_id']==nid):
                    graph.edge(nid, network['mac_address'].replace(':','-'))
#                    print network['device_owner']
#                    print network['network_id']
#                    print network['fixed_ips']
#                    print network['mac_address']
                    add_hosts_with(conn, network['mac_address'], network['fixed_ips'], graph)

def add_ports_with(conn, nid, graph):
        for network in conn.network.ports():
                if (network['network_id']==nid):
#                    graph.edge(nid, network['mac_address'].replace(':','-'))
#                    print network['device_owner']
#                    print network['network_id']
#                    print network['fixed_ips']
#                    print network['mac_address']
                    add_hosts_with(conn, network['mac_address'], network['fixed_ips'], graph, nid)

def add_hosts_withaa(conn, mac, subnet, graph):
    for server in conn.compute.servers():
#        print server['name']
        for p_address, p_info in server['addresses'].items():
                for pinfo in p_info:
                        if (mac == pinfo['OS-EXT-IPS-MAC:mac_addr']):
                            graph.edge(mac.replace(':','-'), pinfo['addr'])
                            graph.edge(pinfo['addr'], server['name'])
#                           print pinfo['OS-EXT-IPS-MAC:mac_addr'] + " " + pinfo['addr'] + " " + pinfo['OS-EXT-IPS:type']


def add_hosts_with(conn, mac, subnet, graph, nid):
    for server in conn.compute.servers():
#        print server['name']
        for p_address, p_info in server['addresses'].items():
                for pinfo in p_info:
                        if (mac == pinfo['OS-EXT-IPS-MAC:mac_addr']):
                            graph.edge(nid, pinfo['addr'])
                            graph.edge(pinfo['addr'], server['name'])
#                           print pinfo['OS-EXT-IPS-MAC:mac_addr'] + " " + pinfo['addr'] + " " + pinfo['OS-EXT-IPS:type']
