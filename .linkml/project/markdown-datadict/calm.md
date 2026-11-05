
# CALM


**metamodel version:** 1.11.0

**version:** 1.2


LinkML representation of the FINOS Common Architecture Language Model (CALM) 1.2 specification. CALM is a declarative, JSON-based modeling language for describing complex software architectures (nodes, relationships, controls, flows, decorators, timelines, evidence, and units). This LinkML schema is generated from the CALM JSON-Schema meta files.


## Class Diagram

```mermaid
classDiagram
Node <|-- NodeMoment
```

## ERD Diagram

```mermaid
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
NodeMoment {
    Metadata NodeMoment_details  
    stringList adrs  
    Metadata details  
    date valid_from  
    string name  
    string description  
    string Node_description  
    Metadata metadata  
    NodeType node_type  
    string unique_id  
}
OptionList {

}
Relationship {
    string description  
    Metadata metadata  
    Protocol protocol  
    string unique_id  
}
RelationshipType {

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
NodeMoment ||--|o Control : "controls"
NodeMoment ||--}o InterfaceDefinition : "Node_interfaces, interfaces"
OptionList ||--}o Decision : "decisions"
Relationship ||--|o Control : "controls"
Relationship ||--|| RelationshipType : "relationship_type"
RelationshipType ||--|o ComposedOfRelationship : "composed_of"
RelationshipType ||--|o ConnectsRelationship : "connects"
RelationshipType ||--|o DeployedInRelationship : "deployed_in"
RelationshipType ||--|o InteractsRelationship : "interacts"
RelationshipType ||--}o Decision : "options"

```

## Base Classes


Foundational classes in the hierarchy (root classes and direct children of Thing):

