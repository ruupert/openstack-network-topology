#!/usr/bin/python
import openstack
import os_graph


from graphviz import render
from graphviz import Graph


myProjects = [
        {'id': 'PROJECT X ID','name': 'PROJECT X NAME'}, 
        {'id': 'PROJECT Y ID','name': 'PROJECT Y NAME'}, 
        {'id': 'PROJECT Z ID','name': 'PROJECT Z NAME'}]


def get_connection(pid):
        conn = openstack.connection.Connection(
                region_name='',
                auth=dict(
                        auth_url='',
                        username='',
                        password='',
                        project_id=pid,
                        project_domain_name='',
                        user_domain_name=''),
                compute_api_version='2',
                identity_interface='internal')
        return conn




### This is for all
for proj in myProjects:
        print proj['name']
        fname = '{}.gv'.format(proj['name']).rstrip()
        g = Graph('G', filename=fname, engine='dot')
        conn = get_connection(proj['id'])
        hello_graph.add_networks(conn, g)
        g.render(filename=fname, directory='png', format='png')


