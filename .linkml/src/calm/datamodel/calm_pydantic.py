from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.12.0"
version = "1.3"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'annotations': {'upstream_commit': {'tag': 'upstream_commit',
                                         'value': '47e2a41a0e1e5e9fe639b30ce2adae8c4abc5b6d'},
                     'upstream_license': {'tag': 'upstream_license',
                                          'value': 'Apache-2.0'},
                     'upstream_release_date': {'tag': 'upstream_release_date',
                                               'value': '2026-10-24'},
                     'upstream_tag': {'tag': 'upstream_tag', 'value': 'v1.3'}},
     'comments': ['A key with a hyphen, such as unique-id, is the alias of a slot '
                  "named with an underscore. scripts/calm_meta.py writes CALM's "
                  'files with the aliases as keys, which plain gen-json-schema '
                  'does only with --preserve-names.',
                  'A reference to a node, relationship or moment is its unique-id, '
                  'a string, as CALM gives it. No slot is an identifier: '
                  "gen-python in linkml 1.12.1 names an identifier's type from its "
                  'alias, and the hyphen in unique-id makes that name invalid '
                  'Python.',
                  "calm.json and calm-timeline.json declare CALM's vocabulary "
                  "beside JSON Schema's own and hold no definition, so no module "
                  'renders them; the build copies them from upstream/.'],
     'default_prefix': 'calm',
     'default_range': 'string',
     'description': 'A LinkML model of CALM 1.3, the Common Architecture Language '
                    "Model of FINOS's Architecture as Code project. Each module "
                    "renders one file of the CALM Meta Schema and keeps CALM's "
                    "keys, so a CALM document validates here unchanged, and CALM's "
                    'JSON Schema files can be generated from the model.',
     'id': 'https://w3id.org/lmodel/calm',
     'imports': ['linkml:types',
                 'calm_control',
                 'calm_interface',
                 'calm_core',
                 'calm_flow',
                 'calm_timeline',
                 'calm_decorators',
                 'calm_evidence',
                 'calm_control_requirement',
                 'calm_units'],
     'keywords': ['architecture as code', 'software architecture', 'CALM', 'FINOS'],
     'license': 'Apache-2.0',
     'name': 'calm',
     'prefixes': {'calm': {'prefix_prefix': 'calm',
                           'prefix_reference': 'https://w3id.org/lmodel/calm/'},
                  'calm_meta': {'prefix_prefix': 'calm_meta',
                                'prefix_reference': 'https://calm.finos.org/release/1.3/meta/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'see_also': ['https://lmodel.github.io/calm',
                  'https://calm.finos.org/',
                  'https://github.com/finos/calm-schema'],
     'source': 'https://github.com/finos/calm-schema/tree/47e2a41a0e1e5e9fe639b30ce2adae8c4abc5b6d/schema',
     'source_file': 'src/calm/schema/calm.yaml',
     'title': 'FINOS CALM'} )

class CalmProtocol(str, Enum):
    """
    The protocol a relationship uses.
    """
    HTTP = "HTTP"
    """
    Hypertext Transfer Protocol.
    """
    HTTPS = "HTTPS"
    """
    HTTP over TLS.
    """
    FTP = "FTP"
    """
    File Transfer Protocol.
    """
    SFTP = "SFTP"
    """
    SSH File Transfer Protocol.
    """
    JDBC = "JDBC"
    """
    Java Database Connectivity.
    """
    WebSocket = "WebSocket"
    """
    The WebSocket protocol.
    """
    SocketIO = "SocketIO"
    """
    The Socket.IO protocol.
    """
    LDAP = "LDAP"
    """
    Lightweight Directory Access Protocol.
    """
    AMQP = "AMQP"
    """
    Advanced Message Queuing Protocol.
    """
    TLS = "TLS"
    """
    Transport Layer Security.
    """
    mTLS = "mTLS"
    """
    TLS in which both ends present a certificate.
    """
    TCP = "TCP"
    """
    Transmission Control Protocol.
    """


class CalmNodeTypeDefinition(str, Enum):
    """
    CALM's built-in node types. A node may also name a type of its own, so the build publishes this list open to any other string.
    """
    actor = "actor"
    """
    A person or system outside the architecture that acts on it.
    """
    ecosystem = "ecosystem"
    """
    A group of systems that work together.
    """
    system = "system"
    """
    A system made of other nodes.
    """
    service = "service"
    """
    A service that runs in the architecture.
    """
    database = "database"
    """
    A store of data.
    """
    network = "network"
    """
    A network that nodes are deployed in.
    """
    ldap = "ldap"
    """
    A directory service reached over LDAP.
    """
    webclient = "webclient"
    """
    A client that runs in a web browser.
    """
    data_asset = "data-asset"
    """
    A body of data the architecture holds or moves.
    """


