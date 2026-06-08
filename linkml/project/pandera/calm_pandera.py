import pandera.polars as pla
from pandera.api.polars.types import PolarsData
from . import panderagen_polars_schema as pa_pl
import polars as pl
from typing import Optional


from pandera.typing import (
    Index,
    DataFrame,
    Series
)
from pandera.engines.polars_engine import (
    DateTime,
    Date,
    Time,
    Enum,
    Struct,
    List,
    Object
)


from linkml.generators.panderagen.linkml_pandera_validator import LinkmlPanderaValidator as _LinkmlPanderaValidator


# These are all str for now
ID_TYPES = {
    "InterfaceDefinition": "str",
    "Control": "str",
    "Node": "str",
    "InteractsRelationship": "str",
    "NodeInterface": "str",
    "ConnectsRelationship": "str",
    "DeployedInRelationship": "str",
    "ComposedOfRelationship": "str",
    "Decision": "str",
    "RelationshipType": "str",
    "Relationship": "str",
    "Transition": "str",
    "Flow": "str",
    "Architecture": "str",
    "NodeMoment": "str",
    "OptionList": "str",
    "ControlDetail": "str",
    "ControlRequirement": "str",
    "Decorator": "str",
    "EvidenceDocument": "str",
    "InterfaceType": "str",
    "Timeline": "str",
    "TimeUnit": "str",
    "RateUnit": "str",
}

# metamodel_version: 1.11.0
# version: 1.2class InterfaceDefinition(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Modular interface definition referencing an external schema.
    """

    _id_name : str =  'unique_id' 
    unique_id: str = pla.Field()
    """
    Stable opaque identifier used to cross-link CALM elements.
    """
    
    definition_url: str = pla.Field()
    """
    URI of the external schema this interface configuration conforms to
    """
    
    config: str = pla.Field()
    """
    Inline configuration of how the control requirement schema is met
    """
    
    
class Control(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A named control attached to an architecture element.
    """

    _id_name : str = None
    pass
    
    
