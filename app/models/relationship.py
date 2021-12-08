class Relationship:
    def __init__(self, sourceEntity, targetEntity, relationName, type):
        self.sourceEntity = sourceEntity
        self.targetEntity = targetEntity
        self.relationName = relationName
        self.type = type