class CalmTransitionDirection(str, Enum):
    """
    The direction of a transition along its relationship.
    """
    source_to_destination = "source-to-destination"
    """
    From the relationship's source to its destination.
    """
    destination_to_source = "destination-to-source"
    """
    From the relationship's destination back to its source.
    """


class CalmDecoratorTargetType(str, Enum):
    """
    The kinds of CALM document a decorator can target.
    """
    architecture = "architecture"
    """
    An architecture document.
    """


class CalmTimeUnitName(str, Enum):
    """
    The units a time unit counts in.
    """
    nanoseconds = "nanoseconds"
    """
    Billionths of a second.
    """
    microseconds = "microseconds"
    """
    Millionths of a second.
    """
    milliseconds = "milliseconds"
    """
    Thousandths of a second.
    """
    seconds = "seconds"
    """
    Seconds.
    """
    minutes = "minutes"
    """
    Minutes.
    """
    hours = "hours"
    """
    Hours.
    """
    days = "days"
    """
    Days.
    """
    weeks = "weeks"
    """
    Weeks.
    """
    months = "months"
    """
    Calendar months.
    """
    quarters = "quarters"
    """
    Quarters of a year.
    """
    years = "years"
    """
    Years.
    """


class CalmRateInterval(str, Enum):
    """
    The interval a rate is counted over.
    """
    nanosecond = "nanosecond"
    """
    Per billionth of a second.
    """
    microsecond = "microsecond"
    """
    Per millionth of a second.
    """
    millisecond = "millisecond"
    """
    Per thousandth of a second.
    """
    second = "second"
    """
    Per second.
    """
    minute = "minute"
    """
    Per minute.
    """
    hour = "hour"
    """
    Per hour.
    """
    day = "day"
    """
    Per day.
    """
    week = "week"
    """
    Per week.
    """
    month = "month"
    """
    Per calendar month.
    """
    quarter = "quarter"
    """
    Per quarter of a year.
    """
    year = "year"
    """
    Per year.
    """



class CalmControls(ConfiguredBaseModel):
    """
    The controls that apply to an architecture element, each under a key of letters, digits and hyphens.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['CALM states the key pattern with patternProperties, which '
                      'LinkML cannot state, so any key is accepted here. CALM itself '
                      'leaves a key outside the pattern unchecked.'],
         'exact_mappings': ['calm_meta:control.json#/defs/controls'],
         'extra_slots': {'range_expression': {'range': 'CalmControl'}},
         'from_schema': 'https://w3id.org/lmodel/calm/calm_control'})

    pass


class CalmControl(ConfiguredBaseModel):
    """
    One control in a controls map, with the requirements that define it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/calm/calm_control'})

    description: str = Field(default=..., description="""A description of a control and how it applies to a given architecture""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmControl',
                       'CalmNode',
                       'CalmRelationship',
                       'CalmDecision',
                       'CalmFlow',
                       'CalmTransition',
                       'CalmControlRequirement'],
         'slot_uri': 'schema:description'} })
    requirements: list[CalmControlDetail] = Field(default=..., description="""The requirements this control applies, each with its configuration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmControl']} })


class CalmControlDetail(ConfiguredBaseModel):
    """
    A control requirement this control applies, with its configuration given by address or inline, but not both.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['calm_meta:control.json#/defs/control-detail'],
         'exactly_one_of': [{'slot_conditions': {'config_url': {'name': 'config_url',
                                                                'value_presence': 'PRESENT'}}},
                            {'slot_conditions': {'config': {'name': 'config',
                                                            'value_presence': 'PRESENT'}}}],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/calm/calm_control'})

    requirement_url: str = Field(default=..., alias="requirement-url", description="""The requirement schema that specifies how a control should be defined""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmControlDetail', 'CalmFlow']} })
    config_url: Optional[str] = Field(default=None, alias="config-url", description="""The configuration of how the control requirement schema is met""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmControlDetail']} })
    config: Optional[CalmControlConfig] = Field(default=None, description="""Inline configuration of how the control requirement schema is met""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmControlDetail', 'CalmInterfaceDefinition']} })


class CalmControlConfig(ConfiguredBaseModel):
    """
    A configuration object, free in shape, that meets a control requirement.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/calm/calm_control'})

    pass


class CalmInterfaceDefinition(ConfiguredBaseModel):
    """
    A modular interface definition referencing an external schema
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['calm_meta:interface.json#/defs/interface-definition'],
         'from_schema': 'https://w3id.org/lmodel/calm/calm_interface'})

    unique_id: str = Field(default=..., alias="unique-id", description="""Unique identifier for this interface instance""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmInterfaceDefinition',
                       'CalmInterfaceType',
                       'CalmNode',
                       'CalmRelationship',
                       'CalmFlow',
                       'CalmDecorator',
                       'CalmEvidence']} })
    definition_url: str = Field(default=..., alias="definition-url", description="""URI of the external schema this interface configuration conforms to""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmInterfaceDefinition']} })
    config: CalmInterfaceConfig = Field(default=..., description="""Inline configuration conforming to the external interface schema""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmControlDetail', 'CalmInterfaceDefinition']} })


class CalmInterfaceConfig(ConfiguredBaseModel):
    """
    A configuration object, free in shape, that an interface definition's schema checks.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/calm/calm_interface'})

    pass


