
from sqlalchemy import Column, Index, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()
metadata = Base.metadata


class Architecture(Base):
    """
    Top-level CALM architecture document.
    """
    __tablename__ = 'Architecture'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    metadata = Column(Text())
    controls_id = Column(Integer(), ForeignKey('Control.id'))
    controls = relationship("Control", uselist=False, foreign_keys=[controls_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='Architecture', source_slot='nodes', mapping_type=None, target_class='Node', target_slot='Architecture_id', join_class=None, uses_join_table=None, multivalued=False)
    nodes = relationship( "Node", foreign_keys="[Node.Architecture_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Architecture', source_slot='relationships', mapping_type=None, target_class='Relationship', target_slot='Architecture_id', join_class=None, uses_join_table=None, multivalued=False)
    relationships = relationship( "Relationship", foreign_keys="[Relationship.Architecture_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Architecture', source_slot='flows', mapping_type=None, target_class='Flow', target_slot='Architecture_id', join_class=None, uses_join_table=None, multivalued=False)
    flows = relationship( "Flow", foreign_keys="[Flow.Architecture_id]")
    
    
    adrs_rel = relationship( "ArchitectureAdrs" )
    adrs = association_proxy("adrs_rel", "adrs",
                                  creator=lambda x_: ArchitectureAdrs(adrs=x_))
    

    def __repr__(self):
        return f"Architecture(id={self.id},metadata={self.metadata},controls_id={self.controls_id},)"



    


class Node(Base):
    """
    A logical or physical element of an architecture (system, service, actor, ...).
    """
    __tablename__ = 'Node'

    unique_id = Column(Text(), primary_key=True, nullable=False )
    node_type = Column(Enum('actor', 'ecosystem', 'system', 'service', 'database', 'network', 'ldap', 'webclient', 'data_asset', name='NodeType'), nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    details = Column(Text())
    metadata = Column(Text())
    Architecture_id = Column(Integer(), ForeignKey('Architecture.id'))
    Decision_id = Column(Integer(), ForeignKey('Decision.id'))
    controls_id = Column(Integer(), ForeignKey('Control.id'))
    controls = relationship("Control", uselist=False, foreign_keys=[controls_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='Node', source_slot='interfaces', mapping_type=None, target_class='InterfaceDefinition', target_slot='Node_unique_id', join_class=None, uses_join_table=None, multivalued=False)
    interfaces = relationship( "InterfaceDefinition", foreign_keys="[InterfaceDefinition.Node_unique_id]")
    

    def __repr__(self):
        return f"Node(unique_id={self.unique_id},node_type={self.node_type},name={self.name},description={self.description},details={self.details},metadata={self.metadata},Architecture_id={self.Architecture_id},Decision_id={self.Decision_id},controls_id={self.controls_id},)"



    


class Relationship(Base):
    """
    A typed link between architecture elements.
    """
    __tablename__ = 'Relationship'

    unique_id = Column(Text(), primary_key=True, nullable=False )
    description = Column(Text())
    protocol = Column(Enum('HTTP', 'HTTPS', 'FTP', 'SFTP', 'JDBC', 'WebSocket', 'SocketIO', 'LDAP', 'AMQP', 'TLS', 'mTLS', 'TCP', name='Protocol'))
    metadata = Column(Text())
    Architecture_id = Column(Integer(), ForeignKey('Architecture.id'))
    Decision_id = Column(Integer(), ForeignKey('Decision.id'))
    relationship_type_id = Column(Integer(), ForeignKey('RelationshipType.id'), nullable=False )
    relationship_type = relationship("RelationshipType", uselist=False, foreign_keys=[relationship_type_id])
    controls_id = Column(Integer(), ForeignKey('Control.id'))
    controls = relationship("Control", uselist=False, foreign_keys=[controls_id])
    

    def __repr__(self):
        return f"Relationship(unique_id={self.unique_id},description={self.description},protocol={self.protocol},metadata={self.metadata},Architecture_id={self.Architecture_id},Decision_id={self.Decision_id},relationship_type_id={self.relationship_type_id},controls_id={self.controls_id},)"



    


class InteractsRelationship(Base):
    """
    An ``interacts`` relationship between an actor and one or more nodes.
    """
    __tablename__ = 'InteractsRelationship'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    actor = Column(Text(), nullable=False )
    
    
    # ManyToMany
    nodes = relationship( "Node", secondary="InteractsRelationship_nodes")
    

    def __repr__(self):
        return f"InteractsRelationship(id={self.id},actor={self.actor},)"



    


class ConnectsRelationship(Base):
    """
    A ``connects`` relationship between two node interfaces.
    """
    __tablename__ = 'ConnectsRelationship'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    source_id = Column(Integer(), ForeignKey('NodeInterface.id'), nullable=False )
    source = relationship("NodeInterface", uselist=False, foreign_keys=[source_id])
    destination_id = Column(Integer(), ForeignKey('NodeInterface.id'), nullable=False )
    destination = relationship("NodeInterface", uselist=False, foreign_keys=[destination_id])
    

    def __repr__(self):
        return f"ConnectsRelationship(id={self.id},source_id={self.source_id},destination_id={self.destination_id},)"



    


class DeployedInRelationship(Base):
    """
    A ``deployed-in`` containment relationship.
    """
    __tablename__ = 'DeployedInRelationship'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    container = Column(Text(), nullable=False )
    
    
    # ManyToMany
    nodes = relationship( "Node", secondary="DeployedInRelationship_nodes")
    

    def __repr__(self):
        return f"DeployedInRelationship(id={self.id},container={self.container},)"



    


class ComposedOfRelationship(Base):
    """
    A ``composed-of`` containment relationship.
    """
    __tablename__ = 'ComposedOfRelationship'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    container = Column(Text(), nullable=False )
    
    
    # ManyToMany
    nodes = relationship( "Node", secondary="ComposedOfRelationship_nodes")
    

    def __repr__(self):
        return f"ComposedOfRelationship(id={self.id},container={self.container},)"



    


class Decision(Base):
    """
    A candidate decision within an ``options`` relationship.
    """
    __tablename__ = 'Decision'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    description = Column(Text(), nullable=False )
    OptionList_id = Column(Integer(), ForeignKey('OptionList.id'))
    RelationshipType_id = Column(Integer(), ForeignKey('RelationshipType.id'))
    controls_id = Column(Integer(), ForeignKey('Control.id'))
    controls = relationship("Control", uselist=False, foreign_keys=[controls_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='Decision', source_slot='nodes', mapping_type=None, target_class='Node', target_slot='Decision_id', join_class=None, uses_join_table=None, multivalued=False)
    nodes = relationship( "Node", foreign_keys="[Node.Decision_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Decision', source_slot='relationships', mapping_type=None, target_class='Relationship', target_slot='Decision_id', join_class=None, uses_join_table=None, multivalued=False)
    relationships = relationship( "Relationship", foreign_keys="[Relationship.Decision_id]")
    

    def __repr__(self):
        return f"Decision(id={self.id},description={self.description},OptionList_id={self.OptionList_id},RelationshipType_id={self.RelationshipType_id},controls_id={self.controls_id},)"



    


class ControlDetail(Base):
    """
    A single control requirement and its inline / referenced configuration.
    """
    __tablename__ = 'ControlDetail'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    requirement_url = Column(Text(), nullable=False )
    config_url = Column(Text())
    config = Column(Text())
    

    def __repr__(self):
        return f"ControlDetail(id={self.id},requirement_url={self.requirement_url},config_url={self.config_url},config={self.config},)"



    


class Control(Base):
    """
    A named control attached to an architecture element.
    """
    __tablename__ = 'Control'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    

    def __repr__(self):
        return f"Control(id={self.id},)"



    


class ControlRequirement(Base):
    """
    Domain-defined control requirement that controls can reference.
    """
    __tablename__ = 'ControlRequirement'

    control_id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    

    def __repr__(self):
        return f"ControlRequirement(control_id={self.control_id},name={self.name},description={self.description},)"



    


class Decorator(Base):
    """
    Cross-cutting annotation attached to nodes, relationships, or flows.
    """
    __tablename__ = 'Decorator'

    unique_id = Column(Text(), primary_key=True, nullable=False )
    type = Column(Text(), nullable=False )
    data = Column(Text(), nullable=False )
    
    
    target_rel = relationship( "DecoratorTarget" )
    target = association_proxy("target_rel", "target",
                                  creator=lambda x_: DecoratorTarget(target=x_))
    
    
    applies_to_rel = relationship( "DecoratorAppliesTo" )
    applies_to = association_proxy("applies_to_rel", "applies_to",
                                  creator=lambda x_: DecoratorAppliesTo(applies_to=x_))
    

    def __repr__(self):
        return f"Decorator(unique_id={self.unique_id},type={self.type},data={self.data},)"



    


class EvidenceDocument(Base):
    """
    Top-level CALM evidence document linking control configurations to evidence artefacts.
    """
    __tablename__ = 'EvidenceDocument'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    evidence = Column(Text(), nullable=False )
    

    def __repr__(self):
        return f"EvidenceDocument(id={self.id},evidence={self.evidence},)"



    


class Transition(Base):
    """
    A single step in a flow, anchored on a relationship.
    """
    __tablename__ = 'Transition'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    relationship_unique_id = Column(Text(), nullable=False )
    sequence_number = Column(Integer(), nullable=False )
    description = Column(Text(), nullable=False )
    direction = Column(Enum('source_to_destination', 'destination_to_source', name='TransitionDirection'))
    Flow_unique_id = Column(Text(), ForeignKey('Flow.unique_id'))
    

    def __repr__(self):
        return f"Transition(id={self.id},relationship_unique_id={self.relationship_unique_id},sequence_number={self.sequence_number},description={self.description},direction={self.direction},Flow_unique_id={self.Flow_unique_id},)"



    


class Flow(Base):
    """
    Business flow mapped onto architecture relationships.
    """
    __tablename__ = 'Flow'

    unique_id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    requirement_url = Column(Text())
    metadata = Column(Text())
    Architecture_id = Column(Integer(), ForeignKey('Architecture.id'))
    controls_id = Column(Integer(), ForeignKey('Control.id'))
    controls = relationship("Control", uselist=False, foreign_keys=[controls_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='Flow', source_slot='transitions', mapping_type=None, target_class='Transition', target_slot='Flow_unique_id', join_class=None, uses_join_table=None, multivalued=False)
    transitions = relationship( "Transition", foreign_keys="[Transition.Flow_unique_id]")
    

    def __repr__(self):
        return f"Flow(unique_id={self.unique_id},name={self.name},description={self.description},requirement_url={self.requirement_url},metadata={self.metadata},Architecture_id={self.Architecture_id},controls_id={self.controls_id},)"



    


class InterfaceDefinition(Base):
    """
    Modular interface definition referencing an external schema.
    """
    __tablename__ = 'InterfaceDefinition'

    unique_id = Column(Text(), primary_key=True, nullable=False )
    definition_url = Column(Text(), nullable=False )
    config = Column(Text(), nullable=False )
    Node_unique_id = Column(Text(), ForeignKey('Node.unique_id'))
    NodeInterface_id = Column(Integer(), ForeignKey('NodeInterface.id'))
    NodeMoment_unique_id = Column(Text(), ForeignKey('NodeMoment.unique_id'))
    

    def __repr__(self):
        return f"InterfaceDefinition(unique_id={self.unique_id},definition_url={self.definition_url},config={self.config},Node_unique_id={self.Node_unique_id},NodeInterface_id={self.NodeInterface_id},NodeMoment_unique_id={self.NodeMoment_unique_id},)"



    


class InterfaceType(Base):
    """
    Inline (free-form) interface definition keyed by unique-id.
    """
    __tablename__ = 'InterfaceType'

    unique_id = Column(Text(), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"InterfaceType(unique_id={self.unique_id},)"



    


class NodeInterface(Base):
    """
    Reference to one or more interfaces exposed by a node.
    """
    __tablename__ = 'NodeInterface'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    node = Column(Text(), nullable=False )
    
    
    # One-To-Many: OneToAnyMapping(source_class='NodeInterface', source_slot='interfaces', mapping_type=None, target_class='InterfaceDefinition', target_slot='NodeInterface_id', join_class=None, uses_join_table=None, multivalued=False)
    interfaces = relationship( "InterfaceDefinition", foreign_keys="[InterfaceDefinition.NodeInterface_id]")
    

    def __repr__(self):
        return f"NodeInterface(id={self.id},node={self.node},)"



    


class Timeline(Base):
    """
    CALM timeline document capturing architecture moments over time.
    """
    __tablename__ = 'Timeline'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    current_moment = Column(Text())
    metadata = Column(Text())
    
    
    moments_rel = relationship( "TimelineMoments" )
    moments = association_proxy("moments_rel", "moments",
                                  creator=lambda x_: TimelineMoments(moments=x_))
    

    def __repr__(self):
        return f"Timeline(id={self.id},current_moment={self.current_moment},metadata={self.metadata},)"



    


class TimeUnit(Base):
    """
    A quantity of time expressed as a numeric value and a unit.
    """
    __tablename__ = 'TimeUnit'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    unit = Column(Enum('nanoseconds', 'microseconds', 'milliseconds', 'seconds', 'minutes', 'hours', 'days', 'weeks', 'months', 'quarters', 'years', name='TimeUnitName'), nullable=False )
    value = Column(Float(), nullable=False )
    

    def __repr__(self):
        return f"TimeUnit(id={self.id},unit={self.unit},value={self.value},)"



    


class RateUnit(Base):
    """
    A rate (count per time unit), e.g. operations per second.
    """
    __tablename__ = 'RateUnit'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    rate = Column(Float(), nullable=False )
    per = Column(Enum('nanosecond', 'microsecond', 'millisecond', 'second', 'minute', 'hour', 'day', 'week', 'month', 'quarter', 'year', name='RatePerUnit'), nullable=False )
    

    def __repr__(self):
        return f"RateUnit(id={self.id},rate={self.rate},per={self.per},)"



    


class OptionList(Base):
    """
    Wrapper around the list of ``Decision`` alternatives in an options relationship.
    """
    __tablename__ = 'OptionList'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    
    
    # One-To-Many: OneToAnyMapping(source_class='OptionList', source_slot='decisions', mapping_type=None, target_class='Decision', target_slot='OptionList_id', join_class=None, uses_join_table=None, multivalued=False)
    decisions = relationship( "Decision", foreign_keys="[Decision.OptionList_id]")
    

    def __repr__(self):
        return f"OptionList(id={self.id},)"



    


class RelationshipType(Base):
    """
    Tagged-union container for the variant body of a relationship. Exactly one of ``interacts``, ``connects``, ``deployed_in``, ``composed_of``, ``options`` is populated; see ``RelationshipKind`` for the discriminator values.
    """
    __tablename__ = 'RelationshipType'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    interacts_id = Column(Integer(), ForeignKey('InteractsRelationship.id'))
    interacts = relationship("InteractsRelationship", uselist=False, foreign_keys=[interacts_id])
    connects_id = Column(Integer(), ForeignKey('ConnectsRelationship.id'))
    connects = relationship("ConnectsRelationship", uselist=False, foreign_keys=[connects_id])
    deployed_in_id = Column(Integer(), ForeignKey('DeployedInRelationship.id'))
    deployed_in = relationship("DeployedInRelationship", uselist=False, foreign_keys=[deployed_in_id])
    composed_of_id = Column(Integer(), ForeignKey('ComposedOfRelationship.id'))
    composed_of = relationship("ComposedOfRelationship", uselist=False, foreign_keys=[composed_of_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='RelationshipType', source_slot='options', mapping_type=None, target_class='Decision', target_slot='RelationshipType_id', join_class=None, uses_join_table=None, multivalued=False)
    options = relationship( "Decision", foreign_keys="[Decision.RelationshipType_id]")
    

    def __repr__(self):
        return f"RelationshipType(id={self.id},interacts_id={self.interacts_id},connects_id={self.connects_id},deployed_in_id={self.deployed_in_id},composed_of_id={self.composed_of_id},)"



    


class ArchitectureAdrs(Base):
    """
    None
    """
    __tablename__ = 'Architecture_adrs'

    Architecture_id = Column(Integer(), ForeignKey('Architecture.id'), primary_key=True)
    adrs = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Architecture_adrs(Architecture_id={self.Architecture_id},adrs={self.adrs},)"



    


class InteractsRelationshipNodes(Base):
    """
    None
    """
    __tablename__ = 'InteractsRelationship_nodes'

    InteractsRelationship_id = Column(Integer(), ForeignKey('InteractsRelationship.id'), primary_key=True)
    nodes_unique_id = Column(Text(), ForeignKey('Node.unique_id'), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"InteractsRelationship_nodes(InteractsRelationship_id={self.InteractsRelationship_id},nodes_unique_id={self.nodes_unique_id},)"



    


class DeployedInRelationshipNodes(Base):
    """
    None
    """
    __tablename__ = 'DeployedInRelationship_nodes'

    DeployedInRelationship_id = Column(Integer(), ForeignKey('DeployedInRelationship.id'), primary_key=True)
    nodes_unique_id = Column(Text(), ForeignKey('Node.unique_id'), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"DeployedInRelationship_nodes(DeployedInRelationship_id={self.DeployedInRelationship_id},nodes_unique_id={self.nodes_unique_id},)"



    


class ComposedOfRelationshipNodes(Base):
    """
    None
    """
    __tablename__ = 'ComposedOfRelationship_nodes'

    ComposedOfRelationship_id = Column(Integer(), ForeignKey('ComposedOfRelationship.id'), primary_key=True)
    nodes_unique_id = Column(Text(), ForeignKey('Node.unique_id'), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"ComposedOfRelationship_nodes(ComposedOfRelationship_id={self.ComposedOfRelationship_id},nodes_unique_id={self.nodes_unique_id},)"



    


class DecoratorTarget(Base):
    """
    None
    """
    __tablename__ = 'Decorator_target'

    Decorator_unique_id = Column(Text(), ForeignKey('Decorator.unique_id'), primary_key=True)
    target = Column(Text(), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"Decorator_target(Decorator_unique_id={self.Decorator_unique_id},target={self.target},)"



    


class DecoratorAppliesTo(Base):
    """
    None
    """
    __tablename__ = 'Decorator_applies_to'

    Decorator_unique_id = Column(Text(), ForeignKey('Decorator.unique_id'), primary_key=True)
    applies_to = Column(Text(), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"Decorator_applies_to(Decorator_unique_id={self.Decorator_unique_id},applies_to={self.applies_to},)"



    


class TimelineMoments(Base):
    """
    None
    """
    __tablename__ = 'Timeline_moments'

    Timeline_id = Column(Integer(), ForeignKey('Timeline.id'), primary_key=True)
    moments = Column(Text(), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"Timeline_moments(Timeline_id={self.Timeline_id},moments={self.moments},)"



    


class NodeMomentAdrs(Base):
    """
    None
    """
    __tablename__ = 'NodeMoment_adrs'

    NodeMoment_unique_id = Column(Text(), ForeignKey('NodeMoment.unique_id'), primary_key=True)
    adrs = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"NodeMoment_adrs(NodeMoment_unique_id={self.NodeMoment_unique_id},adrs={self.adrs},)"



    


class NodeMoment(Node):
    """
    An architecture moment - a point-in-time snapshot of the architecture.
    """
    __tablename__ = 'NodeMoment'

    unique_id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text(), nullable=False )
    metadata = Column(Text())
    node_type = Column(Enum('actor', 'ecosystem', 'system', 'service', 'database', 'network', 'ldap', 'webclient', 'data_asset', name='NodeType'), nullable=False )
    valid_from = Column(Date())
    details = Column(Text(), nullable=False )
    controls_id = Column(Integer(), ForeignKey('Control.id'))
    controls = relationship("Control", uselist=False, foreign_keys=[controls_id])
    
    
    adrs_rel = relationship( "NodeMomentAdrs" )
    adrs = association_proxy("adrs_rel", "adrs",
                                  creator=lambda x_: NodeMomentAdrs(adrs=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='NodeMoment', source_slot='interfaces', mapping_type=None, target_class='InterfaceDefinition', target_slot='NodeMoment_unique_id', join_class=None, uses_join_table=None, multivalued=False)
    interfaces = relationship( "InterfaceDefinition", foreign_keys="[InterfaceDefinition.NodeMoment_unique_id]")
    

    def __repr__(self):
        return f"NodeMoment(unique_id={self.unique_id},name={self.name},description={self.description},metadata={self.metadata},node_type={self.node_type},valid_from={self.valid_from},details={self.details},controls_id={self.controls_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