| Class | Description |
| --- | --- |
| [Node](#Node) | A logical or physical element of an architecture (system, service, actor, ...). |

## Standalone Classes


These classes are completely isolated with no relationships and are not used as base classes:

| Class | Description |
| --- | --- |
| [ControlDetail](#ControlDetail) | A single control requirement and its inline / referenced configuration. |
| [ControlRequirement](#ControlRequirement) | Domain-defined control requirement that controls can reference. |
| [Decorator](#Decorator) | Cross-cutting annotation attached to nodes, relationships, or flows. |
| [EvidenceDocument](#EvidenceDocument) | Top-level CALM evidence document linking control configurations to evidence artefacts. |
| [InterfaceType](#InterfaceType) | Inline (free-form) interface definition keyed by unique-id. |
| [RateUnit](#RateUnit) | A rate (count per time unit), e.g. operations per second. |
| [TimeUnit](#TimeUnit) | A quantity of time expressed as a numeric value and a unit. |
| [Timeline](#Timeline) | CALM timeline document capturing architecture moments over time. |

## Classes


### Architecture

Top-level CALM architecture document.

```mermaid
erDiagram
Architecture {

}
Control {

}
Flow {

}
Node {

}
Relationship {

}

Architecture ||--|o Control : "controls"
Architecture ||--}o Flow : "Architecture_flows, flows"
Architecture ||--}o Node : "Architecture_nodes, nodes"
Architecture ||--}o Relationship : "Architecture_relationships, relationships"
Flow ||--|o Control : "controls"
Flow ||--}| Transition : "transitions"
Node ||--|o Control : "controls"
Node ||--}o InterfaceDefinition : "Node_interfaces, interfaces"
Relationship ||--|o Control : "controls"
Relationship ||--|| RelationshipType : "relationship_type"

```

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[Architecture_flows](#ArchitectureFlows)** | <sub>0..\*</sub> | [Flow](#Flow) |  |
| **[Architecture_nodes](#ArchitectureNodes)** | <sub>0..\*</sub> | [Node](#Node) |  |
| **[Architecture_relationships](#ArchitectureRelationships)** | <sub>0..\*</sub> | [Relationship](#Relationship) |  |
| **[adrs](#Adrs)** | <sub>0..\*</sub> | string | External links to ADRs (Architecture Decision Records) or similar documents that provide context or decisions related to the architecture. These can be URLs or references to internal documentation. |
| **[controls](#Controls)** | <sub>0..1</sub> | [Control](#Control) |  |
| **[flows](#Flows)** | <sub>0..\*</sub> | [Flow](#Flow) |  |
| **[metadata](#Metadata)** | <sub>0..1</sub> | Metadata |  |
| **[nodes](#Nodes)** | <sub>0..\*</sub> | [Node](#Node) |  |
| **[relationships](#Relationships)** | <sub>0..\*</sub> | [Relationship](#Relationship) |  |




### ComposedOfRelationship

A ``composed-of`` containment relationship.

```mermaid
erDiagram
ComposedOfRelationship {

}
Node {

}
RelationshipType {

}

ComposedOfRelationship ||--}| Node : "ComposedOfRelationship_nodes, nodes"
Node ||--|o Control : "controls"
Node ||--}o InterfaceDefinition : "Node_interfaces, interfaces"
RelationshipType ||--|o ComposedOfRelationship : "composed_of"
RelationshipType ||--|o ConnectsRelationship : "connects"
RelationshipType ||--|o DeployedInRelationship : "deployed_in"
RelationshipType ||--|o InteractsRelationship : "interacts"
RelationshipType ||--}o Decision : "options"

```

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[ComposedOfRelationship_nodes](#ComposedOfRelationshipNodes)** | <sub>1..\*</sub> | [Node](#Node) |  |
| **[container](#Container)** | <sub>1..1</sub> | string |  |
| **[nodes](#Nodes)** | <sub>1..\*</sub> | [Node](#Node) |  |

#### Referenced by:

 *  **[RelationshipType](#RelationshipType)** : composed_of  <sub>0..1</sub> 




### ConnectsRelationship

A ``connects`` relationship between two node interfaces.

```mermaid
erDiagram
ConnectsRelationship {

}
NodeInterface {

}
RelationshipType {

}

ConnectsRelationship ||--|| NodeInterface : "destination, source"
NodeInterface ||--}o InterfaceDefinition : "NodeInterface_interfaces, interfaces"
RelationshipType ||--|o ComposedOfRelationship : "composed_of"
RelationshipType ||--|o ConnectsRelationship : "connects"
RelationshipType ||--|o DeployedInRelationship : "deployed_in"
RelationshipType ||--|o InteractsRelationship : "interacts"
RelationshipType ||--}o Decision : "options"

```

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[destination](#Destination)** | <sub>1..1</sub> | [NodeInterface](#NodeInterface) |  |
| **[source](#Source)** | <sub>1..1</sub> | [NodeInterface](#NodeInterface) |  |

#### Referenced by:

 *  **[RelationshipType](#RelationshipType)** : connects  <sub>0..1</sub> 




### Control

A named control attached to an architecture element.

```mermaid
erDiagram
Architecture {

}
Control {

}
Decision {

}
Flow {

}
Node {

}
NodeMoment {

}
Relationship {

}

Architecture ||--|o Control : "controls"
Architecture ||--}o Flow : "Architecture_flows, flows"
Architecture ||--}o Node : "Architecture_nodes, nodes"
Architecture ||--}o Relationship : "Architecture_relationships, relationships"
Decision ||--|o Control : "controls"
Decision ||--}| Node : "Decision_nodes, nodes"
Decision ||--}| Relationship : "Decision_relationships, relationships"
Flow ||--|o Control : "controls"
Flow ||--}| Transition : "transitions"
Node ||--|o Control : "controls"
Node ||--}o InterfaceDefinition : "Node_interfaces, interfaces"
NodeMoment ||--|o Control : "controls"
NodeMoment ||--}o InterfaceDefinition : "Node_interfaces, interfaces"
Relationship ||--|o Control : "controls"
Relationship ||--|| RelationshipType : "relationship_type"

```

This class has no attributes


#### Referenced by:

 *  **[Architecture](#Architecture)** : controls  <sub>0..1</sub> 
 *  **[Decision](#Decision)** : controls  <sub>0..1</sub> 
 *  **[Flow](#Flow)** : controls  <sub>0..1</sub> 
 *  **[Node](#Node)** : controls  <sub>0..1</sub> 
 *  **[NodeMoment](#NodeMoment)** : controls  <sub>0..1</sub> 
 *  **[Relationship](#Relationship)** : controls  <sub>0..1</sub> 




### ControlDetail

A single control requirement and its inline / referenced configuration.


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[ControlDetail_requirement_url](#ControlDetailRequirementUrl)** | <sub>1..1</sub> | string | The requirement schema that specifies how a control should be defined |
| **[config](#Config)** | <sub>0..1</sub> | Metadata | Inline configuration of how the control requirement schema is met |
| **[config_url](#ConfigUrl)** | <sub>0..1</sub> | string | The configuration of how the control requirement schema is met |
| **[requirement_url](#RequirementUrl)** | <sub>1..1</sub> | string | The requirement schema that specifies how a control should be defined |




### ControlRequirement

Domain-defined control requirement that controls can reference.


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[name](#Name)** | <sub>1..1</sub> | string | Short human-readable name. |
| **[description](#Description)** | <sub>1..1</sub> | string | Free-form description of the element. |
| **[ControlRequirement_description](#ControlRequirementDescription)** | <sub>1..1</sub> | string | Free-form description of the element. |
| **[control_id](#ControlId)** | <sub>1..1</sub> | string | The unique identifier of this control, which has the potential to be used for linking evidence |




### Decision

A candidate decision within an ``options`` relationship.

```mermaid
erDiagram
Control {

}
Decision {

}
Node {

}
OptionList {

}
Relationship {

}
RelationshipType {

}

Decision ||--|o Control : "controls"
Decision ||--}| Node : "Decision_nodes, nodes"
Decision ||--}| Relationship : "Decision_relationships, relationships"
Node ||--|o Control : "controls"
Node ||--}o InterfaceDefinition : "Node_interfaces, interfaces"
OptionList ||--}o Decision : "decisions"
Relationship ||--|o Control : "controls"
Relationship ||--|| RelationshipType : "relationship_type"
RelationshipType ||--|o ComposedOfRelationship : "composed_of"
RelationshipType ||--|o ConnectsRelationship : "connects"
RelationshipType ||--|o DeployedInRelationship : "deployed_in"
RelationshipType ||--|o InteractsRelationship : "interacts"
RelationshipType ||--}o Decision : "options"

```

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[description](#Description)** | <sub>1..1</sub> | string | Free-form description of the element. |
| **[Decision_description](#DecisionDescription)** | <sub>1..1</sub> | string | Free-form description of the element. |
| **[Decision_nodes](#DecisionNodes)** | <sub>1..\*</sub> | [Node](#Node) |  |
| **[Decision_relationships](#DecisionRelationships)** | <sub>1..\*</sub> | [Relationship](#Relationship) |  |
| **[controls](#Controls)** | <sub>0..1</sub> | [Control](#Control) |  |
| **[nodes](#Nodes)** | <sub>1..\*</sub> | [Node](#Node) |  |
| **[relationships](#Relationships)** | <sub>1..\*</sub> | [Relationship](#Relationship) |  |

#### Referenced by:

 *  **[OptionList](#OptionList)** : decisions  <sub>0..\*</sub> 
 *  **[RelationshipType](#RelationshipType)** : options  <sub>0..\*</sub> 




### Decorator

Cross-cutting annotation attached to nodes, relationships, or flows.


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[applies_to](#AppliesTo)** | <sub>1..\*</sub> | string | Array of unique-ids referencing nodes, relationships, flows, or other architecture elements |
| **[data](#Data)** | <sub>1..1</sub> | Metadata | Free-form JSON object containing the decorator's data |
| **[target](#Target)** | <sub>1..\*</sub> | string | Array of file paths or URLs referencing the CALM documents (patterns, architectures, or controls) this decorator targets |
| **[type](#Type)** | <sub>1..1</sub> | string | Type of decorator - a free-form string identifying the decorator category |
| **[unique_id](#UniqueId)** | <sub>1..1</sub> | string | Stable opaque identifier used to cross-link CALM elements. |




### DeployedInRelationship

A ``deployed-in`` containment relationship.

```mermaid
erDiagram
DeployedInRelationship {

}
Node {

}
RelationshipType {

}

DeployedInRelationship ||--}| Node : "DeployedInRelationship_nodes, nodes"
Node ||--|o Control : "controls"
Node ||--}o InterfaceDefinition : "Node_interfaces, interfaces"
RelationshipType ||--|o ComposedOfRelationship : "composed_of"
RelationshipType ||--|o ConnectsRelationship : "connects"
RelationshipType ||--|o DeployedInRelationship : "deployed_in"
RelationshipType ||--|o InteractsRelationship : "interacts"
RelationshipType ||--}o Decision : "options"

```

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[DeployedInRelationship_nodes](#DeployedInRelationshipNodes)** | <sub>1..\*</sub> | [Node](#Node) |  |
| **[container](#Container)** | <sub>1..1</sub> | string |  |
| **[nodes](#Nodes)** | <sub>1..\*</sub> | [Node](#Node) |  |

#### Referenced by:

 *  **[RelationshipType](#RelationshipType)** : deployed_in  <sub>0..1</sub> 




### EvidenceDocument

Top-level CALM evidence document linking control configurations to evidence artefacts.


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[evidence](#Evidence)** | <sub>1..1</sub> | Metadata |  |




### Flow

Business flow mapped onto architecture relationships.

```mermaid
erDiagram
Architecture {

}
Control {

}
Flow {

}
Transition {

}

Architecture ||--|o Control : "controls"
Architecture ||--}o Flow : "Architecture_flows, flows"
Architecture ||--}o Node : "Architecture_nodes, nodes"
Architecture ||--}o Relationship : "Architecture_relationships, relationships"
Flow ||--|o Control : "controls"
Flow ||--}| Transition : "transitions"

```

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[name](#Name)** | <sub>1..1</sub> | string | Short human-readable name. |
| **[description](#Description)** | <sub>1..1</sub> | string | Free-form description of the element. |
| **[Flow_description](#FlowDescription)** | <sub>1..1</sub> | string | Free-form description of the element. |
| **[controls](#Controls)** | <sub>0..1</sub> | [Control](#Control) |  |
| **[metadata](#Metadata)** | <sub>0..1</sub> | Metadata |  |
| **[requirement_url](#RequirementUrl)** | <sub>0..1</sub> | string | The requirement schema that specifies how a control should be defined |
| **[transitions](#Transitions)** | <sub>1..\*</sub> | [Transition](#Transition) |  |
| **[unique_id](#UniqueId)** | <sub>1..1</sub> | string | Stable opaque identifier used to cross-link CALM elements. |

#### Referenced by:

 *  **[Architecture](#Architecture)** : flows  <sub>0..\*</sub> 
 *  **[Architecture](#Architecture)** : flows  <sub>0..\*</sub> 




### InteractsRelationship

An ``interacts`` relationship between an actor and one or more nodes.

```mermaid
erDiagram
InteractsRelationship {

}
Node {

}
RelationshipType {

}

InteractsRelationship ||--}| Node : "InteractsRelationship_nodes, nodes"
Node ||--|o Control : "controls"
Node ||--}o InterfaceDefinition : "Node_interfaces, interfaces"
RelationshipType ||--|o ComposedOfRelationship : "composed_of"
RelationshipType ||--|o ConnectsRelationship : "connects"
RelationshipType ||--|o DeployedInRelationship : "deployed_in"
RelationshipType ||--|o InteractsRelationship : "interacts"
RelationshipType ||--}o Decision : "options"

```

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[InteractsRelationship_nodes](#InteractsRelationshipNodes)** | <sub>1..\*</sub> | [Node](#Node) |  |
| **[actor](#Actor)** | <sub>1..1</sub> | string |  |
| **[nodes](#Nodes)** | <sub>1..\*</sub> | [Node](#Node) |  |

#### Referenced by:

 *  **[RelationshipType](#RelationshipType)** : interacts  <sub>0..1</sub> 




### InterfaceDefinition

Modular interface definition referencing an external schema.

```mermaid
erDiagram
InterfaceDefinition {

}
Node {

}
NodeInterface {

}
NodeMoment {

}

Node ||--|o Control : "controls"
Node ||--}o InterfaceDefinition : "Node_interfaces, interfaces"
NodeInterface ||--}o InterfaceDefinition : "NodeInterface_interfaces, interfaces"
NodeMoment ||--|o Control : "controls"
NodeMoment ||--}o InterfaceDefinition : "Node_interfaces, interfaces"

```

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[InterfaceDefinition_config](#InterfaceDefinitionConfig)** | <sub>1..1</sub> | Metadata | Inline configuration of how the control requirement schema is met |
| **[config](#Config)** | <sub>1..1</sub> | Metadata | Inline configuration of how the control requirement schema is met |
| **[definition_url](#DefinitionUrl)** | <sub>1..1</sub> | string | URI of the external schema this interface configuration conforms to |
| **[unique_id](#UniqueId)** | <sub>1..1</sub> | string | Stable opaque identifier used to cross-link CALM elements. |

#### Referenced by:

 *  **[NodeInterface](#NodeInterface)** : interfaces  <sub>0..\*</sub> 
 *  **[Node](#Node)** : interfaces  <sub>0..\*</sub> 
 *  **[Node](#Node)** : interfaces  <sub>0..\*</sub> 
 *  **[NodeInterface](#NodeInterface)** : interfaces  <sub>0..\*</sub> 
 *  **[NodeMoment](#NodeMoment)** : interfaces  <sub>0..\*</sub> 




### InterfaceType

Inline (free-form) interface definition keyed by unique-id.


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[unique_id](#UniqueId)** | <sub>1..1</sub> | string | Stable opaque identifier used to cross-link CALM elements. |




### Node

A logical or physical element of an architecture (system, service, actor, ...).

```mermaid
erDiagram
Architecture {

}
ComposedOfRelationship {

}
Control {

}
Decision {

}
DeployedInRelationship {

}
InteractsRelationship {

}
InterfaceDefinition {

}
Node {

}

Architecture ||--|o Control : "controls"
Architecture ||--}o Flow : "Architecture_flows, flows"
Architecture ||--}o Node : "Architecture_nodes, nodes"
Architecture ||--}o Relationship : "Architecture_relationships, relationships"
ComposedOfRelationship ||--}| Node : "ComposedOfRelationship_nodes, nodes"
Decision ||--|o Control : "controls"
Decision ||--}| Node : "Decision_nodes, nodes"
Decision ||--}| Relationship : "Decision_relationships, relationships"
DeployedInRelationship ||--}| Node : "DeployedInRelationship_nodes, nodes"
InteractsRelationship ||--}| Node : "InteractsRelationship_nodes, nodes"
Node ||--|o Control : "controls"
Node ||--}o InterfaceDefinition : "Node_interfaces, interfaces"

```

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[name](#Name)** | <sub>1..1</sub> | string | Short human-readable name. |
| **[description](#Description)** | <sub>1..1</sub> | string | Free-form description of the element. |
| **[Node_description](#NodeDescription)** | <sub>1..1</sub> | string | Free-form description of the element. |
| **[Node_interfaces](#NodeInterfaces)** | <sub>0..\*</sub> | [InterfaceDefinition](#InterfaceDefinition) | Interface definitions exposed by nodes. |
| **[controls](#Controls)** | <sub>0..1</sub> | [Control](#Control) |  |
| **[details](#Details)** | <sub>0..1</sub> | Metadata |  |
| **[interfaces](#Interfaces)** | <sub>0..\*</sub> | [InterfaceDefinition](#InterfaceDefinition) | Interface definitions exposed by nodes. |
| **[metadata](#Metadata)** | <sub>0..1</sub> | Metadata |  |
| **[node_type](#NodeType)** | <sub>1..1</sub> | [NodeType](#NodeType) | Category of the node (system, service, actor, etc.). |
| **[unique_id](#UniqueId)** | <sub>1..1</sub> | string | Stable opaque identifier used to cross-link CALM elements. |

#### Children

 * [NodeMoment](#NodeMoment) - An architecture moment - a point-in-time snapshot of the architecture.

#### Referenced by:

 *  **[Architecture](#Architecture)** : nodes  <sub>0..\*</sub> 
 *  **[ComposedOfRelationship](#ComposedOfRelationship)** : nodes  <sub>1..\*</sub> 
 *  **[Decision](#Decision)** : nodes  <sub>1..\*</sub> 
 *  **[DeployedInRelationship](#DeployedInRelationship)** : nodes  <sub>1..\*</sub> 
 *  **[InteractsRelationship](#InteractsRelationship)** : nodes  <sub>1..\*</sub> 
 *  **[Architecture](#Architecture)** : nodes  <sub>0..\*</sub> 
 *  **[ComposedOfRelationship](#ComposedOfRelationship)** : nodes  <sub>0..\*</sub> 
 *  **[Decision](#Decision)** : nodes  <sub>0..\*</sub> 
 *  **[DeployedInRelationship](#DeployedInRelationship)** : nodes  <sub>0..\*</sub> 
 *  **[InteractsRelationship](#InteractsRelationship)** : nodes  <sub>0..\*</sub> 




### NodeInterface

Reference to one or more interfaces exposed by a node.

```mermaid
erDiagram
ConnectsRelationship {

}
InterfaceDefinition {

}
NodeInterface {

}

ConnectsRelationship ||--|| NodeInterface : "destination, source"
NodeInterface ||--}o InterfaceDefinition : "NodeInterface_interfaces, interfaces"

```

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[NodeInterface_interfaces](#NodeInterfaceInterfaces)** | <sub>0..\*</sub> | [InterfaceDefinition](#InterfaceDefinition) | Interface definitions exposed by nodes. |
| **[interfaces](#Interfaces)** | <sub>0..\*</sub> | [InterfaceDefinition](#InterfaceDefinition) | Interface definitions exposed by nodes. |
| **[node](#Node)** | <sub>1..1</sub> | string |  |

#### Referenced by:

 *  **[ConnectsRelationship](#ConnectsRelationship)** : destination  <sub>1..1</sub> 
 *  **[ConnectsRelationship](#ConnectsRelationship)** : source  <sub>1..1</sub> 




### NodeMoment

An architecture moment - a point-in-time snapshot of the architecture.

```mermaid
erDiagram
Control {

}
InterfaceDefinition {

}
NodeMoment {

}

NodeMoment ||--|o Control : "controls"
NodeMoment ||--}o InterfaceDefinition : "Node_interfaces, interfaces"

```

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[name](#Name)** | <sub>1..1</sub> | string | Short human-readable name. |
| **[description](#Description)** | <sub>1..1</sub> | string | Free-form description of the element. |
| **[Node_interfaces](#NodeInterfaces)** | <sub>0..\*</sub> | [InterfaceDefinition](#InterfaceDefinition) | Interface definitions exposed by nodes. |
| **[NodeMoment_details](#NodeMomentDetails)** | <sub>1..1</sub> | Metadata |  |
| **[Node_description](#NodeDescription)** | <sub>1..1</sub> | string | Free-form description of the element. |
| **[adrs](#Adrs)** | <sub>0..\*</sub> | string | External links to ADRs (Architecture Decision Records) or similar documents that provide context or decisions related to the architecture. These can be URLs or references to internal documentation. |
| **[controls](#Controls)** | <sub>0..1</sub> | [Control](#Control) |  |
| **[details](#Details)** | <sub>1..1</sub> | Metadata |  |
| **[interfaces](#Interfaces)** | <sub>0..\*</sub> | [InterfaceDefinition](#InterfaceDefinition) | Interface definitions exposed by nodes. |
| **[metadata](#Metadata)** | <sub>0..1</sub> | Metadata |  |
| **[node_type](#NodeType)** | <sub>1..1</sub> | [NodeType](#NodeType) | Category of the node (system, service, actor, etc.). |
| **[unique_id](#UniqueId)** | <sub>1..1</sub> | string | Stable opaque identifier used to cross-link CALM elements. |
| **[valid_from](#ValidFrom)** | <sub>0..1</sub> | date | The date when this architecture moment came into effect. |

#### Parents

 * [Node](#Node) - A logical or physical element of an architecture (system, service, actor, ...).




### OptionList

Wrapper around the list of ``Decision`` alternatives in an options relationship.

```mermaid
erDiagram
Decision {

}
OptionList {

}

Decision ||--|o Control : "controls"
Decision ||--}| Node : "Decision_nodes, nodes"
Decision ||--}| Relationship : "Decision_relationships, relationships"
OptionList ||--}o Decision : "decisions"

```

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[decisions](#Decisions)** | <sub>0..\*</sub> | [Decision](#Decision) | Alternative decisions under an ``options`` relationship. |




### RateUnit

A rate (count per time unit), e.g. operations per second.


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[per](#Per)** | <sub>1..1</sub> | [RatePerUnit](#RatePerUnit) | The time unit defining the rate interval. |
| **[rate](#Rate)** | <sub>1..1</sub> | float | The numeric value representing the rate. |




### Relationship

A typed link between architecture elements.

```mermaid
erDiagram
Architecture {

}
Control {

}
Decision {

}
Relationship {

}
RelationshipType {

}

Architecture ||--|o Control : "controls"
Architecture ||--}o Flow : "Architecture_flows, flows"
Architecture ||--}o Node : "Architecture_nodes, nodes"
Architecture ||--}o Relationship : "Architecture_relationships, relationships"
Decision ||--|o Control : "controls"
Decision ||--}| Node : "Decision_nodes, nodes"
Decision ||--}| Relationship : "Decision_relationships, relationships"
Relationship ||--|o Control : "controls"
Relationship ||--|| RelationshipType : "relationship_type"
RelationshipType ||--|o ComposedOfRelationship : "composed_of"
RelationshipType ||--|o ConnectsRelationship : "connects"
RelationshipType ||--|o DeployedInRelationship : "deployed_in"
RelationshipType ||--|o InteractsRelationship : "interacts"
RelationshipType ||--}o Decision : "options"

```

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[description](#Description)** | <sub>0..1</sub> | string | Free-form description of the element. |
| **[controls](#Controls)** | <sub>0..1</sub> | [Control](#Control) |  |
| **[metadata](#Metadata)** | <sub>0..1</sub> | Metadata |  |
| **[protocol](#Protocol)** | <sub>0..1</sub> | [Protocol](#Protocol) |  |
| **[relationship_type](#RelationshipType)** | <sub>1..1</sub> | [RelationshipType](#RelationshipType) |  |
| **[unique_id](#UniqueId)** | <sub>1..1</sub> | string | Stable opaque identifier used to cross-link CALM elements. |

#### Referenced by:

 *  **[Architecture](#Architecture)** : relationships  <sub>0..\*</sub> 
 *  **[Decision](#Decision)** : relationships  <sub>1..\*</sub> 
 *  **[Architecture](#Architecture)** : relationships  <sub>0..\*</sub> 
 *  **[Decision](#Decision)** : relationships  <sub>0..\*</sub> 




### RelationshipType

Tagged-union container for the variant body of a relationship. Exactly one of ``interacts``, ``connects``, ``deployed_in``, ``composed_of``, ``options`` is populated; see ``RelationshipKind`` for the discriminator values.

```mermaid
erDiagram
ComposedOfRelationship {

}
ConnectsRelationship {

}
Decision {

}
DeployedInRelationship {

}
InteractsRelationship {

}
Relationship {

}
RelationshipType {

}

ComposedOfRelationship ||--}| Node : "ComposedOfRelationship_nodes, nodes"
ConnectsRelationship ||--|| NodeInterface : "destination, source"
Decision ||--|o Control : "controls"
Decision ||--}| Node : "Decision_nodes, nodes"
Decision ||--}| Relationship : "Decision_relationships, relationships"
DeployedInRelationship ||--}| Node : "DeployedInRelationship_nodes, nodes"
InteractsRelationship ||--}| Node : "InteractsRelationship_nodes, nodes"
Relationship ||--|o Control : "controls"
Relationship ||--|| RelationshipType : "relationship_type"
RelationshipType ||--|o ComposedOfRelationship : "composed_of"
RelationshipType ||--|o ConnectsRelationship : "connects"
RelationshipType ||--|o DeployedInRelationship : "deployed_in"
RelationshipType ||--|o InteractsRelationship : "interacts"
RelationshipType ||--}o Decision : "options"

```

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[composed_of](#ComposedOf)** | <sub>0..1</sub> | [ComposedOfRelationship](#ComposedOfRelationship) |  |
| **[connects](#Connects)** | <sub>0..1</sub> | [ConnectsRelationship](#ConnectsRelationship) |  |
| **[deployed_in](#DeployedIn)** | <sub>0..1</sub> | [DeployedInRelationship](#DeployedInRelationship) |  |
| **[interacts](#Interacts)** | <sub>0..1</sub> | [InteractsRelationship](#InteractsRelationship) |  |
| **[options](#Options)** | <sub>0..\*</sub> | [Decision](#Decision) |  |

#### Referenced by:

 *  **[Relationship](#Relationship)** : relationship_type  <sub>1..1</sub> 




### TimeUnit

A quantity of time expressed as a numeric value and a unit.


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[unit](#Unit)** | <sub>1..1</sub> | [TimeUnitName](#TimeUnitName) | The unit of time (e.g., seconds, minutes, hours). |
| **[value](#Value)** | <sub>1..1</sub> | float | The numeric value representing the amount of time. |




### Timeline

CALM timeline document capturing architecture moments over time.


#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[current_moment](#CurrentMoment)** | <sub>0..1</sub> | string | The unique-id of the current architecture moment within the timeline. |
| **[metadata](#Metadata)** | <sub>0..1</sub> | Metadata |  |
| **[moments](#Moments)** | <sub>1..\*</sub> | string | A list of significant architecture states or points in time, each represented as a 'moment'. |




### Transition

A single step in a flow, anchored on a relationship.

```mermaid
erDiagram
Flow {

}
Transition {

}

Flow ||--|o Control : "controls"
Flow ||--}| Transition : "transitions"

```

#### Attributes

| Name | Cardinality: | Type | Description |
| --- | --- | --- | --- |
| **[description](#Description)** | <sub>1..1</sub> | string | Free-form description of the element. |
| **[Transition_description](#TransitionDescription)** | <sub>1..1</sub> | string | Free-form description of the element. |
| **[direction](#Direction)** | <sub>0..1</sub> | [TransitionDirection](#TransitionDirection) | Direction of flow on the transition. |
| **[relationship_unique_id](#RelationshipUniqueId)** | <sub>1..1</sub> | string | Unique identifier for the relationship in the architecture |
| **[sequence_number](#SequenceNumber)** | <sub>1..1</sub> | integer | Indicates the sequence of the relationship in the flow |

#### Referenced by:

 *  **[Flow](#Flow)** : transitions  <sub>1..\*</sub> 




## Slots

| Name | Cardinality/Range | Used By |
| --- | --- | --- |
| <a id="Name"></a>**name**<br/>Short human-readable name. | <sub>1..1</sub><br/>string | [ControlRequirement](#ControlRequirement), [Flow](#Flow), [Node](#Node), [NodeMoment](#NodeMoment) |
| <a id="Description"></a>**description**<br/>Free-form description of the element. | <sub>0..1</sub><br/>string | [ControlRequirement](#ControlRequirement), [Decision](#Decision), [Flow](#Flow), [Node](#Node), [NodeMoment](#NodeMoment), [Relationship](#Relationship), [Transition](#Transition) |
| <a id="ArchitectureFlows"></a>**Architecture_flows** | <sub>0..\*</sub><br/>[Flow](#Flow) | [Architecture](#Architecture) |
| <a id="ArchitectureNodes"></a>**Architecture_nodes** | <sub>0..\*</sub><br/>[Node](#Node) | [Architecture](#Architecture) |
| <a id="ArchitectureRelationships"></a>**Architecture_relationships** | <sub>0..\*</sub><br/>[Relationship](#Relationship) | [Architecture](#Architecture) |
| <a id="ComposedOfRelationshipNodes"></a>**ComposedOfRelationship_nodes** | <sub>1..\*</sub><br/>[Node](#Node) | [ComposedOfRelationship](#ComposedOfRelationship) |
| <a id="ControlDetailRequirementUrl"></a>**ControlDetail_requirement_url**<br/>The requirement schema that specifies how a control should be defined | <sub>1..1</sub><br/>string | [ControlDetail](#ControlDetail) |
| <a id="ControlRequirementDescription"></a>**ControlRequirement_description**<br/>Free-form description of the element. | <sub>1..1</sub><br/>string | [ControlRequirement](#ControlRequirement) |
| <a id="DecisionDescription"></a>**Decision_description**<br/>Free-form description of the element. | <sub>1..1</sub><br/>string | [Decision](#Decision) |
| <a id="DecisionNodes"></a>**Decision_nodes** | <sub>1..\*</sub><br/>[Node](#Node) | [Decision](#Decision) |
| <a id="DecisionRelationships"></a>**Decision_relationships** | <sub>1..\*</sub><br/>[Relationship](#Relationship) | [Decision](#Decision) |
| <a id="DeployedInRelationshipNodes"></a>**DeployedInRelationship_nodes** | <sub>1..\*</sub><br/>[Node](#Node) | [DeployedInRelationship](#DeployedInRelationship) |
| <a id="FlowDescription"></a>**Flow_description**<br/>Free-form description of the element. | <sub>1..1</sub><br/>string | [Flow](#Flow) |
| <a id="InteractsRelationshipNodes"></a>**InteractsRelationship_nodes** | <sub>1..\*</sub><br/>[Node](#Node) | [InteractsRelationship](#InteractsRelationship) |
| <a id="InterfaceDefinitionConfig"></a>**InterfaceDefinition_config**<br/>Inline configuration of how the control requirement schema is met | <sub>1..1</sub><br/>Metadata | [InterfaceDefinition](#InterfaceDefinition) |
| <a id="NodeInterfaceInterfaces"></a>**NodeInterface_interfaces**<br/>Interface definitions exposed by nodes. | <sub>0..\*</sub><br/>[InterfaceDefinition](#InterfaceDefinition) | [NodeInterface](#NodeInterface) |
| <a id="NodeMomentDetails"></a>**NodeMoment_details** | <sub>1..1</sub><br/>Metadata | [NodeMoment](#NodeMoment) |
| <a id="NodeDescription"></a>**Node_description**<br/>Free-form description of the element. | <sub>1..1</sub><br/>string | [Node](#Node), [NodeMoment](#NodeMoment) |
| <a id="NodeInterfaces"></a>**Node_interfaces**<br/>Interface definitions exposed by nodes. | <sub>0..\*</sub><br/>[InterfaceDefinition](#InterfaceDefinition) | [Node](#Node), [NodeMoment](#NodeMoment) |
| <a id="TransitionDescription"></a>**Transition_description**<br/>Free-form description of the element. | <sub>1..1</sub><br/>string | [Transition](#Transition) |
| <a id="Actor"></a>**actor** | <sub>1..1</sub><br/>string | [InteractsRelationship](#InteractsRelationship) |
| <a id="Adrs"></a>**adrs**<br/>External links to ADRs (Architecture Decision Records) or similar documents that provide context or decisions related to the architecture. These can be URLs or references to internal documentation. | <sub>0..\*</sub><br/>string | [Architecture](#Architecture), [NodeMoment](#NodeMoment) |
| <a id="AppliesTo"></a>**applies_to**<br/>Array of unique-ids referencing nodes, relationships, flows, or other architecture elements | <sub>1..\*</sub><br/>string | [Decorator](#Decorator) |
| <a id="ComposedOf"></a>**composed_of** | <sub>0..1</sub><br/>[ComposedOfRelationship](#ComposedOfRelationship) | [RelationshipType](#RelationshipType) |
| <a id="Config"></a>**config**<br/>Inline configuration of how the control requirement schema is met | <sub>0..1</sub><br/>Metadata | [ControlDetail](#ControlDetail), [InterfaceDefinition](#InterfaceDefinition) |
| <a id="ConfigUrl"></a>**config_url**<br/>The configuration of how the control requirement schema is met | <sub>0..1</sub><br/>string | [ControlDetail](#ControlDetail) |
| <a id="Connects"></a>**connects** | <sub>0..1</sub><br/>[ConnectsRelationship](#ConnectsRelationship) | [RelationshipType](#RelationshipType) |
| <a id="Container"></a>**container** | <sub>1..1</sub><br/>string | [ComposedOfRelationship](#ComposedOfRelationship), [DeployedInRelationship](#DeployedInRelationship) |
| <a id="ControlConfigUrl"></a>**control_config_url** | <sub>0..1</sub><br/>string |  |
| <a id="ControlId"></a>**control_id**<br/>The unique identifier of this control, which has the potential to be used for linking evidence | <sub>1..1</sub><br/>string | [ControlRequirement](#ControlRequirement) |
| <a id="Controls"></a>**controls** | <sub>0..1</sub><br/>[Control](#Control) | [Architecture](#Architecture), [Decision](#Decision), [Flow](#Flow), [Node](#Node), [NodeMoment](#NodeMoment), [Relationship](#Relationship) |
| <a id="CurrentMoment"></a>**current_moment**<br/>The unique-id of the current architecture moment within the timeline. | <sub>0..1</sub><br/>string | [Timeline](#Timeline) |
| <a id="Data"></a>**data**<br/>Free-form JSON object containing the decorator's data | <sub>1..1</sub><br/>Metadata | [Decorator](#Decorator) |
| <a id="Decisions"></a>**decisions**<br/>Alternative decisions under an ``options`` relationship. | <sub>0..\*</sub><br/>[Decision](#Decision) | [OptionList](#OptionList) |
| <a id="DefinitionUrl"></a>**definition_url**<br/>URI of the external schema this interface configuration conforms to | <sub>1..1</sub><br/>string | [InterfaceDefinition](#InterfaceDefinition) |
| <a id="DeployedIn"></a>**deployed_in** | <sub>0..1</sub><br/>[DeployedInRelationship](#DeployedInRelationship) | [RelationshipType](#RelationshipType) |
| <a id="Destination"></a>**destination** | <sub>1..1</sub><br/>[NodeInterface](#NodeInterface) | [ConnectsRelationship](#ConnectsRelationship) |
| <a id="Details"></a>**details** | <sub>0..1</sub><br/>Metadata | [Node](#Node), [NodeMoment](#NodeMoment) |
| <a id="Direction"></a>**direction**<br/>Direction of flow on the transition. | <sub>0..1</sub><br/>[TransitionDirection](#TransitionDirection) | [Transition](#Transition) |
| <a id="Evidence"></a>**evidence** | <sub>1..1</sub><br/>Metadata | [EvidenceDocument](#EvidenceDocument) |
| <a id="EvidencePaths"></a>**evidence_paths**<br/>Paths (filesystem or URL) pointing at supporting evidence. | <sub>0..\*</sub><br/>string |  |
| <a id="Flows"></a>**flows** | <sub>0..\*</sub><br/>[Flow](#Flow) | [Architecture](#Architecture) |
| <a id="Interacts"></a>**interacts** | <sub>0..1</sub><br/>[InteractsRelationship](#InteractsRelationship) | [RelationshipType](#RelationshipType) |
| <a id="Interfaces"></a>**interfaces**<br/>Interface definitions exposed by nodes. | <sub>0..\*</sub><br/>[InterfaceDefinition](#InterfaceDefinition) | [Node](#Node), [NodeInterface](#NodeInterface), [NodeMoment](#NodeMoment) |
| <a id="Metadata"></a>**metadata** | <sub>0..1</sub><br/>Metadata | [Architecture](#Architecture), [Flow](#Flow), [Node](#Node), [NodeMoment](#NodeMoment), [Relationship](#Relationship), [Timeline](#Timeline) |
| <a id="Moments"></a>**moments**<br/>A list of significant architecture states or points in time, each represented as a 'moment'. | <sub>1..\*</sub><br/>string | [Timeline](#Timeline) |
| <a id="Node"></a>**node** | <sub>1..1</sub><br/>string | [NodeInterface](#NodeInterface) |
| <a id="NodeType"></a>**node_type**<br/>Category of the node (system, service, actor, etc.). | <sub>1..1</sub><br/>[NodeType](#NodeType) | [Node](#Node), [NodeMoment](#NodeMoment) |
| <a id="Nodes"></a>**nodes** | <sub>0..\*</sub><br/>[Node](#Node) | [Architecture](#Architecture), [ComposedOfRelationship](#ComposedOfRelationship), [Decision](#Decision), [DeployedInRelationship](#DeployedInRelationship), [InteractsRelationship](#InteractsRelationship) |
| <a id="Options"></a>**options** | <sub>0..\*</sub><br/>[Decision](#Decision) | [RelationshipType](#RelationshipType) |
| <a id="Per"></a>**per**<br/>The time unit defining the rate interval. | <sub>1..1</sub><br/>[RatePerUnit](#RatePerUnit) | [RateUnit](#RateUnit) |
| <a id="Protocol"></a>**protocol** | <sub>0..1</sub><br/>[Protocol](#Protocol) | [Relationship](#Relationship) |
| <a id="Rate"></a>**rate**<br/>The numeric value representing the rate. | <sub>1..1</sub><br/>float | [RateUnit](#RateUnit) |
| <a id="RelationshipType"></a>**relationship_type** | <sub>1..1</sub><br/>[RelationshipType](#RelationshipType) | [Relationship](#Relationship) |
| <a id="RelationshipUniqueId"></a>**relationship_unique_id**<br/>Unique identifier for the relationship in the architecture | <sub>1..1</sub><br/>string | [Transition](#Transition) |
| <a id="Relationships"></a>**relationships** | <sub>0..\*</sub><br/>[Relationship](#Relationship) | [Architecture](#Architecture), [Decision](#Decision) |
| <a id="RequirementUrl"></a>**requirement_url**<br/>The requirement schema that specifies how a control should be defined | <sub>0..1</sub><br/>string | [ControlDetail](#ControlDetail), [Flow](#Flow) |
| <a id="SequenceNumber"></a>**sequence_number**<br/>Indicates the sequence of the relationship in the flow | <sub>1..1</sub><br/>integer | [Transition](#Transition) |
| <a id="Source"></a>**source** | <sub>1..1</sub><br/>[NodeInterface](#NodeInterface) | [ConnectsRelationship](#ConnectsRelationship) |
| <a id="Target"></a>**target**<br/>Array of file paths or URLs referencing the CALM documents (patterns, architectures, or controls) this decorator targets | <sub>1..\*</sub><br/>string | [Decorator](#Decorator) |
| <a id="Transitions"></a>**transitions** | <sub>1..\*</sub><br/>[Transition](#Transition) | [Flow](#Flow) |
| <a id="Type"></a>**type**<br/>Type of decorator - a free-form string identifying the decorator category | <sub>1..1</sub><br/>string | [Decorator](#Decorator) |
| <a id="UniqueId"></a>**unique_id**<br/>Stable opaque identifier used to cross-link CALM elements. | <sub>1..1</sub><br/>string | [Decorator](#Decorator), [Flow](#Flow), [InterfaceDefinition](#InterfaceDefinition), [InterfaceType](#InterfaceType), [Node](#Node), [NodeMoment](#NodeMoment), [Relationship](#Relationship) |
| <a id="Unit"></a>**unit**<br/>The unit of time (e.g., seconds, minutes, hours). | <sub>1..1</sub><br/>[TimeUnitName](#TimeUnitName) | [TimeUnit](#TimeUnit) |
| <a id="Url"></a>**url** | <sub>0..1</sub><br/>string |  |
| <a id="ValidFrom"></a>**valid_from**<br/>The date when this architecture moment came into effect. | <sub>0..1</sub><br/>date | [NodeMoment](#NodeMoment) |
| <a id="Value"></a>**value**<br/>The numeric value representing the amount of time. | <sub>1..1</sub><br/>float | [TimeUnit](#TimeUnit) |

## Enums


### NodeType

Category of architecture node. The CALM JSON-Schema allows arbitrary strings; this enum lists the canonical values plus an escape hatch via ``any_of`` on the slot.

| Text | Meaning: | Description |
| --- | --- | --- |
| actor | calm:node-type/actor | A actor node. |
| data_asset | calm:node-type/data-asset | A data-asset node. |
| database | calm:node-type/database | A database node. |
| ecosystem | calm:node-type/ecosystem | A ecosystem node. |
| ldap | calm:node-type/ldap | A ldap node. |
| network | calm:node-type/network | A network node. |
| service | calm:node-type/service | A service node. |
| system | calm:node-type/system | A system node. |
| webclient | calm:node-type/webclient | A webclient node. |

#### Used by

 *  **[Node](#Node)** *[node_type](#NodeType)*  <sub>1..1</sub> 
 *  **[NodeMoment](#NodeMoment)** *[node_type](#NodeType)*  <sub>1..1</sub> 

### Protocol

Wire-level protocol used by a relationship.

| Text | Meaning: | Description |
| --- | --- | --- |
| AMQP | calm:protocol/AMQP | The AMQP protocol. |
| FTP | calm:protocol/FTP | The FTP protocol. |
| HTTP | calm:protocol/HTTP | The HTTP protocol. |
| HTTPS | calm:protocol/HTTPS | The HTTPS protocol. |
| JDBC | calm:protocol/JDBC | The JDBC protocol. |
| LDAP | calm:protocol/LDAP | The LDAP protocol. |
| SFTP | calm:protocol/SFTP | The SFTP protocol. |
| SocketIO | calm:protocol/SocketIO | The SocketIO protocol. |
| TCP | calm:protocol/TCP | The TCP protocol. |
| TLS | calm:protocol/TLS | The TLS protocol. |
| WebSocket | calm:protocol/WebSocket | The WebSocket protocol. |
| mTLS | calm:protocol/mTLS | The mTLS protocol. |

#### Used by

 *  **[Relationship](#Relationship)** *[protocol](#Protocol)*  <sub>0..1</sub> 

### RatePerUnit

Time interval denominator used by ``RateUnit``.

| Text | Meaning: | Description |
| --- | --- | --- |
| day | None | Rate denominator: per day. |
| hour | None | Rate denominator: per hour. |
| microsecond | None | Rate denominator: per microsecond. |
| millisecond | None | Rate denominator: per millisecond. |
| minute | None | Rate denominator: per minute. |
| month | None | Rate denominator: per month. |
| nanosecond | None | Rate denominator: per nanosecond. |
| quarter | None | Rate denominator: per quarter. |
| second | None | Rate denominator: per second. |
| week | None | Rate denominator: per week. |
| year | None | Rate denominator: per year. |

#### Used by

 *  **[RateUnit](#RateUnit)** *[per](#Per)*  <sub>1..1</sub> 

### RelationshipKind

Discriminator for the variant of a ``relationship-type``: exactly one of the following keys is set on a relationship's ``relationship-type``.

| Text | Meaning: | Description |
| --- | --- | --- |
| composed_of | None | Composition: nodes composed by a container. |
| connects | None | Interface-to-interface connection. |
| deployed_in | None | Containment: nodes deployed in a container. |
| interacts | None | Actor-to-nodes interaction. |
| options | None | A set of alternative decisions. |

### TimeUnitName

Named unit of time used by ``TimeUnit``.

| Text | Meaning: | Description |
| --- | --- | --- |
| days | None | Time unit: days. |
| hours | None | Time unit: hours. |
| microseconds | None | Time unit: microseconds. |
| milliseconds | None | Time unit: milliseconds. |
| minutes | None | Time unit: minutes. |
| months | None | Time unit: months. |
| nanoseconds | None | Time unit: nanoseconds. |
| quarters | None | Time unit: quarters. |
| seconds | None | Time unit: seconds. |
| weeks | None | Time unit: weeks. |
| years | None | Time unit: years. |

#### Used by

 *  **[TimeUnit](#TimeUnit)** *[unit](#Unit)*  <sub>1..1</sub> 

### TransitionDirection

Direction of flow on a transition.

| Text | Meaning: | Description |
| --- | --- | --- |
| destination_to_source | None | Flow direction: destination-to-source. |
| source_to_destination | None | Flow direction: source-to-destination. |

#### Used by

 *  **[Transition](#Transition)** *[direction](#Direction)*  <sub>0..1</sub>

