from cassandra.cluster import Cluster
from cassandra import ConsistencyLevel
from cassandra.query import SimpleStatement

cluster = Cluster()
connection = cluster.connect('testing')

drop = 'drop.cql'
create = 'create.cql'
work = 'work.cql'

with open(drop, mode='r') as file:
    txt = file.read()
    code = txt.split(';')
    for i in code:
        cod = i.strip()
        if cod != '':
            print(f'Executing {cod}')
            query = SimpleStatement(cod, consistency_level=ConsistencyLevel.QUORUM)
            connection.execute(query)
            print(f'{cod} - done')

with open(create, mode='r') as file:
    txt = file.read()
    code = txt.split(';')
    for i in code:
        cod = i.strip()
        if cod != '':
            print(f'Executing {cod}')
            query = SimpleStatement(cod, consistency_level=ConsistencyLevel.ALL)
            connection.execute(query)
            print(f'{cod} - done')

with open(work, mode='r') as file:
    txt = file.read()
    code = txt.split(';')
    for i in code:
        cod = i.strip()
        if cod != '':
            print(f'Executing {cod}')
            query = SimpleStatement(cod, consistency_level=ConsistencyLevel.ONE)
            connection.execute(query)
            print(f'{cod} - done')