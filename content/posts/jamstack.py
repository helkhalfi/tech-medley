from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.compute import Server

from diagrams.onprem.client import Client
from diagrams.oci.connectivity import CDN
from diagrams.custom import Custom
with Diagram("JAM Stack", show=True, direction="TB"):
    client = Client("client")
    with Cluster("Microservices") as ms:
        services = [
            Server("Service A"),
            Server("Service B"),
        ]

    with Cluster("CDN"):
        cdn = CDN("")

    client >> Edge() << services
    client >> Edge() << cdn
