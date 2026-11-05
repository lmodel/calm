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


metamodel_version = "1.11.0"
version = "1.2"


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


linkml_meta = LinkMLMeta({'default_prefix': 'calm',
     'default_range': 'string',
     'description': 'LinkML representation of the FINOS Common Architecture '
                    'Language Model (CALM) 1.2 specification. CALM is a '
                    'declarative, JSON-based modeling language for describing '
                    'complex software architectures (nodes, relationships, '
                    'controls, flows, decorators, timelines, evidence, and units). '
                    'This LinkML schema is generated from the CALM JSON-Schema '
                    'meta files.',
     'id': 'https://w3id.org/lmodel/calm',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'calm',
     'prefixes': {'ai_governance_framework': {'prefix_prefix': 'ai_governance_framework',
                                              'prefix_reference': 'https://w3id.org/lmodel/ai-governance-framework/'},
                  'attack': {'prefix_prefix': 'attack',
                             'prefix_reference': 'https://w3id.org/lmodel/attack/'},
                  'calm': {'prefix_prefix': 'calm',
                           'prefix_reference': 'https://w3id.org/lmodel/calm/'},
                  'capec': {'prefix_prefix': 'capec',
                            'prefix_reference': 'https://w3id.org/lmodel/capec/'},
                  'cis_controls': {'prefix_prefix': 'cis_controls',
                                   'prefix_reference': 'https://w3id.org/lmodel/cis-controls/'},
                  'dct': {'prefix_prefix': 'dct',
                          'prefix_reference': 'http://purl.org/dc/terms/'},
                  'dpv': {'prefix_prefix': 'dpv',
                          'prefix_reference': 'https://w3id.org/lmodel/dpv/'},
                  'finos_calm': {'prefix_prefix': 'finos_calm',
                                 'prefix_reference': 'https://calm.finos.org/release/1.2/meta/'},
                  'fluxnova_bpmn_platform': {'prefix_prefix': 'fluxnova_bpmn_platform',
                                             'prefix_reference': 'https://w3id.org/lmodel/fluxnova-bpm-platform/'},
                  'gist': {'prefix_prefix': 'gist',
                           'prefix_reference': 'https://w3id.org/lmodel/gist/'},
                  'iso27001': {'prefix_prefix': 'iso27001',
                               'prefix_reference': 'https://w3id.org/lmodel/iso27001/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nist_csf_v2': {'prefix_prefix': 'nist_csf_v2',
                                  'prefix_reference': 'https://w3id.org/lmodel/nist-csf-v2/'},
                  'nist_sp_800_53': {'prefix_prefix': 'nist_sp_800_53',
                                     'prefix_reference': 'https://w3id.org/lmodel/nist-sp-800-53/'},
                  'ocsf': {'prefix_prefix': 'ocsf',
                           'prefix_reference': 'https://w3id.org/lmodel/ocsf/'},
                  'oscal': {'prefix_prefix': 'oscal',
                            'prefix_reference': 'https://w3id.org/lmodel/oscal/'},
                  'owl': {'prefix_prefix': 'owl',
                          'prefix_reference': 'http://www.w3.org/2002/07/owl#'},
                  'prov': {'prefix_prefix': 'prov',
                           'prefix_reference': 'http://www.w3.org/ns/prov#'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'rdfs': {'prefix_prefix': 'rdfs',
                           'prefix_reference': 'http://www.w3.org/2000/01/rdf-schema#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'},
                  'stix': {'prefix_prefix': 'stix',
                           'prefix_reference': 'https://w3id.org/lmodel/stix/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://calm.finos.org/',
                  'https://github.com/finos/architecture-as-code'],
     'source': 'https://calm.finos.org/release/1.2/meta/calm.json',
     'source_file': 'src/calm/schema/calm.yaml',
     'subsets': {'control_framework': {'description': 'Control framework: '
                                                      'controls, requirements, '
                                                      'evidence.',
                                       'from_schema': 'https://w3id.org/lmodel/calm',
                                       'name': 'control_framework'},
                 'core': {'description': 'Core architecture vocabulary (nodes, '
                                         'relationships, decisions).',
                          'from_schema': 'https://w3id.org/lmodel/calm',
                          'name': 'core'},
                 'decorators': {'description': 'Cross-cutting decorators that '
                                               'annotate elements.',
                                'from_schema': 'https://w3id.org/lmodel/calm',
                                'name': 'decorators'},
                 'flow_modeling': {'description': 'Business flow modeling: flows '
                                                  'and transitions.',
                                   'from_schema': 'https://w3id.org/lmodel/calm',
                                   'name': 'flow_modeling'},
                 'interface_defs': {'description': 'Interface definitions exposed '
                                                   'by nodes.',
                                    'from_schema': 'https://w3id.org/lmodel/calm',
                                    'name': 'interface_defs'},
                 'timeline': {'description': 'Time-based architecture snapshots '
                                             '(moments).',
                              'from_schema': 'https://w3id.org/lmodel/calm',
                              'name': 'timeline'},
                 'units': {'description': 'Quantity and rate unit primitives.',
                           'from_schema': 'https://w3id.org/lmodel/calm',
                           'name': 'units'}},
     'title': 'Common Architecture Language Model (CALM)',
     'types': {'CronExpression': {'base': 'str',
                                  'description': 'A Unix-style cron expression '
                                                 '(minute, hour, day, month, '
                                                 'weekday).',
                                  'from_schema': 'https://w3id.org/lmodel/calm',
                                  'name': 'CronExpression',
                                  'pattern': '^([0-5]?\\d)\\s([01]?\\d|2[0-3])\\s(3[01]|[12]\\d|0?[1-9])\\s(1[0-2]|0?[1-9])\\s([0-6])$',
                                  'uri': 'xsd:string'},
               'Metadata': {'base': 'str',
                            'description': 'Opaque key/value metadata payload. '
                                           'JSON-Schema allows either an object or '
                                           'an array of objects; in LinkML this is '
                                           'modeled as a permissive string type '
                                           'that downstream consumers parse as '
                                           'JSON.',
                            'from_schema': 'https://w3id.org/lmodel/calm',
                            'name': 'Metadata',
                            'uri': 'xsd:string'}}} )

class Protocol(str, Enum):
    """
    Wire-level protocol used by a relationship.
    """
    HTTP = "HTTP"
    """
    The HTTP protocol.
    """
    HTTPS = "HTTPS"
    """
    The HTTPS protocol.
    """
    FTP = "FTP"
    """
    The FTP protocol.
    """
    SFTP = "SFTP"
    """
    The SFTP protocol.
    """
    JDBC = "JDBC"
    """
    The JDBC protocol.
    """
    WebSocket = "WebSocket"
    """
    The WebSocket protocol.
    """
    SocketIO = "SocketIO"
    """
    The SocketIO protocol.
    """
    LDAP = "LDAP"
    """
    The LDAP protocol.
    """
    AMQP = "AMQP"
    """
    The AMQP protocol.
    """
    TLS = "TLS"
    """
    The TLS protocol.
    """
    mTLS = "mTLS"
    """
    The mTLS protocol.
    """
    TCP = "TCP"
    """
    The TCP protocol.
    """


class NodeType(str, Enum):
    """
    Category of architecture node. The CALM JSON-Schema allows arbitrary strings; this enum lists the canonical values plus an escape hatch via ``any_of`` on the slot.
    """
    actor = "actor"
    """
    A actor node.
    """
    ecosystem = "ecosystem"
    """
    A ecosystem node.
    """
    system = "system"
    """
    A system node.
    """
    service = "service"
    """
    A service node.
    """
    database = "database"
    """
    A database node.
    """
    network = "network"
    """
    A network node.
    """
    ldap = "ldap"
    """
    A ldap node.
    """
    webclient = "webclient"
    """
    A webclient node.
    """
    data_asset = "data_asset"
    """
    A data-asset node.
    """


class TimeUnitName(str, Enum):
    """
    Named unit of time used by ``TimeUnit``.
    """
    nanoseconds = "nanoseconds"
    """
    Time unit: nanoseconds.
    """
    microseconds = "microseconds"
    """
    Time unit: microseconds.
    """
    milliseconds = "milliseconds"
    """
    Time unit: milliseconds.
    """
    seconds = "seconds"
    """
    Time unit: seconds.
    """
    minutes = "minutes"
    """
    Time unit: minutes.
    """
    hours = "hours"
    """
    Time unit: hours.
    """
    days = "days"
    """
    Time unit: days.
    """
    weeks = "weeks"
    """
    Time unit: weeks.
    """
    months = "months"
    """
    Time unit: months.
    """
    quarters = "quarters"
    """
    Time unit: quarters.
    """
    years = "years"
    """
    Time unit: years.
    """


class RatePerUnit(str, Enum):
    """
    Time interval denominator used by ``RateUnit``.
    """
    nanosecond = "nanosecond"
    """
    Rate denominator: per nanosecond.
    """
    microsecond = "microsecond"
    """
    Rate denominator: per microsecond.
    """
    millisecond = "millisecond"
    """
    Rate denominator: per millisecond.
    """
    second = "second"
    """
    Rate denominator: per second.
    """
    minute = "minute"
    """
    Rate denominator: per minute.
    """
    hour = "hour"
    """
    Rate denominator: per hour.
    """
    day = "day"
    """
    Rate denominator: per day.
    """
    week = "week"
    """
    Rate denominator: per week.
    """
    month = "month"
    """
    Rate denominator: per month.
    """
    quarter = "quarter"
    """
    Rate denominator: per quarter.
    """
    year = "year"
    """
    Rate denominator: per year.
    """


class TransitionDirection(str, Enum):
    """
    Direction of flow on a transition.
    """
    source_to_destination = "source_to_destination"
    """
    Flow direction: source-to-destination.
    """
    destination_to_source = "destination_to_source"
    """
    Flow direction: destination-to-source.
    """


class RelationshipKind(str, Enum):
    """
    Discriminator for the variant of a ``relationship-type``: exactly one of the following keys is set on a relationship's ``relationship-type``.
    """
    interacts = "interacts"
    """
    Actor-to-nodes interaction.
    """
    connects = "connects"
    """
    Interface-to-interface connection.
    """
    deployed_in = "deployed_in"
    """
    Containment: nodes deployed in a container.
    """
    composed_of = "composed_of"
    """
    Composition: nodes composed by a container.
    """
    options = "options"
    """
    A set of alternative decisions.
    """



class Architecture(ConfiguredBaseModel):
    """
    Top-level CALM architecture document.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'calm:Architecture',
         'close_mappings': ['schema:SoftwareApplication', 'gist:System'],
         'from_schema': 'https://w3id.org/lmodel/calm',
         'in_subset': ['core'],
         'related_mappings': ['capec:Category',
                              'cis_controls:CISControlsDocument',
                              'dpv:Context',
                              'iso27001:InformationSecurityManagementSystem',
                              'nist_csf_v2:CSFDocument',
                              'nist_sp_800_53:Catalog',
                              'oscal:SystemSecurityPlan',
                              'stix:Bundle'],
         'slot_usage': {'flows': {'inlined': True,
                                  'inlined_as_list': True,
                                  'name': 'flows'},
                        'nodes': {'inlined': True,
                                  'inlined_as_list': True,
                                  'name': 'nodes'},
                        'relationships': {'inlined': True,
                                          'inlined_as_list': True,
                                          'name': 'relationships'}},
         'title': 'Common Architecture Language Model (CALM) Vocab',
         'tree_root': True})

    nodes: Optional[list[Node]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Architecture',
                       'InteractsRelationship',
                       'DeployedInRelationship',
                       'ComposedOfRelationship',
                       'Decision']} })
    relationships: Optional[list[Relationship]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Architecture', 'Decision']} })
    metadata: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Architecture', 'Node', 'Relationship', 'Flow', 'Timeline']} })
    controls: Optional[Control] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Architecture', 'Node', 'Relationship', 'Decision', 'Flow']} })
    flows: Optional[list[Flow]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Architecture']} })
    adrs: Optional[list[str]] = Field(default=None, description="""External links to ADRs (Architecture Decision Records) or similar documents that provide context or decisions related to the architecture. These can be URLs or references to internal documentation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Architecture', 'NodeMoment']} })


class Node(ConfiguredBaseModel):
    """
    A logical or physical element of an architecture (system, service, actor, ...).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['stix:StixDomainObject'],
         'class_uri': 'calm:Node',
         'close_mappings': ['schema:Thing',
                            'attack:Asset',
                            'gist:NetworkNode',
                            'iso27001:Asset',
                            'ocsf:Node',
                            'ocsf:Actor'],
         'from_schema': 'https://w3id.org/lmodel/calm',
         'in_subset': ['core'],
         'related_mappings': ['capec:AttackPattern',
                              'cis_controls:Safeguard',
                              'dpv:DataController',
                              'oscal:SspInventoryItem'],
         'slot_usage': {'description': {'name': 'description', 'required': True},
                        'interfaces': {'inlined': True,
                                       'inlined_as_list': True,
                                       'name': 'interfaces'}}})

    unique_id: str = Field(default=..., description="""Stable opaque identifier used to cross-link CALM elements.""", json_schema_extra = { "linkml_meta": {'aliases': ['unique-id'],
         'domain_of': ['Node',
                       'Relationship',
                       'Decorator',
                       'Flow',
                       'InterfaceDefinition',
                       'InterfaceType'],
         'slot_uri': 'schema:identifier'} })
    node_type: Union[NodeType, str] = Field(default=..., description="""Category of the node (system, service, actor, etc.).""", json_schema_extra = { "linkml_meta": {'aliases': ['node-type'],
         'any_of': [{'range': 'NodeType'}, {'range': 'string'}],
         'domain_of': ['Node', 'NodeMoment']} })
    name: str = Field(default=..., description="""Short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'ControlRequirement', 'Flow'], 'slot_uri': 'rdfs:label'} })
    description: str = Field(default=..., description="""Free-form description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node',
                       'Relationship',
                       'Decision',
                       'ControlRequirement',
                       'Transition',
                       'Flow'],
         'slot_uri': 'dct:description'} })
    details: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Node']} })
    interfaces: Optional[list[InterfaceDefinition]] = Field(default=None, description="""Interface definitions exposed by nodes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'NodeInterface', 'NodeMoment']} })
    controls: Optional[Control] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Architecture', 'Node', 'Relationship', 'Decision', 'Flow']} })
    metadata: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Architecture', 'Node', 'Relationship', 'Flow', 'Timeline']} })