class CalmInterfaceType(ConfiguredBaseModel):
    """
    An interface given by its own keys, such as a host and port, rather than by an external schema.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['calm_meta:interface.json#/defs/interface-type'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/calm/calm_interface'})

    unique_id: str = Field(default=..., alias="unique-id", description="""The interface's identifier, unique within the architecture.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmInterfaceDefinition',
                       'CalmInterfaceType',
                       'CalmNode',
                       'CalmRelationship',
                       'CalmFlow',
                       'CalmDecorator',
                       'CalmEvidence']} })


class CalmNodeInterface(ConfiguredBaseModel):
    """
    One end of a connection, naming a node and, optionally, which of its interfaces.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['calm_meta:interface.json#/defs/node-interface'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/calm/calm_interface'})

    node: str = Field(default=..., description="""The unique-id of the node at this end.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNodeInterface']} })
    interfaces: Optional[list[str]] = Field(default=None, description="""The unique-ids of the node's interfaces this end uses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNodeInterface', 'CalmNode']} })


class CalmNode(ConfiguredBaseModel):
    """
    A component of the architecture, such as a system, service, database or actor, with its interfaces and controls.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['calm_meta:core.json#/defs/node'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/calm/calm_core'})

    unique_id: str = Field(default=..., alias="unique-id", description="""The node's identifier, unique within the architecture.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmInterfaceDefinition',
                       'CalmInterfaceType',
                       'CalmNode',
                       'CalmRelationship',
                       'CalmFlow',
                       'CalmDecorator',
                       'CalmEvidence']} })
    node_type: Union[CalmNodeTypeDefinition, str] = Field(default=..., alias="node-type", description="""What kind of node this is, one of CALM's built-in types or any other name.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'CalmNodeTypeDefinition'}, {'range': 'string'}],
         'domain_of': ['CalmNode']} })
    name: str = Field(default=..., description="""The node's name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNode', 'CalmFlow', 'CalmControlRequirement'],
         'slot_uri': 'schema:name'} })
    description: str = Field(default=..., description="""What the node is and does.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmControl',
                       'CalmNode',
                       'CalmRelationship',
                       'CalmDecision',
                       'CalmFlow',
                       'CalmTransition',
                       'CalmControlRequirement'],
         'slot_uri': 'schema:description'} })
    details: Optional[CalmNodeDetails] = Field(default=None, description="""Where a more detailed architecture of this node is, and the pattern it must follow.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNode']} })
    interfaces: Optional[list[Union[CalmInterfaceDefinition, CalmInterfaceType]]] = Field(default=None, description="""The interfaces the node exposes.""", json_schema_extra = { "linkml_meta": {'any_of': [{'inlined': True, 'range': 'CalmInterfaceDefinition'},
                    {'inlined': True, 'range': 'CalmInterfaceType'}],
         'domain_of': ['CalmNodeInterface', 'CalmNode']} })
    controls: Optional[CalmControls] = Field(default=None, description="""The controls that apply to this node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNode',
                       'CalmRelationship',
                       'CalmDecision',
                       'CalmFlow',
                       'CalmArchitecture']} })
    metadata: Optional[Any] = Field(default=None, description="""Free-form metadata about this node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNode',
                       'CalmRelationship',
                       'CalmFlow',
                       'CalmTimeline',
                       'CalmArchitecture']} })


class CalmNodeDetails(ConfiguredBaseModel):
    """
    References from a node to a more detailed architecture and to the pattern it must follow.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/calm/calm_core'})

    detailed_architecture: Optional[str] = Field(default=None, alias="detailed-architecture", description="""The address of an architecture document that describes this node in detail.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNodeDetails']} })
    required_pattern: Optional[str] = Field(default=None, alias="required-pattern", description="""The address of a pattern that the detailed architecture must follow.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNodeDetails']} })


class CalmRelationship(ConfiguredBaseModel):
    """
    A link between nodes, of one of CALM's kinds, or a choice between options.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['calm_meta:core.json#/defs/relationship'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/calm/calm_core'})

    unique_id: str = Field(default=..., alias="unique-id", description="""The relationship's identifier, unique within the architecture.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmInterfaceDefinition',
                       'CalmInterfaceType',
                       'CalmNode',
                       'CalmRelationship',
                       'CalmFlow',
                       'CalmDecorator',
                       'CalmEvidence']} })
    description: Optional[str] = Field(default=None, description="""What the relationship is for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmControl',
                       'CalmNode',
                       'CalmRelationship',
                       'CalmDecision',
                       'CalmFlow',
                       'CalmTransition',
                       'CalmControlRequirement'],
         'slot_uri': 'schema:description'} })
    relationship_type: CalmRelationshipType = Field(default=..., alias="relationship-type", description="""The kind of the relationship and the nodes it links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmRelationship']} })
    protocol: Optional[CalmProtocol] = Field(default=None, description="""The protocol a connection uses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmRelationship']} })
    metadata: Optional[Any] = Field(default=None, description="""Free-form metadata about this relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNode',
                       'CalmRelationship',
                       'CalmFlow',
                       'CalmTimeline',
                       'CalmArchitecture']} })
    controls: Optional[CalmControls] = Field(default=None, description="""The controls that apply to this relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNode',
                       'CalmRelationship',
                       'CalmDecision',
                       'CalmFlow',
                       'CalmArchitecture']} })


class CalmRelationshipType(ConfiguredBaseModel):
    """
    The kind of a relationship, given by exactly one of its keys: interacts, connects, deployed-in, composed-of or options.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exactly_one_of': [{'slot_conditions': {'deployed_in': {'name': 'deployed_in',
                                                                 'value_presence': 'PRESENT'}}},
                            {'slot_conditions': {'composed_of': {'name': 'composed_of',
                                                                 'value_presence': 'PRESENT'}}},
                            {'slot_conditions': {'interacts': {'name': 'interacts',
                                                               'value_presence': 'PRESENT'}}},
                            {'slot_conditions': {'connects': {'name': 'connects',
                                                              'value_presence': 'PRESENT'}}},
                            {'slot_conditions': {'options': {'name': 'options',
                                                             'value_presence': 'PRESENT'}}}],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/calm/calm_core'})

    interacts: Optional[CalmInteractsType] = Field(default=None, description="""An actor that interacts with nodes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmRelationshipType']} })
    connects: Optional[CalmConnectsType] = Field(default=None, description="""A connection from one node's interfaces to another's.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmRelationshipType']} })
    deployed_in: Optional[CalmDeployedInType] = Field(default=None, alias="deployed-in", description="""Nodes deployed in a container node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmRelationshipType']} })
    composed_of: Optional[CalmComposedOfType] = Field(default=None, alias="composed-of", description="""Nodes that make up a container node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmRelationshipType']} })
    options: Optional[list[CalmDecision]] = Field(default=None, description="""Decisions between options, each naming the nodes and relationships it would add.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmRelationshipType']} })


class CalmInteractsType(ConfiguredBaseModel):
    """
    A relationship in which an actor interacts with nodes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['calm_meta:core.json#/defs/interacts-type'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/calm/calm_core'})

    actor: str = Field(default=..., description="""The unique-id of the node that acts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmInteractsType']} })
    nodes: list[str] = Field(default=..., description="""The unique-ids of the nodes it interacts with.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['CalmInteractsType',
                       'CalmDeployedInType',
                       'CalmComposedOfType',
                       'CalmDecision',
                       'CalmArchitecture']} })


class CalmConnectsType(ConfiguredBaseModel):
    """
    A relationship in which one node connects to another through their interfaces.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['calm_meta:core.json#/defs/connects-type'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/calm/calm_core'})

    source: CalmNodeInterface = Field(default=..., description="""The end that opens the connection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmConnectsType']} })
    destination: CalmNodeInterface = Field(default=..., description="""The end the connection reaches.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmConnectsType']} })


class CalmDeployedInType(ConfiguredBaseModel):
    """
    A relationship in which nodes are deployed in a container node.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['calm_meta:core.json#/defs/deployed-in-type'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/calm/calm_core'})

    container: str = Field(default=..., description="""The unique-id of the node the others are deployed in.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmDeployedInType', 'CalmComposedOfType']} })
    nodes: list[str] = Field(default=..., description="""The unique-ids of the deployed nodes.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['CalmInteractsType',
                       'CalmDeployedInType',
                       'CalmComposedOfType',
                       'CalmDecision',
                       'CalmArchitecture']} })


class CalmComposedOfType(ConfiguredBaseModel):
    """
    A relationship in which nodes make up a container node.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['calm_meta:core.json#/defs/composed-of-type'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/calm/calm_core'})

    container: str = Field(default=..., description="""The unique-id of the node the others make up.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmDeployedInType', 'CalmComposedOfType']} })
    nodes: list[str] = Field(default=..., description="""The unique-ids of the nodes it is made of.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['CalmInteractsType',
                       'CalmDeployedInType',
                       'CalmComposedOfType',
                       'CalmDecision',
                       'CalmArchitecture']} })


class CalmDecision(ConfiguredBaseModel):
    """
    One option of a choice, naming the nodes, relationships and controls it would add.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['calm_meta:core.json#/defs/decision'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/calm/calm_core'})

    description: str = Field(default=..., description="""What choosing this option means.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmControl',
                       'CalmNode',
                       'CalmRelationship',
                       'CalmDecision',
                       'CalmFlow',
                       'CalmTransition',
                       'CalmControlRequirement'],
         'slot_uri': 'schema:description'} })
    nodes: list[str] = Field(default=..., description="""The unique-ids of the nodes this option adds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmInteractsType',
                       'CalmDeployedInType',
                       'CalmComposedOfType',
                       'CalmDecision',
                       'CalmArchitecture']} })
    relationships: list[str] = Field(default=..., description="""The unique-ids of the relationships this option adds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmDecision', 'CalmArchitecture']} })
    controls: Optional[list[str]] = Field(default=None, description="""The keys of the controls this option adds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNode',
                       'CalmRelationship',
                       'CalmDecision',
                       'CalmFlow',
                       'CalmArchitecture']} })


