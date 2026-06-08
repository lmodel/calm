erDiagram
Architecture {
    stringList adrs  
    Metadata metadata  
}
ComposedOfRelationship {
    string container  
}
ConnectsRelationship {

}
Control {

}
Decision {
    string description  
    string Decision_description  
}
DeployedInRelationship {
    string container  
}
Flow {
    string name  
    string description  
    string Flow_description  
    Metadata metadata  
    string requirement_url  
    string unique_id  
}
InteractsRelationship {
    string actor  
}
InterfaceDefinition {
    Metadata InterfaceDefinition_config  
    Metadata config  
    string definition_url  
    string unique_id  
}
Node {
    string name  
    string description  
    string Node_description  
    Metadata details  
    Metadata metadata  
    NodeType node_type  
    string unique_id  
}
NodeInterface {
    string node  
}
Relationship {
    string description  
    Metadata metadata  
    Protocol protocol  
    string unique_id  
}
RelationshipType {

}
Timeline {
    string current_moment  
    Metadata metadata  
    stringList moments  
}
Transition {
    string description  
    string Transition_description  
    TransitionDirection direction  
    string relationship_unique_id  
    integer sequence_number  
}

Architecture ||--|o Control : "controls"
Architecture ||--}o Flow : "Architecture_flows, flows"
Architecture ||--}o Node : "Architecture_nodes, nodes"
Architecture ||--}o Relationship : "Architecture_relationships, relationships"
ComposedOfRelationship ||--}| Node : "ComposedOfRelationship_nodes, nodes"
ConnectsRelationship ||--|| NodeInterface : "destination, source"
Decision ||--|o Control : "controls"
Decision ||--}| Node : "Decision_nodes, nodes"
Decision ||--}| Relationship : "Decision_relationships, relationships"
DeployedInRelationship ||--}| Node : "DeployedInRelationship_nodes, nodes"
Flow ||--|o Control : "controls"
Flow ||--}| Transition : "transitions"
InteractsRelationship ||--}| Node : "InteractsRelationship_nodes, nodes"
Node ||--|o Control : "controls"
Node ||--}o InterfaceDefinition : "Node_interfaces, interfaces"
NodeInterface ||--}o InterfaceDefinition : "NodeInterface_interfaces, interfaces"
Relationship ||--|o Control : "controls"
Relationship ||--|| RelationshipType : "relationship_type"
RelationshipType ||--|o ComposedOfRelationship : "composed_of"
RelationshipType ||--|o ConnectsRelationship : "connects"
RelationshipType ||--|o DeployedInRelationship : "deployed_in"
RelationshipType ||--|o InteractsRelationship : "interacts"
RelationshipType ||--}o Decision : "options"

