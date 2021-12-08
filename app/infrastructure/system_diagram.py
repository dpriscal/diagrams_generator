from diagrams import Cluster, Diagram, Edge, Node
from diagrams.azure.general import Usericon

node_attr = {
    "shape": "square",
    "height": "0.8",
    "style": "filled",
    "color": "lightgrey",
    "labelloc": "c",
}

attribute_attr = {
    "shape": "circle",
    "height": "0.8",
    "style": "filled",
    "color": "lightblue",
    "labelloc": "c",
}

edge_attr = {"shape": "none"}


class SystemDiagram:
    def __init__(self, system):
        self.system = system
        self.nodesMap = {}

    def printSystem(self):
        with Diagram(
            self.system.name, show=False, filename="./diagrams/" + self.getDiagramName()
        ):
            for relationship in self.system.relationships:
                self.printRelationship(relationship)

    def printRelationship(self, relationship):
        sourceEntity = relationship.sourceEntity
        targetEntity = relationship.targetEntity

        sourceEntityNode = self.getNodeWithAttributes(
            sourceEntity.name, sourceEntity.attributes
        )
        targetEntityNode = self.getNodeWithAttributes(
            targetEntity.name, targetEntity.attributes
        )

        label = relationship.relationName + " " + relationship.type
        sourceEntityNode >> Edge(label=label) >> targetEntityNode

    def getNodeWithAttributes(self, name, attributes):
        if name not in self.nodesMap:
            node = Node(name, **node_attr)
            self.nodesMap[name] = node
            for attribute in attributes:
                node - self.getAttribute(attribute)

        return self.nodesMap[name]

    def getAttribute(self, name):
        return Node(name, **attribute_attr)

    def getDiagramName(self):
        return self.system.name.replace(" ", "_").lower()