class CalmFlow(ConfiguredBaseModel):
    """
    A business flow, as an ordered list of transitions across the architecture's relationships.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['calm_meta:flow.json#/defs/flow'],
         'from_schema': 'https://w3id.org/lmodel/calm/calm_flow'})

    unique_id: str = Field(default=..., alias="unique-id", description="""Unique identifier for the flow""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmInterfaceDefinition',
                       'CalmInterfaceType',
                       'CalmNode',
                       'CalmRelationship',
                       'CalmFlow',
                       'CalmDecorator',
                       'CalmEvidence']} })
    name: str = Field(default=..., description="""Descriptive name for the business flow""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNode', 'CalmFlow', 'CalmControlRequirement'],
         'slot_uri': 'schema:name'} })
    description: str = Field(default=..., description="""Detailed description of the flow's purpose""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmControl',
                       'CalmNode',
                       'CalmRelationship',
                       'CalmDecision',
                       'CalmFlow',
                       'CalmTransition',
                       'CalmControlRequirement'],
         'slot_uri': 'schema:description'} })
    requirement_url: Optional[str] = Field(default=None, alias="requirement-url", description="""Link to a detailed requirement document""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmControlDetail', 'CalmFlow']} })
    transitions: list[CalmTransition] = Field(default=..., description="""The steps of the flow, each across one relationship.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['CalmFlow']} })
    controls: Optional[CalmControls] = Field(default=None, description="""The controls that apply to this flow.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNode',
                       'CalmRelationship',
                       'CalmDecision',
                       'CalmFlow',
                       'CalmArchitecture']} })
    metadata: Optional[Any] = Field(default=None, description="""Free-form metadata about this flow.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNode',
                       'CalmRelationship',
                       'CalmFlow',
                       'CalmTimeline',
                       'CalmArchitecture']} })