class Relationship(ConfiguredBaseModel):
    """
    A typed link between architecture elements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'calm:Relationship',
         'close_mappings': ['gist:NetworkLink', 'stix:StixRelationshipObject'],
         'from_schema': 'https://w3id.org/lmodel/calm',
         'in_subset': ['core'],
         'related_mappings': ['prov:wasInfluencedBy',
                              'attack:AttackRelationship',
                              'ocsf:NetworkEndpoint']})

    unique_id: str = Field(default=..., description="""Stable opaque identifier used to cross-link CALM elements.""", json_schema_extra = { "linkml_meta": {'aliases': ['unique-id'],
         'domain_of': ['Node',
                       'Relationship',
                       'Decorator',
                       'Flow',
                       'InterfaceDefinition',
                       'InterfaceType'],
         'slot_uri': 'schema:identifier'} })
    description: Optional[str] = Field(default=None, description="""Free-form description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node',
                       'Relationship',
                       'Decision',
                       'ControlRequirement',
                       'Transition',
                       'Flow'],
         'slot_uri': 'dct:description'} })
    relationship_type: RelationshipType = Field(default=..., json_schema_extra = { "linkml_meta": {'aliases': ['relationship-type'], 'domain_of': ['Relationship']} })
    protocol: Optional[Protocol] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Relationship']} })
    metadata: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Architecture', 'Node', 'Relationship', 'Flow', 'Timeline']} })
    controls: Optional[Control] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Architecture', 'Node', 'Relationship', 'Decision', 'Flow']} })


