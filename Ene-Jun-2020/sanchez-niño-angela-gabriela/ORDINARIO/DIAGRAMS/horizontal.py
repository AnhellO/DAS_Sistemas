from diagrams import Diagram
from diagrams import Cluster, Diagram
from diagrams.aws.network import ELB
from diagrams.aws.compute import ECS
from diagrams.onprem.database import PostgreSQL
from diagrams.aws.database import Aurora

with Diagram("DIAGRAMA : ARQUITECTURA HORIZONTAL", show=False):
    lb = ELB("API/CONETENEDOR C")
    with Cluster("Database "):
        master = PostgreSQL("CONTENEDOR A")
        data = Aurora("DATABASE")
        lb >> master>> data
    with Cluster("Service"):
        svc_pgadmin = ECS("PGADMIN/CONTENEDOR B")
        data>>svc_pgadmin
    with Cluster("Services"):
        svc_flask = ECS("FLASK/CONTENEDOR D")
        svc_redis = ECS("REDIS/CONTENEDOR E")
        master >> svc_flask
        master >> svc_redis
        

       