class Node(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A logical or physical element of an architecture (system, service, actor, ...).
    """

    _id_name : str =  'unique_id' 
    unique_id: str = pla.Field()
    """
    Stable opaque identifier used to cross-link CALM elements.
    """
    
    node_type: Enum = pla.Field(dtype_kwargs={"categories":('actor','ecosystem','system','service','database','network','ldap','webclient','data_asset',)})
    """
    Category of the node (system, service, actor, etc.).
    """
    
    name: str = pla.Field()
    """
    Short human-readable name.
    """
    
    description: str = pla.Field()
    """
    Free-form description of the element.
    """
    
    details: Optional[str] = pla.Field(nullable=True, )
    interfaces: Optional[List] = pla.Field(nullable=True, )
    """
    Interface definitions exposed by nodes.
    """
    
    controls: Optional[Struct] = pla.Field(nullable=True, )
    metadata: Optional[str] = pla.Field(nullable=True, )
    
    @pla.check("interfaces")
    def check_nested_struct_interfaces(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, InterfaceDefinition, pa_pl.InterfaceDefinitionDict)
        
    @pla.check("controls")
    def check_nested_struct_controls(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, Control, pa_pl.Control)
        
class InteractsRelationship(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    An ``interacts`` relationship between an actor and one or more nodes.
    """

    _id_name : str = None
    actor: str = pla.Field()
    nodes: List = pla.Field()
    
class NodeInterface(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Reference to one or more interfaces exposed by a node.
    """

    _id_name : str = None
    node: str = pla.Field()
    interfaces: Optional[List] = pla.Field(nullable=True, )
    """
    Interface definitions exposed by nodes.
    """
    
    
    @pla.check("interfaces")
    def check_nested_struct_interfaces(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, InterfaceDefinition, pa_pl.InterfaceDefinitionDict)
        
class ConnectsRelationship(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A ``connects`` relationship between two node interfaces.
    """

    _id_name : str = None
    source: Struct = pla.Field()
    destination: Struct = pla.Field()
    
    @pla.check("source")
    def check_nested_struct_source(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, NodeInterface, pa_pl.NodeInterface)
        
    @pla.check("destination")
    def check_nested_struct_destination(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, NodeInterface, pa_pl.NodeInterface)
        
class DeployedInRelationship(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A ``deployed-in`` containment relationship.
    """

    _id_name : str = None
    container: str = pla.Field()
    nodes: List = pla.Field()
    
class ComposedOfRelationship(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A ``composed-of`` containment relationship.
    """

    _id_name : str = None
    container: str = pla.Field()
    nodes: List = pla.Field()
    
class Decision(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A candidate decision within an ``options`` relationship.
    """

    _id_name : str = None
    description: str = pla.Field()
    """
    Free-form description of the element.
    """
    
    nodes: List = pla.Field()
    relationships: List = pla.Field()
    controls: Optional[Struct] = pla.Field(nullable=True, )
    
    @pla.check("nodes")
    def check_nested_struct_nodes(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Node, pa_pl.NodeDict)
        
    @pla.check("relationships")
    def check_nested_struct_relationships(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Relationship, pa_pl.RelationshipDict)
        
    @pla.check("controls")
    def check_nested_struct_controls(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, Control, pa_pl.Control)
        
class RelationshipType(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Tagged-union container for the variant body of a relationship. Exactly one of ``interacts``, ``connects``, ``deployed_in``, ``composed_of``, ``options`` is populated; see ``RelationshipKind`` for the discriminator values.
    """

    _id_name : str = None
    interacts: Optional[Struct] = pla.Field(nullable=True, )
    connects: Optional[Struct] = pla.Field(nullable=True, )
    deployed_in: Optional[Struct] = pla.Field(nullable=True, )
    composed_of: Optional[Struct] = pla.Field(nullable=True, )
    options: Optional[List] = pla.Field(nullable=True, )
    
    @pla.check("interacts")
    def check_nested_struct_interacts(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, InteractsRelationship, pa_pl.InteractsRelationship)
        
    @pla.check("connects")
    def check_nested_struct_connects(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ConnectsRelationship, pa_pl.ConnectsRelationship)
        
    @pla.check("deployed_in")
    def check_nested_struct_deployed_in(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, DeployedInRelationship, pa_pl.DeployedInRelationship)
        
    @pla.check("composed_of")
    def check_nested_struct_composed_of(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, ComposedOfRelationship, pa_pl.ComposedOfRelationship)
        
    @pla.check("options")
    def check_nested_struct_options(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Decision, pa_pl.DecisionDict)
        
class Relationship(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A typed link between architecture elements.
    """

    _id_name : str =  'unique_id' 
    unique_id: str = pla.Field()
    """
    Stable opaque identifier used to cross-link CALM elements.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Free-form description of the element.
    """
    
    relationship_type: Struct = pla.Field()
    protocol: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('HTTP','HTTPS','FTP','SFTP','JDBC','WebSocket','SocketIO','LDAP','AMQP','TLS','mTLS','TCP',)})
    metadata: Optional[str] = pla.Field(nullable=True, )
    controls: Optional[Struct] = pla.Field(nullable=True, )
    
    @pla.check("relationship_type")
    def check_nested_struct_relationship_type(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, RelationshipType, pa_pl.RelationshipType)
        
    @pla.check("controls")
    def check_nested_struct_controls(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, Control, pa_pl.Control)
        
class Transition(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A single step in a flow, anchored on a relationship.
    """

    _id_name : str = None
    relationship_unique_id: str = pla.Field()
    """
    Unique identifier for the relationship in the architecture
    """
    
    sequence_number: int = pla.Field(ge=1, )
    """
    Indicates the sequence of the relationship in the flow
    """
    
    description: str = pla.Field()
    """
    Free-form description of the element.
    """
    
    direction: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('source_to_destination','destination_to_source',)})
    """
    Direction of flow on the transition.
    """
    
    
class Flow(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Business flow mapped onto architecture relationships.
    """

    _id_name : str =  'unique_id' 
    unique_id: str = pla.Field()
    """
    Stable opaque identifier used to cross-link CALM elements.
    """
    
    name: str = pla.Field()
    """
    Short human-readable name.
    """
    
    description: str = pla.Field()
    """
    Free-form description of the element.
    """
    
    requirement_url: Optional[str] = pla.Field(nullable=True, )
    """
    The requirement schema that specifies how a control should be defined
    """
    
    transitions: List = pla.Field()
    controls: Optional[Struct] = pla.Field(nullable=True, )
    metadata: Optional[str] = pla.Field(nullable=True, )
    
    @pla.check("transitions")
    def check_nested_struct_transitions(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Transition, pa_pl.TransitionDict)
        
    @pla.check("controls")
    def check_nested_struct_controls(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, Control, pa_pl.Control)
        
class Architecture(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Top-level CALM architecture document.
    """

    _id_name : str = None
    nodes: Optional[List] = pla.Field(nullable=True, )
    relationships: Optional[List] = pla.Field(nullable=True, )
    metadata: Optional[str] = pla.Field(nullable=True, )
    controls: Optional[Struct] = pla.Field(nullable=True, )
    flows: Optional[List] = pla.Field(nullable=True, )
    adrs: Optional[str] = pla.Field(nullable=True, )
    """
    External links to ADRs (Architecture Decision Records) or similar documents that provide context or decisions related to the architecture. These can be URLs or references to internal documentation.
    """
    
    
    @pla.check("nodes")
    def check_nested_struct_nodes(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Node, pa_pl.NodeDict)
        
    @pla.check("relationships")
    def check_nested_struct_relationships(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Relationship, pa_pl.RelationshipDict)
        
    @pla.check("controls")
    def check_nested_struct_controls(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, Control, pa_pl.Control)
        
    @pla.check("flows")
    def check_nested_struct_flows(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Flow, pa_pl.FlowDict)
        
class NodeMoment(Node):
    """
    An architecture moment - a point-in-time snapshot of the architecture.
    """

    _id_name : str =  'unique_id' 
    valid_from: Optional[Date] = pla.Field(nullable=True, )
    """
    The date when this architecture moment came into effect.
    """
    
    adrs: Optional[str] = pla.Field(nullable=True, )
    """
    External links to ADRs (Architecture Decision Records) or similar documents that provide context or decisions related to the architecture. These can be URLs or references to internal documentation.
    """
    
    interfaces: Optional[List] = pla.Field(nullable=True, )
    """
    Interface definitions exposed by nodes.
    """
    
    details: str = pla.Field()
    
    @pla.check("interfaces")
    def check_nested_struct_interfaces(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, InterfaceDefinition, pa_pl.InterfaceDefinitionDict)
        
class OptionList(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Wrapper around the list of ``Decision`` alternatives in an options relationship.
    """

    _id_name : str = None
    decisions: Optional[List] = pla.Field(nullable=True, )
    """
    Alternative decisions under an ``options`` relationship.
    """
    
    
    @pla.check("decisions")
    def check_nested_struct_decisions(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Decision, pa_pl.DecisionDict)
        
class ControlDetail(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A single control requirement and its inline / referenced configuration.
    """

    _id_name : str = None
    requirement_url: str = pla.Field()
    """
    The requirement schema that specifies how a control should be defined
    """
    
    config_url: Optional[str] = pla.Field(nullable=True, )
    """
    The configuration of how the control requirement schema is met
    """
    
    config: Optional[str] = pla.Field(nullable=True, )
    """
    Inline configuration of how the control requirement schema is met
    """
    
    
class ControlRequirement(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Domain-defined control requirement that controls can reference.
    """

    _id_name : str =  'control_id' 
    control_id: str = pla.Field()
    """
    The unique identifier of this control, which has the potential to be used for linking evidence
    """
    
    name: str = pla.Field()
    """
    Short human-readable name.
    """
    
    description: str = pla.Field()
    """
    Free-form description of the element.
    """
    
    
class Decorator(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Cross-cutting annotation attached to nodes, relationships, or flows.
    """

    _id_name : str =  'unique_id' 
    unique_id: str = pla.Field()
    """
    Stable opaque identifier used to cross-link CALM elements.
    """
    
    type: str = pla.Field()
    """
    Type of decorator - a free-form string identifying the decorator category
    """
    
    target: str = pla.Field()
    """
    Array of file paths or URLs referencing the CALM documents (patterns, architectures, or controls) this decorator targets
    """
    
    applies_to: str = pla.Field()
    """
    Array of unique-ids referencing nodes, relationships, flows, or other architecture elements
    """
    
    data: str = pla.Field()
    """
    Free-form JSON object containing the decorator's data
    """
    
    
class EvidenceDocument(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Top-level CALM evidence document linking control configurations to evidence artefacts.
    """

    _id_name : str = None
    evidence: str = pla.Field()
    
class InterfaceType(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Inline (free-form) interface definition keyed by unique-id.
    """

    _id_name : str =  'unique_id' 
    unique_id: str = pla.Field()
    """
    Stable opaque identifier used to cross-link CALM elements.
    """
    
    
class Timeline(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    CALM timeline document capturing architecture moments over time.
    """

    _id_name : str = None
    current_moment: Optional[str] = pla.Field(nullable=True, )
    """
    The unique-id of the current architecture moment within the timeline.
    """
    
    moments: str = pla.Field()
    """
    A list of significant architecture states or points in time, each represented as a 'moment'.
    """
    
    metadata: Optional[str] = pla.Field(nullable=True, )
    
class TimeUnit(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A quantity of time expressed as a numeric value and a unit.
    """

    _id_name : str = None
    unit: Enum = pla.Field(dtype_kwargs={"categories":('nanoseconds','microseconds','milliseconds','seconds','minutes','hours','days','weeks','months','quarters','years',)})
    """
    The unit of time (e.g., seconds, minutes, hours).
    """
    
    value: float = pla.Field(ge=0, )
    """
    The numeric value representing the amount of time.
    """
    
    
class RateUnit(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A rate (count per time unit), e.g. operations per second.
    """

    _id_name : str = None
    rate: float = pla.Field(ge=0, )
    """
    The numeric value representing the rate.
    """
    
    per: Enum = pla.Field(dtype_kwargs={"categories":('nanosecond','microsecond','millisecond','second','minute','hour','day','week','month','quarter','year',)})
    """
    The time unit defining the rate interval.
    """
    
    