class CalmTransition(ConfiguredBaseModel):
    """
    One step of a flow, across one relationship of the architecture.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['calm_meta:flow.json#/defs/transition'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/calm/calm_flow'})

    relationship_unique_id: str = Field(default=..., alias="relationship-unique-id", description="""Unique identifier for the relationship in the architecture""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmTransition']} })
    sequence_number: int = Field(default=..., alias="sequence-number", description="""Indicates the sequence of the relationship in the flow""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmTransition']} })
    description: str = Field(default=..., description="""Functional summary of what is happening in the transition""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmControl',
                       'CalmNode',
                       'CalmRelationship',
                       'CalmDecision',
                       'CalmFlow',
                       'CalmTransition',
                       'CalmControlRequirement'],
         'slot_uri': 'schema:description'} })
    direction: Optional[CalmTransitionDirection] = Field(default=CalmTransitionDirection("source-to-destination"), description="""Which way along the relationship the step goes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmTransition'], 'ifabsent': 'string(source-to-destination)'} })


class CalmTimeline(ConfiguredBaseModel):
    """
    A timeline document, listing the moments of an architecture and naming the current one.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['calm_meta:timeline.json'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/calm/calm_timeline'})

    current_moment: Optional[str] = Field(default=None, alias="current-moment", description="""The unique-id of the current architecture moment within the timeline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmTimeline']} })
    moments: list[CalmNodeMoment] = Field(default=..., description="""A list of significant architecture states or points in time, each represented as a 'moment'.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmTimeline']} })
    metadata: Optional[Any] = Field(default=None, description="""Free-form metadata about this timeline.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNode',
                       'CalmRelationship',
                       'CalmFlow',
                       'CalmTimeline',
                       'CalmArchitecture']} })


class CalmNodeMoment(CalmNode):
    """
    A moment of a timeline: a node of type moment, with no interfaces, whose details point to the architecture of that moment.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'all_of': [{'slot_conditions': {'node_type': {'equals_string': 'moment',
                                                       'name': 'node_type'}}},
                    {'slot_conditions': {'details': {'name': 'details',
                                                     'value_presence': 'PRESENT'}}},
                    {'slot_conditions': {'interfaces': {'name': 'interfaces',
                                                        'value_presence': 'ABSENT'}}}],
         'comments': ['The three conditions on inherited slots are class rules, not '
                      'slot_usage, because gen-shacl refuses equals_string on a slot '
                      'that also has any_of.'],
         'exact_mappings': ['calm_meta:timeline.json#/defs/node-moment'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/calm/calm_timeline'})

    valid_from: Optional[date] = Field(default=None, alias="valid-from", description="""The date when this architecture moment came into effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNodeMoment']} })
    adrs: Optional[list[str]] = Field(default=None, description="""External links to ADRs (Architecture Decision Records) or similar documents that provide context or decisions related to why the architecture changed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNodeMoment', 'CalmArchitecture']} })
    unique_id: str = Field(default=..., alias="unique-id", description="""The node's identifier, unique within the architecture.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmInterfaceDefinition',
                       'CalmInterfaceType',
                       'CalmNode',
                       'CalmRelationship',
                       'CalmFlow',
                       'CalmDecorator',
                       'CalmEvidence']} })
    node_type: Union[CalmNodeTypeDefinition, str] = Field(default=..., alias="node-type", description="""What kind of node this is, one of CALM's built-in types or any other name.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'CalmNodeTypeDefinition'}, {'range': 'string'}],
         'domain_of': ['CalmNode']} })
    name: str = Field(default=..., description="""The node's name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNode', 'CalmFlow', 'CalmControlRequirement'],
         'slot_uri': 'schema:name'} })
    description: str = Field(default=..., description="""What the node is and does.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmControl',
                       'CalmNode',
                       'CalmRelationship',
                       'CalmDecision',
                       'CalmFlow',
                       'CalmTransition',
                       'CalmControlRequirement'],
         'slot_uri': 'schema:description'} })
    details: Optional[CalmNodeDetails] = Field(default=None, description="""Where a more detailed architecture of this node is, and the pattern it must follow.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNode']} })
    interfaces: Optional[list[Union[CalmInterfaceDefinition, CalmInterfaceType]]] = Field(default=None, description="""The interfaces the node exposes.""", json_schema_extra = { "linkml_meta": {'any_of': [{'inlined': True, 'range': 'CalmInterfaceDefinition'},
                    {'inlined': True, 'range': 'CalmInterfaceType'}],
         'domain_of': ['CalmNodeInterface', 'CalmNode']} })
    controls: Optional[CalmControls] = Field(default=None, description="""The controls that apply to this node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNode',
                       'CalmRelationship',
                       'CalmDecision',
                       'CalmFlow',
                       'CalmArchitecture']} })
    metadata: Optional[Any] = Field(default=None, description="""Free-form metadata about this node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNode',
                       'CalmRelationship',
                       'CalmFlow',
                       'CalmTimeline',
                       'CalmArchitecture']} })


class CalmDecorator(ConfiguredBaseModel):
    """
    Supplementary information about elements of one or more architectures, kept apart from the architectures themselves.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['calm_meta:decorators.json#/defs/decorator'],
         'from_schema': 'https://w3id.org/lmodel/calm/calm_decorators'})

    decorator_schema: Optional[str] = Field(default=None, description="""URI of the schema that this decorator conforms to, for example a decorator standard""", json_schema_extra = { "linkml_meta": {'aliases': ['$schema'],
         'comments': ["CALM's key is $schema, listed under aliases rather than as the "
                      "alias, because gen-python makes an alias the attribute's name "
                      'and $schema is no Python name. scripts/calm_meta.py writes the '
                      'key as $schema.'],
         'domain_of': ['CalmDecorator']} })
    unique_id: str = Field(default=..., alias="unique-id", description="""Unique identifier for this decorator""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmInterfaceDefinition',
                       'CalmInterfaceType',
                       'CalmNode',
                       'CalmRelationship',
                       'CalmFlow',
                       'CalmDecorator',
                       'CalmEvidence']} })
    type: str = Field(default=..., description="""Type of decorator - a free-form string identifying the decorator category""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmDecorator']} })
    target_type: Optional[list[CalmDecoratorTargetType]] = Field(default=None, alias="target-type", description="""Optional array of the types of CALM document that this decorator can target. The only type is architecture, because applies-to holds the unique-ids of architecture elements.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['CalmDecorator'], 'list_elements_unique': True} })
    target: list[str] = Field(default=..., description="""Array of file paths or URLs referencing the CALM architectures this decorator targets""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['CalmDecorator']} })
    applies_to: list[str] = Field(default=..., alias="applies-to", description="""Array of unique-ids referencing nodes, relationships, flows, or other architecture elements""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['CalmDecorator']} })
    data: CalmDecoratorData = Field(default=..., description="""Free-form JSON object containing the decorator's data""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmDecorator']} })