class InteractsRelationship(ConfiguredBaseModel):
    """
    An ``interacts`` relationship between an actor and one or more nodes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'calm:InteractsRelationship',
         'from_schema': 'https://w3id.org/lmodel/calm',
         'in_subset': ['core'],
         'slot_usage': {'nodes': {'name': 'nodes', 'required': True}}})

    actor: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['InteractsRelationship']} })
    nodes: list[str] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Architecture',
                       'InteractsRelationship',
                       'DeployedInRelationship',
                       'ComposedOfRelationship',
                       'Decision']} })


class ConnectsRelationship(ConfiguredBaseModel):
    """
    A ``connects`` relationship between two node interfaces.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'calm:ConnectsRelationship',
         'from_schema': 'https://w3id.org/lmodel/calm',
         'in_subset': ['core']})

    source: NodeInterface = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ConnectsRelationship']} })
    destination: NodeInterface = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ConnectsRelationship']} })


class DeployedInRelationship(ConfiguredBaseModel):
    """
    A ``deployed-in`` containment relationship.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'calm:DeployedInRelationship',
         'from_schema': 'https://w3id.org/lmodel/calm',
         'in_subset': ['core'],
         'slot_usage': {'nodes': {'name': 'nodes', 'required': True}}})

    container: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['DeployedInRelationship', 'ComposedOfRelationship']} })
    nodes: list[str] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Architecture',
                       'InteractsRelationship',
                       'DeployedInRelationship',
                       'ComposedOfRelationship',
                       'Decision']} })


class ComposedOfRelationship(ConfiguredBaseModel):
    """
    A ``composed-of`` containment relationship.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'calm:ComposedOfRelationship',
         'from_schema': 'https://w3id.org/lmodel/calm',
         'in_subset': ['core'],
         'slot_usage': {'nodes': {'name': 'nodes', 'required': True}}})

    container: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['DeployedInRelationship', 'ComposedOfRelationship']} })
    nodes: list[str] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Architecture',
                       'InteractsRelationship',
                       'DeployedInRelationship',
                       'ComposedOfRelationship',
                       'Decision']} })


