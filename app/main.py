from fastapi import FastAPI

from app.infrastructure.system_diagram import SystemDiagram
from app.models.entity import Entity
from app.models.relationship import Relationship
from app.models.system import System

app = FastAPI()


@app.get("/")
async def root():

    entity1 = Entity("Entity 1", [])
    entity2 = Entity("Entity 2", [])
    relationship = Relationship(entity1, entity2, "relationship_test")
    relationships = [relationship]
    system = System("hellow_system", relationships)
    diagram = SystemDiagram(system)
    diagram.printSystem()
    return {"message": "Hello World"}