class CalmDecoratorData(ConfiguredBaseModel):
    """
    The decorator's data, an object free in shape.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['CALM requires at least one key, which LinkML cannot state, so '
                      'an empty object is accepted here.'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/calm/calm_decorators'})

    pass


class CalmEvidenceDocument(ConfiguredBaseModel):
    """
    An evidence document, which holds one piece of evidence for a control.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['calm_meta:evidence.json'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/calm/calm_evidence'})

    evidence: CalmEvidence = Field(default=..., description="""The evidence this document holds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmEvidenceDocument']} })


class CalmEvidence(ConfiguredBaseModel):
    """
    Evidence that a control's configuration is met, by the paths where it is kept.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/calm/calm_evidence'})

    unique_id: str = Field(default=..., alias="unique-id", description="""CALM unique-id for future linking and uniquely defining this evidence""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmInterfaceDefinition',
                       'CalmInterfaceType',
                       'CalmNode',
                       'CalmRelationship',
                       'CalmFlow',
                       'CalmDecorator',
                       'CalmEvidence']} })
    evidence_paths: list[str] = Field(default=..., alias="evidence-paths", description="""Paths to the evidence relating to a specific control""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmEvidence']} })
    control_config_url: str = Field(default=..., alias="control-config-url", description="""URI for the control configuration this evidence relates to""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmEvidence']} })


class CalmControlRequirement(ConfiguredBaseModel):
    """
    A control requirement: what a control must achieve, which a control detail's requirement-url points to.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['calm_meta:control-requirement.json'],
         'examples': [{'object': {'control-id': 'CR-001',
                                  'description': 'Ensure that access to sensitive '
                                                 'information is restricted.',
                                  'name': 'Access Control'}}],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/calm/calm_control_requirement'})

    control_id: str = Field(default=..., alias="control-id", description="""The unique identifier of this control, which has the potential to be used for linking evidence""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmControlRequirement']} })
    name: str = Field(default=..., description="""The name of the control requirement that provides contextual meaning within a given domain""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNode', 'CalmFlow', 'CalmControlRequirement'],
         'slot_uri': 'schema:name'} })
    description: str = Field(default=..., description="""A more detailed description of the control and information on what a developer needs to consider""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmControl',
                       'CalmNode',
                       'CalmRelationship',
                       'CalmDecision',
                       'CalmFlow',
                       'CalmTransition',
                       'CalmControlRequirement'],
         'slot_uri': 'schema:description'} })


class CalmTimeUnit(ConfiguredBaseModel):
    """
    A unit of time with a value and a unit type.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['calm_meta:units.json#/defs/time-unit'],
         'examples': [{'object': {'unit': 'seconds', 'value': 30}},
                      {'object': {'unit': 'minutes', 'value': 15}},
                      {'object': {'unit': 'hours', 'value': 1}},
                      {'object': {'unit': 'days', 'value': 7}}],
         'from_schema': 'https://w3id.org/lmodel/calm/calm_units'})

    unit: CalmTimeUnitName = Field(default=..., description="""The unit of time (e.g., seconds, minutes, hours).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmTimeUnit']} })
    value: float = Field(default=..., description="""The numeric value representing the amount of time.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['CalmTimeUnit']} })