class Decision(ConfiguredBaseModel):
    """
    A candidate decision within an ``options`` relationship.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'calm:Decision',
         'from_schema': 'https://w3id.org/lmodel/calm',
         'in_subset': ['core'],
         'slot_usage': {'description': {'name': 'description', 'required': True},
                        'nodes': {'inlined': True,
                                  'inlined_as_list': True,
                                  'name': 'nodes',
                                  'required': True},
                        'relationships': {'inlined': True,
                                          'inlined_as_list': True,
                                          'name': 'relationships',
                                          'required': True}}})

    description: str = Field(default=..., description="""Free-form description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node',
                       'Relationship',
                       'Decision',
                       'ControlRequirement',
                       'Transition',
                       'Flow'],
         'slot_uri': 'dct:description'} })
    nodes: list[Node] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Architecture',
                       'InteractsRelationship',
                       'DeployedInRelationship',
                       'ComposedOfRelationship',
                       'Decision']} })
    relationships: list[Relationship] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Architecture', 'Decision']} })
    controls: Optional[Control] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Architecture', 'Node', 'Relationship', 'Decision', 'Flow']} })


class ControlDetail(ConfiguredBaseModel):
    """
    A single control requirement and its inline / referenced configuration.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'calm:ControlDetail',
         'close_mappings': ['dpv:TechnicalMeasure', 'oscal:SspImplementedRequirement'],
         'from_schema': 'https://w3id.org/lmodel/calm',
         'in_subset': ['control_framework'],
         'related_mappings': ['nist_sp_800_53:ControlGroup'],
         'slot_usage': {'requirement_url': {'name': 'requirement_url',
                                            'required': True}}})

    requirement_url: str = Field(default=..., description="""The requirement schema that specifies how a control should be defined""", json_schema_extra = { "linkml_meta": {'aliases': ['requirement-url'],
         'domain_of': ['ControlDetail', 'Flow'],
         'slot_uri': 'schema:url'} })
    config_url: Optional[str] = Field(default=None, description="""The configuration of how the control requirement schema is met""", json_schema_extra = { "linkml_meta": {'aliases': ['config-url'],
         'domain_of': ['ControlDetail'],
         'slot_uri': 'schema:url'} })
    config: Optional[str] = Field(default=None, description="""Inline configuration of how the control requirement schema is met""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlDetail', 'InterfaceDefinition']} })


class Control(ConfiguredBaseModel):
    """
    A named control attached to an architecture element.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'calm:Control',
         'close_mappings': ['attack:Mitigation',
                            'cis_controls:Safeguard',
                            'dpv:TechnicalOrganisationalMeasure',
                            'iso27001:SecurityControl',
                            'nist_csf_v2:CSFSubcategory',
                            'nist_sp_800_53:Control',
                            'ocsf:Compliance',
                            'oscal:Control'],
         'from_schema': 'https://w3id.org/lmodel/calm',
         'in_subset': ['control_framework'],
         'related_mappings': ['schema:Action', 'capec:Category', 'stix:Core']})

    pass


class ControlRequirement(ConfiguredBaseModel):
    """
    Domain-defined control requirement that controls can reference.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'calm:ControlRequirement',
         'close_mappings': ['cis_controls:CISControl',
                            'dpv:OrganisationalMeasure',
                            'iso27001:SecurityControl',
                            'nist_csf_v2:CSFCategory',
                            'oscal:Control'],
         'from_schema': 'https://w3id.org/lmodel/calm',
         'in_subset': ['control_framework'],
         'related_mappings': ['attack:Technique',
                              'capec:View',
                              'nist_sp_800_53:ControlEnhancement'],
         'slot_usage': {'description': {'name': 'description', 'required': True}},
         'title': 'Common Architecture Language Model Control Requirement'})

    control_id: str = Field(default=..., description="""The unique identifier of this control, which has the potential to be used for linking evidence""", json_schema_extra = { "linkml_meta": {'aliases': ['control-id'], 'domain_of': ['ControlRequirement']} })
    name: str = Field(default=..., description="""Short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'ControlRequirement', 'Flow'], 'slot_uri': 'rdfs:label'} })
    description: str = Field(default=..., description="""Free-form description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node',
                       'Relationship',
                       'Decision',
                       'ControlRequirement',
                       'Transition',
                       'Flow'],
         'slot_uri': 'dct:description'} })