class CalmRateUnit(ConfiguredBaseModel):
    """
    A unit representing a rate (e.g., operations per second).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['calm_meta:units.json#/defs/rate-unit'],
         'examples': [{'object': {'per': 'second', 'rate': 30}},
                      {'object': {'per': 'minute', 'rate': 1000}},
                      {'object': {'per': 'millisecond', 'rate': 5}}],
         'from_schema': 'https://w3id.org/lmodel/calm/calm_units'})

    rate: float = Field(default=..., description="""The numeric value representing the rate.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['CalmRateUnit']} })
    per: CalmRateInterval = Field(default=..., description="""The time unit defining the rate interval.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmRateUnit']} })


class CalmArchitecture(ConfiguredBaseModel):
    """
    A CALM architecture document: the nodes of a system, the relationships between them, its business flows, and the controls that apply to it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['An architecture is itself a JSON Schema document, so it may '
                      "carry JSON Schema's keys, such as $schema, beside CALM's own."],
         'exact_mappings': ['calm_meta:core.json'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/calm',
         'tree_root': True})

    nodes: Optional[list[CalmNode]] = Field(default=None, description="""The components of the architecture.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmInteractsType',
                       'CalmDeployedInType',
                       'CalmComposedOfType',
                       'CalmDecision',
                       'CalmArchitecture']} })
    relationships: Optional[list[CalmRelationship]] = Field(default=None, description="""The links between the architecture's nodes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmDecision', 'CalmArchitecture']} })
    metadata: Optional[Any] = Field(default=None, description="""Free-form metadata about the architecture.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNode',
                       'CalmRelationship',
                       'CalmFlow',
                       'CalmTimeline',
                       'CalmArchitecture']} })
    controls: Optional[CalmControls] = Field(default=None, description="""The controls that apply to the whole architecture.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNode',
                       'CalmRelationship',
                       'CalmDecision',
                       'CalmFlow',
                       'CalmArchitecture']} })
    flows: Optional[list[CalmFlow]] = Field(default=None, description="""The business flows that run across the architecture.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmArchitecture']} })
    adrs: Optional[list[str]] = Field(default=None, description="""External links to ADRs (Architecture Decision Records) or similar documents that provide context or decisions related to the architecture. These can be URLs or references to internal documentation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CalmNodeMoment', 'CalmArchitecture']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
CalmControls.model_rebuild()
CalmControl.model_rebuild()
CalmControlDetail.model_rebuild()
CalmControlConfig.model_rebuild()
CalmInterfaceDefinition.model_rebuild()
CalmInterfaceConfig.model_rebuild()
CalmInterfaceType.model_rebuild()
CalmNodeInterface.model_rebuild()
CalmNode.model_rebuild()
CalmNodeDetails.model_rebuild()
CalmRelationship.model_rebuild()
CalmRelationshipType.model_rebuild()
CalmInteractsType.model_rebuild()
CalmConnectsType.model_rebuild()
CalmDeployedInType.model_rebuild()
CalmComposedOfType.model_rebuild()
CalmDecision.model_rebuild()
CalmFlow.model_rebuild()
CalmTransition.model_rebuild()
CalmTimeline.model_rebuild()
CalmNodeMoment.model_rebuild()
CalmDecorator.model_rebuild()
CalmDecoratorData.model_rebuild()
CalmEvidenceDocument.model_rebuild()
CalmEvidence.model_rebuild()
CalmControlRequirement.model_rebuild()
CalmTimeUnit.model_rebuild()
CalmRateUnit.model_rebuild()
CalmArchitecture.model_rebuild()