class Decorator(ConfiguredBaseModel):
    """
    Cross-cutting annotation attached to nodes, relationships, or flows.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'calm:Decorator',
         'from_schema': 'https://w3id.org/lmodel/calm',
         'in_subset': ['decorators'],
         'related_mappings': ['iso27001:MonitoringItem',
                              'nist_csf_v2:Link',
                              'stix:ExtensionDefinition']})

    unique_id: str = Field(default=..., description="""Stable opaque identifier used to cross-link CALM elements.""", json_schema_extra = { "linkml_meta": {'aliases': ['unique-id'],
         'domain_of': ['Node',
                       'Relationship',
                       'Decorator',
                       'Flow',
                       'InterfaceDefinition',
                       'InterfaceType'],
         'slot_uri': 'schema:identifier'} })
    type: str = Field(default=..., description="""Type of decorator - a free-form string identifying the decorator category""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decorator']} })
    target: list[str] = Field(default=..., description="""Array of file paths or URLs referencing the CALM documents (patterns, architectures, or controls) this decorator targets""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decorator']} })
    applies_to: list[str] = Field(default=..., description="""Array of unique-ids referencing nodes, relationships, flows, or other architecture elements""", json_schema_extra = { "linkml_meta": {'aliases': ['applies-to'], 'domain_of': ['Decorator']} })
    data: str = Field(default=..., description="""Free-form JSON object containing the decorator's data""", json_schema_extra = { "linkml_meta": {'domain_of': ['Decorator']} })


class EvidenceDocument(ConfiguredBaseModel):
    """
    Top-level CALM evidence document linking control configurations to evidence artefacts.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'calm:EvidenceDocument',
         'close_mappings': ['iso27001:DocumentedInformation',
                            'ocsf:Evidences',
                            'oscal:AssessmentResults'],
         'from_schema': 'https://w3id.org/lmodel/calm',
         'in_subset': ['control_framework'],
         'related_mappings': ['dpv:LegalMeasure'],
         'title': 'Common Architecture Language Model Evidence'})

    evidence: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceDocument']} })


class Transition(ConfiguredBaseModel):
    """
    A single step in a flow, anchored on a relationship.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'calm:Transition',
         'close_mappings': ['fluxnova_bpmn_platform:SequenceFlow'],
         'from_schema': 'https://w3id.org/lmodel/calm',
         'in_subset': ['flow_modeling'],
         'slot_usage': {'description': {'name': 'description', 'required': True}}})

    relationship_unique_id: str = Field(default=..., description="""Unique identifier for the relationship in the architecture""", json_schema_extra = { "linkml_meta": {'aliases': ['relationship-unique-id'], 'domain_of': ['Transition']} })
    sequence_number: int = Field(default=..., description="""Indicates the sequence of the relationship in the flow""", ge=1, json_schema_extra = { "linkml_meta": {'aliases': ['sequence-number'], 'domain_of': ['Transition']} })
    description: str = Field(default=..., description="""Free-form description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node',
                       'Relationship',
                       'Decision',
                       'ControlRequirement',
                       'Transition',
                       'Flow'],
         'slot_uri': 'dct:description'} })
    direction: Optional[TransitionDirection] = Field(default=None, description="""Direction of flow on the transition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Transition']} })


class Flow(ConfiguredBaseModel):
    """
    Business flow mapped onto architecture relationships.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'calm:Flow',
         'close_mappings': ['fluxnova_bpmn_platform:FlowElement'],
         'from_schema': 'https://w3id.org/lmodel/calm',
         'in_subset': ['flow_modeling'],
         'related_mappings': ['attack:Tactic',
                              'fluxnova_bpmn_platform:SubProcess',
                              'gist:ServiceSpecification',
                              'iso27001:OperationalProcedure',
                              'nist_csf_v2:CSFFunction',
                              'ocsf:NetworkTraffic',
                              'oscal:SspControlImplementation'],
         'slot_usage': {'description': {'name': 'description', 'required': True}}})

    unique_id: str = Field(default=..., description="""Stable opaque identifier used to cross-link CALM elements.""", json_schema_extra = { "linkml_meta": {'aliases': ['unique-id'],
         'domain_of': ['Node',
                       'Relationship',
                       'Decorator',
                       'Flow',
                       'InterfaceDefinition',
                       'InterfaceType'],
         'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""Short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'ControlRequirement', 'Flow'], 'slot_uri': 'rdfs:label'} })
    description: str = Field(default=..., description="""Free-form description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node',
                       'Relationship',
                       'Decision',
                       'ControlRequirement',
                       'Transition',
                       'Flow'],
         'slot_uri': 'dct:description'} })
    requirement_url: Optional[str] = Field(default=None, description="""The requirement schema that specifies how a control should be defined""", json_schema_extra = { "linkml_meta": {'aliases': ['requirement-url'],
         'domain_of': ['ControlDetail', 'Flow'],
         'slot_uri': 'schema:url'} })
    transitions: list[Transition] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Flow']} })
    controls: Optional[Control] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Architecture', 'Node', 'Relationship', 'Decision', 'Flow']} })
    metadata: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Architecture', 'Node', 'Relationship', 'Flow', 'Timeline']} })


class InterfaceDefinition(ConfiguredBaseModel):
    """
    Modular interface definition referencing an external schema.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'calm:InterfaceDefinition',
         'close_mappings': ['ocsf:NetworkInterface'],
         'from_schema': 'https://w3id.org/lmodel/calm',
         'in_subset': ['interface_defs'],
         'related_mappings': ['gist:Network'],
         'slot_usage': {'config': {'name': 'config', 'required': True}}})

    unique_id: str = Field(default=..., description="""Stable opaque identifier used to cross-link CALM elements.""", json_schema_extra = { "linkml_meta": {'aliases': ['unique-id'],
         'domain_of': ['Node',
                       'Relationship',
                       'Decorator',
                       'Flow',
                       'InterfaceDefinition',
                       'InterfaceType'],
         'slot_uri': 'schema:identifier'} })
    definition_url: str = Field(default=..., description="""URI of the external schema this interface configuration conforms to""", json_schema_extra = { "linkml_meta": {'aliases': ['definition-url'],
         'domain_of': ['InterfaceDefinition'],
         'slot_uri': 'schema:url'} })
    config: str = Field(default=..., description="""Inline configuration of how the control requirement schema is met""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlDetail', 'InterfaceDefinition']} })


class InterfaceType(ConfiguredBaseModel):
    """
    Inline (free-form) interface definition keyed by unique-id.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'calm:InterfaceType',
         'from_schema': 'https://w3id.org/lmodel/calm',
         'in_subset': ['interface_defs']})

    unique_id: str = Field(default=..., description="""Stable opaque identifier used to cross-link CALM elements.""", json_schema_extra = { "linkml_meta": {'aliases': ['unique-id'],
         'domain_of': ['Node',
                       'Relationship',
                       'Decorator',
                       'Flow',
                       'InterfaceDefinition',
                       'InterfaceType'],
         'slot_uri': 'schema:identifier'} })


class NodeInterface(ConfiguredBaseModel):
    """
    Reference to one or more interfaces exposed by a node.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'calm:NodeInterface',
         'from_schema': 'https://w3id.org/lmodel/calm',
         'in_subset': ['interface_defs'],
         'slot_usage': {'interfaces': {'inlined': True,
                                       'inlined_as_list': True,
                                       'name': 'interfaces'}}})

    node: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['NodeInterface']} })
    interfaces: Optional[list[InterfaceDefinition]] = Field(default=None, description="""Interface definitions exposed by nodes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'NodeInterface', 'NodeMoment']} })


class Timeline(ConfiguredBaseModel):
    """
    CALM timeline document capturing architecture moments over time.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'calm:Timeline',
         'from_schema': 'https://w3id.org/lmodel/calm',
         'in_subset': ['timeline'],
         'related_mappings': ['fluxnova_bpmn_platform:Process',
                              'gist:TemporalRelation',
                              'iso27001:ManagementReview',
                              'oscal:AssessmentResultsDocument'],
         'title': 'Common Architecture Language Model (CALM) Timelines Vocab',
         'tree_root': True})

    current_moment: Optional[str] = Field(default=None, description="""The unique-id of the current architecture moment within the timeline.""", json_schema_extra = { "linkml_meta": {'aliases': ['current-moment'], 'domain_of': ['Timeline']} })
    moments: list[str] = Field(default=..., description="""A list of significant architecture states or points in time, each represented as a 'moment'.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Timeline']} })
    metadata: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Architecture', 'Node', 'Relationship', 'Flow', 'Timeline']} })


class NodeMoment(Node):
    """
    An architecture moment - a point-in-time snapshot of the architecture.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'calm:NodeMoment',
         'from_schema': 'https://w3id.org/lmodel/calm',
         'in_subset': ['timeline'],
         'related_mappings': ['fluxnova_bpmn_platform:FlowNode',
                              'fluxnova_bpmn_platform:EndEvent'],
         'slot_usage': {'details': {'name': 'details', 'required': True}}})

    node_type: Union[NodeType, str] = Field(default=..., description="""Category of the node (system, service, actor, etc.).""", json_schema_extra = { "linkml_meta": {'aliases': ['node-type'],
         'any_of': [{'range': 'NodeType'}, {'range': 'string'}],
         'domain_of': ['Node', 'NodeMoment']} })
    valid_from: Optional[date] = Field(default=None, description="""The date when this architecture moment came into effect.""", json_schema_extra = { "linkml_meta": {'aliases': ['valid-from'],
         'annotations': {'json_format': {'tag': 'json_format', 'value': 'date'}},
         'domain_of': ['NodeMoment'],
         'slot_uri': 'prov:startedAtTime'} })
    adrs: Optional[list[str]] = Field(default=None, description="""External links to ADRs (Architecture Decision Records) or similar documents that provide context or decisions related to the architecture. These can be URLs or references to internal documentation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Architecture', 'NodeMoment']} })
    interfaces: Optional[list[InterfaceDefinition]] = Field(default=None, description="""Interface definitions exposed by nodes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'NodeInterface', 'NodeMoment']} })
    unique_id: str = Field(default=..., description="""Stable opaque identifier used to cross-link CALM elements.""", json_schema_extra = { "linkml_meta": {'aliases': ['unique-id'],
         'domain_of': ['Node',
                       'Relationship',
                       'Decorator',
                       'Flow',
                       'InterfaceDefinition',
                       'InterfaceType'],
         'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""Short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node', 'ControlRequirement', 'Flow'], 'slot_uri': 'rdfs:label'} })
    description: str = Field(default=..., description="""Free-form description of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Node',
                       'Relationship',
                       'Decision',
                       'ControlRequirement',
                       'Transition',
                       'Flow'],
         'slot_uri': 'dct:description'} })
    details: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Node']} })
    controls: Optional[Control] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Architecture', 'Node', 'Relationship', 'Decision', 'Flow']} })
    metadata: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Architecture', 'Node', 'Relationship', 'Flow', 'Timeline']} })


class TimeUnit(ConfiguredBaseModel):
    """
    A quantity of time expressed as a numeric value and a unit.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'calm:TimeUnit',
         'exact_mappings': ['schema:Duration'],
         'from_schema': 'https://w3id.org/lmodel/calm',
         'in_subset': ['units']})

    unit: TimeUnitName = Field(default=..., description="""The unit of time (e.g., seconds, minutes, hours).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeUnit']} })
    value: float = Field(default=..., description="""The numeric value representing the amount of time.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['TimeUnit']} })


class RateUnit(ConfiguredBaseModel):
    """
    A rate (count per time unit), e.g. operations per second.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'calm:RateUnit',
         'from_schema': 'https://w3id.org/lmodel/calm',
         'in_subset': ['units']})

    rate: float = Field(default=..., description="""The numeric value representing the rate.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['RateUnit']} })
    per: RatePerUnit = Field(default=..., description="""The time unit defining the rate interval.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RateUnit']} })


class OptionList(ConfiguredBaseModel):
    """
    Wrapper around the list of ``Decision`` alternatives in an options relationship.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/calm'})

    decisions: Optional[list[Decision]] = Field(default=None, description="""Alternative decisions under an ``options`` relationship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OptionList']} })


class RelationshipType(ConfiguredBaseModel):
    """
    Tagged-union container for the variant body of a relationship. Exactly one of ``interacts``, ``connects``, ``deployed_in``, ``composed_of``, ``options`` is populated; see ``RelationshipKind`` for the discriminator values.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'calm:RelationshipType',
         'from_schema': 'https://w3id.org/lmodel/calm',
         'in_subset': ['core']})

    interacts: Optional[InteractsRelationship] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipType']} })
    connects: Optional[ConnectsRelationship] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipType']} })
    deployed_in: Optional[DeployedInRelationship] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['deployed-in'], 'domain_of': ['RelationshipType']} })
    composed_of: Optional[ComposedOfRelationship] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['composed-of'], 'domain_of': ['RelationshipType']} })
    options: Optional[list[Decision]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['RelationshipType']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Architecture.model_rebuild()
Node.model_rebuild()
Relationship.model_rebuild()
InteractsRelationship.model_rebuild()
ConnectsRelationship.model_rebuild()
DeployedInRelationship.model_rebuild()
ComposedOfRelationship.model_rebuild()
Decision.model_rebuild()
ControlDetail.model_rebuild()
Control.model_rebuild()
ControlRequirement.model_rebuild()
Decorator.model_rebuild()
EvidenceDocument.model_rebuild()
Transition.model_rebuild()
Flow.model_rebuild()
InterfaceDefinition.model_rebuild()
InterfaceType.model_rebuild()
NodeInterface.model_rebuild()
Timeline.model_rebuild()
NodeMoment.model_rebuild()
TimeUnit.model_rebuild()
RateUnit.model_rebuild()
OptionList.model_rebuild()
RelationshipType.model_rebuild()
