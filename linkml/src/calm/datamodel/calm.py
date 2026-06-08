# Auto generated from calm.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-07-03T00:41:53
# Schema: calm
#
# id: https://w3id.org/lmodel/calm
# description: LinkML representation of the FINOS Common Architecture Language Model (CALM) 1.2 specification. CALM is a declarative, JSON-based modeling language for describing complex software architectures (nodes, relationships, controls, flows, decorators, timelines, evidence, and units). This LinkML schema is generated from the CALM JSON-Schema meta files.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Date, Float, Integer, String
from linkml_runtime.utils.metamodelcore import XSDDate

metamodel_version = "1.11.0"
version = "1.2"

# Namespaces
AI_GOVERNANCE_FRAMEWORK = CurieNamespace('ai_governance_framework', 'https://w3id.org/lmodel/ai-governance-framework/')
ATTACK = CurieNamespace('attack', 'https://w3id.org/lmodel/attack/')
CALM = CurieNamespace('calm', 'https://w3id.org/lmodel/calm/')
CAPEC = CurieNamespace('capec', 'https://w3id.org/lmodel/capec/')
CIS_CONTROLS = CurieNamespace('cis_controls', 'https://w3id.org/lmodel/cis-controls/')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
DPV = CurieNamespace('dpv', 'https://w3id.org/lmodel/dpv/')
FINOS_CALM = CurieNamespace('finos_calm', 'https://calm.finos.org/release/1.2/meta/')
FLUXNOVA_BPMN_PLATFORM = CurieNamespace('fluxnova_bpmn_platform', 'https://w3id.org/lmodel/fluxnova-bpm-platform/')
GIST = CurieNamespace('gist', 'https://w3id.org/lmodel/gist/')
ISO27001 = CurieNamespace('iso27001', 'https://w3id.org/lmodel/iso27001/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NIST_CSF_V2 = CurieNamespace('nist_csf_v2', 'https://w3id.org/lmodel/nist-csf-v2/')
NIST_SP_800_53 = CurieNamespace('nist_sp_800_53', 'https://w3id.org/lmodel/nist-sp-800-53/')
OCSF = CurieNamespace('ocsf', 'https://w3id.org/lmodel/ocsf/')
OSCAL = CurieNamespace('oscal', 'https://w3id.org/lmodel/oscal/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
STIX = CurieNamespace('stix', 'https://w3id.org/lmodel/stix/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CALM


# Types
class CronExpression(str):
    """ A Unix-style cron expression (minute, hour, day, month, weekday). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "CronExpression"
    type_model_uri = CALM.CronExpression


class Metadata(str):
    """ Opaque key/value metadata payload. JSON-Schema allows either an object or an array of objects; in LinkML this is modeled as a permissive string type that downstream consumers parse as JSON. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Metadata"
    type_model_uri = CALM.Metadata


# Class references
class NodeUniqueId(extended_str):
    pass


class RelationshipUniqueId(extended_str):
    pass


class ControlRequirementControlId(extended_str):
    pass


class DecoratorUniqueId(extended_str):
    pass


class FlowUniqueId(extended_str):
    pass


class InterfaceDefinitionUniqueId(extended_str):
    pass


class InterfaceTypeUniqueId(extended_str):
    pass


class NodeMomentUniqueId(NodeUniqueId):
    pass


@dataclass(repr=False)
class Architecture(YAMLRoot):
    """
    Top-level CALM architecture document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["Architecture"]
    class_class_curie: ClassVar[str] = "calm:Architecture"
    class_name: ClassVar[str] = "Architecture"
    class_model_uri: ClassVar[URIRef] = CALM.Architecture

    nodes: Optional[Union[dict[Union[str, NodeUniqueId], Union[dict, "Node"]], list[Union[dict, "Node"]]]] = empty_dict()
    relationships: Optional[Union[dict[Union[str, RelationshipUniqueId], Union[dict, "Relationship"]], list[Union[dict, "Relationship"]]]] = empty_dict()
    metadata: Optional[str] = None
    controls: Optional[Union[dict, "Control"]] = None
    flows: Optional[Union[dict[Union[str, FlowUniqueId], Union[dict, "Flow"]], list[Union[dict, "Flow"]]]] = empty_dict()
    adrs: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="nodes", slot_type=Node, key_name="unique_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="relationships", slot_type=Relationship, key_name="unique_id", keyed=True)

        if self.metadata is not None and not isinstance(self.metadata, str):
            self.metadata = str(self.metadata)

        if self.controls is not None and not isinstance(self.controls, Control):
            self.controls = Control()

        self._normalize_inlined_as_list(slot_name="flows", slot_type=Flow, key_name="unique_id", keyed=True)

        if not isinstance(self.adrs, list):
            self.adrs = [self.adrs] if self.adrs is not None else []
        self.adrs = [v if isinstance(v, str) else str(v) for v in self.adrs]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Node(YAMLRoot):
    """
    A logical or physical element of an architecture (system, service, actor, ...).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["Node"]
    class_class_curie: ClassVar[str] = "calm:Node"
    class_name: ClassVar[str] = "Node"
    class_model_uri: ClassVar[URIRef] = CALM.Node

    unique_id: Union[str, NodeUniqueId] = None
    node_type: Union[str, "NodeType"] = None
    name: str = None
    description: str = None
    details: Optional[str] = None
    interfaces: Optional[Union[dict[Union[str, InterfaceDefinitionUniqueId], Union[dict, "InterfaceDefinition"]], list[Union[dict, "InterfaceDefinition"]]]] = empty_dict()
    controls: Optional[Union[dict, "Control"]] = None
    metadata: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.unique_id):
            self.MissingRequiredField("unique_id")
        if not isinstance(self.unique_id, NodeUniqueId):
            self.unique_id = NodeUniqueId(self.unique_id)

        if self._is_empty(self.node_type):
            self.MissingRequiredField("node_type")
        if not isinstance(self.node_type, NodeType):
            self.node_type = NodeType(self.node_type)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.details is not None and not isinstance(self.details, str):
            self.details = str(self.details)

        self._normalize_inlined_as_list(slot_name="interfaces", slot_type=InterfaceDefinition, key_name="unique_id", keyed=True)

        if self.controls is not None and not isinstance(self.controls, Control):
            self.controls = Control()

        if self.metadata is not None and not isinstance(self.metadata, str):
            self.metadata = str(self.metadata)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Relationship(YAMLRoot):
    """
    A typed link between architecture elements.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["Relationship"]
    class_class_curie: ClassVar[str] = "calm:Relationship"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = CALM.Relationship

    unique_id: Union[str, RelationshipUniqueId] = None
    relationship_type: Union[dict, "RelationshipType"] = None
    description: Optional[str] = None
    protocol: Optional[Union[str, "Protocol"]] = None
    metadata: Optional[str] = None
    controls: Optional[Union[dict, "Control"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.unique_id):
            self.MissingRequiredField("unique_id")
        if not isinstance(self.unique_id, RelationshipUniqueId):
            self.unique_id = RelationshipUniqueId(self.unique_id)

        if self._is_empty(self.relationship_type):
            self.MissingRequiredField("relationship_type")
        if not isinstance(self.relationship_type, RelationshipType):
            self.relationship_type = RelationshipType(**as_dict(self.relationship_type))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.protocol is not None and not isinstance(self.protocol, Protocol):
            self.protocol = Protocol(self.protocol)

        if self.metadata is not None and not isinstance(self.metadata, str):
            self.metadata = str(self.metadata)

        if self.controls is not None and not isinstance(self.controls, Control):
            self.controls = Control()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InteractsRelationship(YAMLRoot):
    """
    An ``interacts`` relationship between an actor and one or more nodes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["InteractsRelationship"]
    class_class_curie: ClassVar[str] = "calm:InteractsRelationship"
    class_name: ClassVar[str] = "InteractsRelationship"
    class_model_uri: ClassVar[URIRef] = CALM.InteractsRelationship

    actor: str = None
    nodes: Union[Union[str, NodeUniqueId], list[Union[str, NodeUniqueId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.actor):
            self.MissingRequiredField("actor")
        if not isinstance(self.actor, str):
            self.actor = str(self.actor)

        if self._is_empty(self.nodes):
            self.MissingRequiredField("nodes")
        if not isinstance(self.nodes, list):
            self.nodes = [self.nodes] if self.nodes is not None else []
        self.nodes = [v if isinstance(v, NodeUniqueId) else NodeUniqueId(v) for v in self.nodes]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConnectsRelationship(YAMLRoot):
    """
    A ``connects`` relationship between two node interfaces.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["ConnectsRelationship"]
    class_class_curie: ClassVar[str] = "calm:ConnectsRelationship"
    class_name: ClassVar[str] = "ConnectsRelationship"
    class_model_uri: ClassVar[URIRef] = CALM.ConnectsRelationship

    source: Union[dict, "NodeInterface"] = None
    destination: Union[dict, "NodeInterface"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, NodeInterface):
            self.source = NodeInterface(**as_dict(self.source))

        if self._is_empty(self.destination):
            self.MissingRequiredField("destination")
        if not isinstance(self.destination, NodeInterface):
            self.destination = NodeInterface(**as_dict(self.destination))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DeployedInRelationship(YAMLRoot):
    """
    A ``deployed-in`` containment relationship.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["DeployedInRelationship"]
    class_class_curie: ClassVar[str] = "calm:DeployedInRelationship"
    class_name: ClassVar[str] = "DeployedInRelationship"
    class_model_uri: ClassVar[URIRef] = CALM.DeployedInRelationship

    container: str = None
    nodes: Union[Union[str, NodeUniqueId], list[Union[str, NodeUniqueId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.container):
            self.MissingRequiredField("container")
        if not isinstance(self.container, str):
            self.container = str(self.container)

        if self._is_empty(self.nodes):
            self.MissingRequiredField("nodes")
        if not isinstance(self.nodes, list):
            self.nodes = [self.nodes] if self.nodes is not None else []
        self.nodes = [v if isinstance(v, NodeUniqueId) else NodeUniqueId(v) for v in self.nodes]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComposedOfRelationship(YAMLRoot):
    """
    A ``composed-of`` containment relationship.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["ComposedOfRelationship"]
    class_class_curie: ClassVar[str] = "calm:ComposedOfRelationship"
    class_name: ClassVar[str] = "ComposedOfRelationship"
    class_model_uri: ClassVar[URIRef] = CALM.ComposedOfRelationship

    container: str = None
    nodes: Union[Union[str, NodeUniqueId], list[Union[str, NodeUniqueId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.container):
            self.MissingRequiredField("container")
        if not isinstance(self.container, str):
            self.container = str(self.container)

        if self._is_empty(self.nodes):
            self.MissingRequiredField("nodes")
        if not isinstance(self.nodes, list):
            self.nodes = [self.nodes] if self.nodes is not None else []
        self.nodes = [v if isinstance(v, NodeUniqueId) else NodeUniqueId(v) for v in self.nodes]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Decision(YAMLRoot):
    """
    A candidate decision within an ``options`` relationship.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["Decision"]
    class_class_curie: ClassVar[str] = "calm:Decision"
    class_name: ClassVar[str] = "Decision"
    class_model_uri: ClassVar[URIRef] = CALM.Decision

    description: str = None
    nodes: Union[dict[Union[str, NodeUniqueId], Union[dict, Node]], list[Union[dict, Node]]] = empty_dict()
    relationships: Union[dict[Union[str, RelationshipUniqueId], Union[dict, Relationship]], list[Union[dict, Relationship]]] = empty_dict()
    controls: Optional[Union[dict, "Control"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.nodes):
            self.MissingRequiredField("nodes")
        self._normalize_inlined_as_list(slot_name="nodes", slot_type=Node, key_name="unique_id", keyed=True)

        if self._is_empty(self.relationships):
            self.MissingRequiredField("relationships")
        self._normalize_inlined_as_list(slot_name="relationships", slot_type=Relationship, key_name="unique_id", keyed=True)

        if self.controls is not None and not isinstance(self.controls, Control):
            self.controls = Control()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ControlDetail(YAMLRoot):
    """
    A single control requirement and its inline / referenced configuration.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["ControlDetail"]
    class_class_curie: ClassVar[str] = "calm:ControlDetail"
    class_name: ClassVar[str] = "ControlDetail"
    class_model_uri: ClassVar[URIRef] = CALM.ControlDetail

    requirement_url: str = None
    config_url: Optional[str] = None
    config: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.requirement_url):
            self.MissingRequiredField("requirement_url")
        if not isinstance(self.requirement_url, str):
            self.requirement_url = str(self.requirement_url)

        if self.config_url is not None and not isinstance(self.config_url, str):
            self.config_url = str(self.config_url)

        if self.config is not None and not isinstance(self.config, str):
            self.config = str(self.config)

        super().__post_init__(**kwargs)


class Control(YAMLRoot):
    """
    A named control attached to an architecture element.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["Control"]
    class_class_curie: ClassVar[str] = "calm:Control"
    class_name: ClassVar[str] = "Control"
    class_model_uri: ClassVar[URIRef] = CALM.Control


@dataclass(repr=False)
class ControlRequirement(YAMLRoot):
    """
    Domain-defined control requirement that controls can reference.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["ControlRequirement"]
    class_class_curie: ClassVar[str] = "calm:ControlRequirement"
    class_name: ClassVar[str] = "ControlRequirement"
    class_model_uri: ClassVar[URIRef] = CALM.ControlRequirement

    control_id: Union[str, ControlRequirementControlId] = None
    name: str = None
    description: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.control_id):
            self.MissingRequiredField("control_id")
        if not isinstance(self.control_id, ControlRequirementControlId):
            self.control_id = ControlRequirementControlId(self.control_id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Decorator(YAMLRoot):
    """
    Cross-cutting annotation attached to nodes, relationships, or flows.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["Decorator"]
    class_class_curie: ClassVar[str] = "calm:Decorator"
    class_name: ClassVar[str] = "Decorator"
    class_model_uri: ClassVar[URIRef] = CALM.Decorator

    unique_id: Union[str, DecoratorUniqueId] = None
    type: str = None
    target: Union[str, list[str]] = None
    applies_to: Union[str, list[str]] = None
    data: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.unique_id):
            self.MissingRequiredField("unique_id")
        if not isinstance(self.unique_id, DecoratorUniqueId):
            self.unique_id = DecoratorUniqueId(self.unique_id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, list):
            self.target = [self.target] if self.target is not None else []
        self.target = [v if isinstance(v, str) else str(v) for v in self.target]

        if self._is_empty(self.applies_to):
            self.MissingRequiredField("applies_to")
        if not isinstance(self.applies_to, list):
            self.applies_to = [self.applies_to] if self.applies_to is not None else []
        self.applies_to = [v if isinstance(v, str) else str(v) for v in self.applies_to]

        if self._is_empty(self.data):
            self.MissingRequiredField("data")
        if not isinstance(self.data, str):
            self.data = str(self.data)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvidenceDocument(YAMLRoot):
    """
    Top-level CALM evidence document linking control configurations to evidence artefacts.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["EvidenceDocument"]
    class_class_curie: ClassVar[str] = "calm:EvidenceDocument"
    class_name: ClassVar[str] = "EvidenceDocument"
    class_model_uri: ClassVar[URIRef] = CALM.EvidenceDocument

    evidence: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.evidence):
            self.MissingRequiredField("evidence")
        if not isinstance(self.evidence, str):
            self.evidence = str(self.evidence)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Transition(YAMLRoot):
    """
    A single step in a flow, anchored on a relationship.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["Transition"]
    class_class_curie: ClassVar[str] = "calm:Transition"
    class_name: ClassVar[str] = "Transition"
    class_model_uri: ClassVar[URIRef] = CALM.Transition

    relationship_unique_id: str = None
    sequence_number: int = None
    description: str = None
    direction: Optional[Union[str, "TransitionDirection"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.relationship_unique_id):
            self.MissingRequiredField("relationship_unique_id")
        if not isinstance(self.relationship_unique_id, str):
            self.relationship_unique_id = str(self.relationship_unique_id)

        if self._is_empty(self.sequence_number):
            self.MissingRequiredField("sequence_number")
        if not isinstance(self.sequence_number, int):
            self.sequence_number = int(self.sequence_number)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.direction is not None and not isinstance(self.direction, TransitionDirection):
            self.direction = TransitionDirection(self.direction)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Flow(YAMLRoot):
    """
    Business flow mapped onto architecture relationships.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["Flow"]
    class_class_curie: ClassVar[str] = "calm:Flow"
    class_name: ClassVar[str] = "Flow"
    class_model_uri: ClassVar[URIRef] = CALM.Flow

    unique_id: Union[str, FlowUniqueId] = None
    name: str = None
    description: str = None
    transitions: Union[Union[dict, Transition], list[Union[dict, Transition]]] = None
    requirement_url: Optional[str] = None
    controls: Optional[Union[dict, Control]] = None
    metadata: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.unique_id):
            self.MissingRequiredField("unique_id")
        if not isinstance(self.unique_id, FlowUniqueId):
            self.unique_id = FlowUniqueId(self.unique_id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.transitions):
            self.MissingRequiredField("transitions")
        self._normalize_inlined_as_list(slot_name="transitions", slot_type=Transition, key_name="relationship_unique_id", keyed=False)

        if self.requirement_url is not None and not isinstance(self.requirement_url, str):
            self.requirement_url = str(self.requirement_url)

        if self.controls is not None and not isinstance(self.controls, Control):
            self.controls = Control()

        if self.metadata is not None and not isinstance(self.metadata, str):
            self.metadata = str(self.metadata)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InterfaceDefinition(YAMLRoot):
    """
    Modular interface definition referencing an external schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["InterfaceDefinition"]
    class_class_curie: ClassVar[str] = "calm:InterfaceDefinition"
    class_name: ClassVar[str] = "InterfaceDefinition"
    class_model_uri: ClassVar[URIRef] = CALM.InterfaceDefinition

    unique_id: Union[str, InterfaceDefinitionUniqueId] = None
    definition_url: str = None
    config: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.unique_id):
            self.MissingRequiredField("unique_id")
        if not isinstance(self.unique_id, InterfaceDefinitionUniqueId):
            self.unique_id = InterfaceDefinitionUniqueId(self.unique_id)

        if self._is_empty(self.definition_url):
            self.MissingRequiredField("definition_url")
        if not isinstance(self.definition_url, str):
            self.definition_url = str(self.definition_url)

        if self._is_empty(self.config):
            self.MissingRequiredField("config")
        if not isinstance(self.config, str):
            self.config = str(self.config)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InterfaceType(YAMLRoot):
    """
    Inline (free-form) interface definition keyed by unique-id.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["InterfaceType"]
    class_class_curie: ClassVar[str] = "calm:InterfaceType"
    class_name: ClassVar[str] = "InterfaceType"
    class_model_uri: ClassVar[URIRef] = CALM.InterfaceType

    unique_id: Union[str, InterfaceTypeUniqueId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.unique_id):
            self.MissingRequiredField("unique_id")
        if not isinstance(self.unique_id, InterfaceTypeUniqueId):
            self.unique_id = InterfaceTypeUniqueId(self.unique_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NodeInterface(YAMLRoot):
    """
    Reference to one or more interfaces exposed by a node.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["NodeInterface"]
    class_class_curie: ClassVar[str] = "calm:NodeInterface"
    class_name: ClassVar[str] = "NodeInterface"
    class_model_uri: ClassVar[URIRef] = CALM.NodeInterface

    node: str = None
    interfaces: Optional[Union[dict[Union[str, InterfaceDefinitionUniqueId], Union[dict, InterfaceDefinition]], list[Union[dict, InterfaceDefinition]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.node):
            self.MissingRequiredField("node")
        if not isinstance(self.node, str):
            self.node = str(self.node)

        self._normalize_inlined_as_list(slot_name="interfaces", slot_type=InterfaceDefinition, key_name="unique_id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Timeline(YAMLRoot):
    """
    CALM timeline document capturing architecture moments over time.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["Timeline"]
    class_class_curie: ClassVar[str] = "calm:Timeline"
    class_name: ClassVar[str] = "Timeline"
    class_model_uri: ClassVar[URIRef] = CALM.Timeline

    moments: Union[str, list[str]] = None
    current_moment: Optional[str] = None
    metadata: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.moments):
            self.MissingRequiredField("moments")
        if not isinstance(self.moments, list):
            self.moments = [self.moments] if self.moments is not None else []
        self.moments = [v if isinstance(v, str) else str(v) for v in self.moments]

        if self.current_moment is not None and not isinstance(self.current_moment, str):
            self.current_moment = str(self.current_moment)

        if self.metadata is not None and not isinstance(self.metadata, str):
            self.metadata = str(self.metadata)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NodeMoment(Node):
    """
    An architecture moment - a point-in-time snapshot of the architecture.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["NodeMoment"]
    class_class_curie: ClassVar[str] = "calm:NodeMoment"
    class_name: ClassVar[str] = "NodeMoment"
    class_model_uri: ClassVar[URIRef] = CALM.NodeMoment

    unique_id: Union[str, NodeMomentUniqueId] = None
    name: str = None
    description: str = None
    node_type: Union[str, "NodeType"] = None
    details: str = None
    valid_from: Optional[Union[str, XSDDate]] = None
    adrs: Optional[Union[str, list[str]]] = empty_list()
    interfaces: Optional[Union[Union[str, InterfaceDefinitionUniqueId], list[Union[str, InterfaceDefinitionUniqueId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.unique_id):
            self.MissingRequiredField("unique_id")
        if not isinstance(self.unique_id, NodeMomentUniqueId):
            self.unique_id = NodeMomentUniqueId(self.unique_id)

        if self._is_empty(self.node_type):
            self.MissingRequiredField("node_type")
        if not isinstance(self.node_type, NodeType):
            self.node_type = NodeType(self.node_type)

        if self._is_empty(self.details):
            self.MissingRequiredField("details")
        if not isinstance(self.details, str):
            self.details = str(self.details)

        if self.valid_from is not None and not isinstance(self.valid_from, XSDDate):
            self.valid_from = XSDDate(self.valid_from)

        if not isinstance(self.adrs, list):
            self.adrs = [self.adrs] if self.adrs is not None else []
        self.adrs = [v if isinstance(v, str) else str(v) for v in self.adrs]

        if not isinstance(self.interfaces, list):
            self.interfaces = [self.interfaces] if self.interfaces is not None else []
        self.interfaces = [v if isinstance(v, InterfaceDefinitionUniqueId) else InterfaceDefinitionUniqueId(v) for v in self.interfaces]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TimeUnit(YAMLRoot):
    """
    A quantity of time expressed as a numeric value and a unit.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["TimeUnit"]
    class_class_curie: ClassVar[str] = "calm:TimeUnit"
    class_name: ClassVar[str] = "TimeUnit"
    class_model_uri: ClassVar[URIRef] = CALM.TimeUnit

    unit: Union[str, "TimeUnitName"] = None
    value: float = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, TimeUnitName):
            self.unit = TimeUnitName(self.unit)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, float):
            self.value = float(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RateUnit(YAMLRoot):
    """
    A rate (count per time unit), e.g. operations per second.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["RateUnit"]
    class_class_curie: ClassVar[str] = "calm:RateUnit"
    class_name: ClassVar[str] = "RateUnit"
    class_model_uri: ClassVar[URIRef] = CALM.RateUnit

    rate: float = None
    per: Union[str, "RatePerUnit"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.rate):
            self.MissingRequiredField("rate")
        if not isinstance(self.rate, float):
            self.rate = float(self.rate)

        if self._is_empty(self.per):
            self.MissingRequiredField("per")
        if not isinstance(self.per, RatePerUnit):
            self.per = RatePerUnit(self.per)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OptionList(YAMLRoot):
    """
    Wrapper around the list of ``Decision`` alternatives in an options relationship.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["OptionList"]
    class_class_curie: ClassVar[str] = "calm:OptionList"
    class_name: ClassVar[str] = "OptionList"
    class_model_uri: ClassVar[URIRef] = CALM.OptionList

    decisions: Optional[Union[Union[dict, Decision], list[Union[dict, Decision]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="decisions", slot_type=Decision, key_name="description", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelationshipType(YAMLRoot):
    """
    Tagged-union container for the variant body of a relationship. Exactly one of ``interacts``, ``connects``,
    ``deployed_in``, ``composed_of``, ``options`` is populated; see ``RelationshipKind`` for the discriminator values.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["RelationshipType"]
    class_class_curie: ClassVar[str] = "calm:RelationshipType"
    class_name: ClassVar[str] = "RelationshipType"
    class_model_uri: ClassVar[URIRef] = CALM.RelationshipType

    interacts: Optional[Union[dict, InteractsRelationship]] = None
    connects: Optional[Union[dict, ConnectsRelationship]] = None
    deployed_in: Optional[Union[dict, DeployedInRelationship]] = None
    composed_of: Optional[Union[dict, ComposedOfRelationship]] = None
    options: Optional[Union[Union[dict, Decision], list[Union[dict, Decision]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.interacts is not None and not isinstance(self.interacts, InteractsRelationship):
            self.interacts = InteractsRelationship(**as_dict(self.interacts))

        if self.connects is not None and not isinstance(self.connects, ConnectsRelationship):
            self.connects = ConnectsRelationship(**as_dict(self.connects))

        if self.deployed_in is not None and not isinstance(self.deployed_in, DeployedInRelationship):
            self.deployed_in = DeployedInRelationship(**as_dict(self.deployed_in))

        if self.composed_of is not None and not isinstance(self.composed_of, ComposedOfRelationship):
            self.composed_of = ComposedOfRelationship(**as_dict(self.composed_of))

        self._normalize_inlined_as_list(slot_name="options", slot_type=Decision, key_name="description", keyed=False)

        super().__post_init__(**kwargs)


# Enumerations
class Protocol(EnumDefinitionImpl):
    """
    Wire-level protocol used by a relationship.
    """
    HTTP = PermissibleValue(
        text="HTTP",
        description="The HTTP protocol.",
        meaning=CALM["protocol/HTTP"])
    HTTPS = PermissibleValue(
        text="HTTPS",
        description="The HTTPS protocol.",
        meaning=CALM["protocol/HTTPS"])
    FTP = PermissibleValue(
        text="FTP",
        description="The FTP protocol.",
        meaning=CALM["protocol/FTP"])
    SFTP = PermissibleValue(
        text="SFTP",
        description="The SFTP protocol.",
        meaning=CALM["protocol/SFTP"])
    JDBC = PermissibleValue(
        text="JDBC",
        description="The JDBC protocol.",
        meaning=CALM["protocol/JDBC"])
    WebSocket = PermissibleValue(
        text="WebSocket",
        description="The WebSocket protocol.",
        meaning=CALM["protocol/WebSocket"])
    SocketIO = PermissibleValue(
        text="SocketIO",
        description="The SocketIO protocol.",
        meaning=CALM["protocol/SocketIO"])
    LDAP = PermissibleValue(
        text="LDAP",
        description="The LDAP protocol.",
        meaning=CALM["protocol/LDAP"])
    AMQP = PermissibleValue(
        text="AMQP",
        description="The AMQP protocol.",
        meaning=CALM["protocol/AMQP"])
    TLS = PermissibleValue(
        text="TLS",
        description="The TLS protocol.",
        meaning=CALM["protocol/TLS"])
    mTLS = PermissibleValue(
        text="mTLS",
        description="The mTLS protocol.",
        meaning=CALM["protocol/mTLS"])
    TCP = PermissibleValue(
        text="TCP",
        description="The TCP protocol.",
        meaning=CALM["protocol/TCP"])

    _defn = EnumDefinition(
        name="Protocol",
        description="Wire-level protocol used by a relationship.",
    )

class NodeType(EnumDefinitionImpl):
    """
    Category of architecture node. The CALM JSON-Schema allows arbitrary strings; this enum lists the canonical values
    plus an escape hatch via ``any_of`` on the slot.
    """
    actor = PermissibleValue(
        text="actor",
        description="A actor node.",
        meaning=CALM["node-type/actor"])
    ecosystem = PermissibleValue(
        text="ecosystem",
        description="A ecosystem node.",
        meaning=CALM["node-type/ecosystem"])
    system = PermissibleValue(
        text="system",
        description="A system node.",
        meaning=CALM["node-type/system"])
    service = PermissibleValue(
        text="service",
        description="A service node.",
        meaning=CALM["node-type/service"])
    database = PermissibleValue(
        text="database",
        description="A database node.",
        meaning=CALM["node-type/database"])
    network = PermissibleValue(
        text="network",
        description="A network node.",
        meaning=CALM["node-type/network"])
    ldap = PermissibleValue(
        text="ldap",
        description="A ldap node.",
        meaning=CALM["node-type/ldap"])
    webclient = PermissibleValue(
        text="webclient",
        description="A webclient node.",
        meaning=CALM["node-type/webclient"])
    data_asset = PermissibleValue(
        text="data_asset",
        description="A data-asset node.",
        meaning=CALM["node-type/data-asset"])

    _defn = EnumDefinition(
        name="NodeType",
        description="""Category of architecture node. The CALM JSON-Schema allows arbitrary strings; this enum lists the canonical values plus an escape hatch via ``any_of`` on the slot.""",
    )

class TimeUnitName(EnumDefinitionImpl):
    """
    Named unit of time used by ``TimeUnit``.
    """
    nanoseconds = PermissibleValue(
        text="nanoseconds",
        description="Time unit: nanoseconds.")
    microseconds = PermissibleValue(
        text="microseconds",
        description="Time unit: microseconds.")
    milliseconds = PermissibleValue(
        text="milliseconds",
        description="Time unit: milliseconds.")
    seconds = PermissibleValue(
        text="seconds",
        description="Time unit: seconds.")
    minutes = PermissibleValue(
        text="minutes",
        description="Time unit: minutes.")
    hours = PermissibleValue(
        text="hours",
        description="Time unit: hours.")
    days = PermissibleValue(
        text="days",
        description="Time unit: days.")
    weeks = PermissibleValue(
        text="weeks",
        description="Time unit: weeks.")
    months = PermissibleValue(
        text="months",
        description="Time unit: months.")
    quarters = PermissibleValue(
        text="quarters",
        description="Time unit: quarters.")
    years = PermissibleValue(
        text="years",
        description="Time unit: years.")

    _defn = EnumDefinition(
        name="TimeUnitName",
        description="Named unit of time used by ``TimeUnit``.",
    )

class RatePerUnit(EnumDefinitionImpl):
    """
    Time interval denominator used by ``RateUnit``.
    """
    nanosecond = PermissibleValue(
        text="nanosecond",
        description="Rate denominator: per nanosecond.")
    microsecond = PermissibleValue(
        text="microsecond",
        description="Rate denominator: per microsecond.")
    millisecond = PermissibleValue(
        text="millisecond",
        description="Rate denominator: per millisecond.")
    second = PermissibleValue(
        text="second",
        description="Rate denominator: per second.")
    minute = PermissibleValue(
        text="minute",
        description="Rate denominator: per minute.")
    hour = PermissibleValue(
        text="hour",
        description="Rate denominator: per hour.")
    day = PermissibleValue(
        text="day",
        description="Rate denominator: per day.")
    week = PermissibleValue(
        text="week",
        description="Rate denominator: per week.")
    month = PermissibleValue(
        text="month",
        description="Rate denominator: per month.")
    quarter = PermissibleValue(
        text="quarter",
        description="Rate denominator: per quarter.")
    year = PermissibleValue(
        text="year",
        description="Rate denominator: per year.")

    _defn = EnumDefinition(
        name="RatePerUnit",
        description="Time interval denominator used by ``RateUnit``.",
    )

class TransitionDirection(EnumDefinitionImpl):
    """
    Direction of flow on a transition.
    """
    source_to_destination = PermissibleValue(
        text="source_to_destination",
        description="Flow direction: source-to-destination.")
    destination_to_source = PermissibleValue(
        text="destination_to_source",
        description="Flow direction: destination-to-source.")

    _defn = EnumDefinition(
        name="TransitionDirection",
        description="Direction of flow on a transition.",
    )

class RelationshipKind(EnumDefinitionImpl):
    """
    Discriminator for the variant of a ``relationship-type``: exactly one of the following keys is set on a
    relationship's ``relationship-type``.
    """
    interacts = PermissibleValue(
        text="interacts",
        description="Actor-to-nodes interaction.")
    connects = PermissibleValue(
        text="connects",
        description="Interface-to-interface connection.")
    deployed_in = PermissibleValue(
        text="deployed_in",
        description="Containment: nodes deployed in a container.")
    composed_of = PermissibleValue(
        text="composed_of",
        description="Composition: nodes composed by a container.")
    options = PermissibleValue(
        text="options",
        description="A set of alternative decisions.")

    _defn = EnumDefinition(
        name="RelationshipKind",
        description="""Discriminator for the variant of a ``relationship-type``: exactly one of the following keys is set on a relationship's ``relationship-type``.""",
    )

# Slots
class slots:
    pass

slots.nodes = Slot(uri=CALM.nodes, name="nodes", curie=CALM.curie('nodes'),
                   model_uri=CALM.nodes, domain=None, range=Optional[Union[Union[str, NodeUniqueId], list[Union[str, NodeUniqueId]]]])

slots.relationships = Slot(uri=CALM.relationships, name="relationships", curie=CALM.curie('relationships'),
                   model_uri=CALM.relationships, domain=None, range=Optional[Union[Union[str, RelationshipUniqueId], list[Union[str, RelationshipUniqueId]]]])

slots.metadata = Slot(uri=CALM.metadata, name="metadata", curie=CALM.curie('metadata'),
                   model_uri=CALM.metadata, domain=None, range=Optional[str])

slots.controls = Slot(uri=CALM.controls, name="controls", curie=CALM.curie('controls'),
                   model_uri=CALM.controls, domain=None, range=Optional[Union[dict, Control]])

slots.flows = Slot(uri=CALM.flows, name="flows", curie=CALM.curie('flows'),
                   model_uri=CALM.flows, domain=None, range=Optional[Union[Union[str, FlowUniqueId], list[Union[str, FlowUniqueId]]]])

slots.adrs = Slot(uri=CALM.adrs, name="adrs", curie=CALM.curie('adrs'),
                   model_uri=CALM.adrs, domain=None, range=Optional[Union[str, list[str]]])

slots.unique_id = Slot(uri=SCHEMA.identifier, name="unique_id", curie=SCHEMA.curie('identifier'),
                   model_uri=CALM.unique_id, domain=None, range=URIRef)

slots.node_type = Slot(uri=CALM.node_type, name="node_type", curie=CALM.curie('node_type'),
                   model_uri=CALM.node_type, domain=None, range=Union[str, "NodeType"])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=CALM.name, domain=None, range=str)

slots.description = Slot(uri=DCT.description, name="description", curie=DCT.curie('description'),
                   model_uri=CALM.description, domain=None, range=Optional[str])

slots.details = Slot(uri=CALM.details, name="details", curie=CALM.curie('details'),
                   model_uri=CALM.details, domain=None, range=Optional[str])

slots.interfaces = Slot(uri=CALM.interfaces, name="interfaces", curie=CALM.curie('interfaces'),
                   model_uri=CALM.interfaces, domain=None, range=Optional[Union[Union[str, InterfaceDefinitionUniqueId], list[Union[str, InterfaceDefinitionUniqueId]]]])

slots.relationship_type = Slot(uri=CALM.relationship_type, name="relationship_type", curie=CALM.curie('relationship_type'),
                   model_uri=CALM.relationship_type, domain=None, range=Union[dict, RelationshipType])

slots.protocol = Slot(uri=CALM.protocol, name="protocol", curie=CALM.curie('protocol'),
                   model_uri=CALM.protocol, domain=None, range=Optional[Union[str, "Protocol"]])

slots.actor = Slot(uri=CALM.actor, name="actor", curie=CALM.curie('actor'),
                   model_uri=CALM.actor, domain=None, range=str)

slots.source = Slot(uri=CALM.source, name="source", curie=CALM.curie('source'),
                   model_uri=CALM.source, domain=None, range=Union[dict, NodeInterface])

slots.destination = Slot(uri=CALM.destination, name="destination", curie=CALM.curie('destination'),
                   model_uri=CALM.destination, domain=None, range=Union[dict, NodeInterface])

slots.container = Slot(uri=CALM.container, name="container", curie=CALM.curie('container'),
                   model_uri=CALM.container, domain=None, range=str)

slots.requirement_url = Slot(uri=SCHEMA.url, name="requirement_url", curie=SCHEMA.curie('url'),
                   model_uri=CALM.requirement_url, domain=None, range=Optional[str])

slots.config_url = Slot(uri=SCHEMA.url, name="config_url", curie=SCHEMA.curie('url'),
                   model_uri=CALM.config_url, domain=None, range=Optional[str])

slots.config = Slot(uri=CALM.config, name="config", curie=CALM.curie('config'),
                   model_uri=CALM.config, domain=None, range=Optional[str])

slots.control_id = Slot(uri=CALM.control_id, name="control_id", curie=CALM.curie('control_id'),
                   model_uri=CALM.control_id, domain=None, range=URIRef)

slots.type = Slot(uri=CALM.type, name="type", curie=CALM.curie('type'),
                   model_uri=CALM.type, domain=None, range=str)

slots.target = Slot(uri=CALM.target, name="target", curie=CALM.curie('target'),
                   model_uri=CALM.target, domain=None, range=Union[str, list[str]])

slots.applies_to = Slot(uri=CALM.applies_to, name="applies_to", curie=CALM.curie('applies_to'),
                   model_uri=CALM.applies_to, domain=None, range=Union[str, list[str]])

slots.data = Slot(uri=CALM.data, name="data", curie=CALM.curie('data'),
                   model_uri=CALM.data, domain=None, range=str)

slots.evidence = Slot(uri=CALM.evidence, name="evidence", curie=CALM.curie('evidence'),
                   model_uri=CALM.evidence, domain=None, range=str)

slots.relationship_unique_id = Slot(uri=CALM.relationship_unique_id, name="relationship_unique_id", curie=CALM.curie('relationship_unique_id'),
                   model_uri=CALM.relationship_unique_id, domain=None, range=str)

slots.sequence_number = Slot(uri=CALM.sequence_number, name="sequence_number", curie=CALM.curie('sequence_number'),
                   model_uri=CALM.sequence_number, domain=None, range=int)

slots.direction = Slot(uri=CALM.direction, name="direction", curie=CALM.curie('direction'),
                   model_uri=CALM.direction, domain=None, range=Optional[Union[str, "TransitionDirection"]])

slots.transitions = Slot(uri=CALM.transitions, name="transitions", curie=CALM.curie('transitions'),
                   model_uri=CALM.transitions, domain=None, range=Union[Union[dict, Transition], list[Union[dict, Transition]]])

slots.definition_url = Slot(uri=SCHEMA.url, name="definition_url", curie=SCHEMA.curie('url'),
                   model_uri=CALM.definition_url, domain=None, range=str)

slots.node = Slot(uri=CALM.node, name="node", curie=CALM.curie('node'),
                   model_uri=CALM.node, domain=None, range=str)

slots.current_moment = Slot(uri=CALM.current_moment, name="current_moment", curie=CALM.curie('current_moment'),
                   model_uri=CALM.current_moment, domain=None, range=Optional[str])

slots.moments = Slot(uri=CALM.moments, name="moments", curie=CALM.curie('moments'),
                   model_uri=CALM.moments, domain=None, range=Union[str, list[str]])

slots.valid_from = Slot(uri=PROV.startedAtTime, name="valid_from", curie=PROV.curie('startedAtTime'),
                   model_uri=CALM.valid_from, domain=None, range=Optional[Union[str, XSDDate]])

slots.unit = Slot(uri=CALM.unit, name="unit", curie=CALM.curie('unit'),
                   model_uri=CALM.unit, domain=None, range=Union[str, "TimeUnitName"])

slots.value = Slot(uri=CALM.value, name="value", curie=CALM.curie('value'),
                   model_uri=CALM.value, domain=None, range=float)

slots.rate = Slot(uri=CALM.rate, name="rate", curie=CALM.curie('rate'),
                   model_uri=CALM.rate, domain=None, range=float)

slots.per = Slot(uri=CALM.per, name="per", curie=CALM.curie('per'),
                   model_uri=CALM.per, domain=None, range=Union[str, "RatePerUnit"])

slots.url = Slot(uri=SCHEMA.url, name="url", curie=SCHEMA.curie('url'),
                   model_uri=CALM.url, domain=None, range=Optional[str])

slots.control_config_url = Slot(uri=SCHEMA.url, name="control_config_url", curie=SCHEMA.curie('url'),
                   model_uri=CALM.control_config_url, domain=None, range=Optional[str])

slots.evidence_paths = Slot(uri=CALM.evidence_paths, name="evidence_paths", curie=CALM.curie('evidence_paths'),
                   model_uri=CALM.evidence_paths, domain=None, range=Optional[Union[str, list[str]]])

slots.decisions = Slot(uri=CALM.decisions, name="decisions", curie=CALM.curie('decisions'),
                   model_uri=CALM.decisions, domain=None, range=Optional[Union[Union[dict, Decision], list[Union[dict, Decision]]]])

slots.interacts = Slot(uri=CALM.interacts, name="interacts", curie=CALM.curie('interacts'),
                   model_uri=CALM.interacts, domain=None, range=Optional[Union[dict, InteractsRelationship]])

slots.connects = Slot(uri=CALM.connects, name="connects", curie=CALM.curie('connects'),
                   model_uri=CALM.connects, domain=None, range=Optional[Union[dict, ConnectsRelationship]])

slots.deployed_in = Slot(uri=CALM.deployed_in, name="deployed_in", curie=CALM.curie('deployed_in'),
                   model_uri=CALM.deployed_in, domain=None, range=Optional[Union[dict, DeployedInRelationship]])

slots.composed_of = Slot(uri=CALM.composed_of, name="composed_of", curie=CALM.curie('composed_of'),
                   model_uri=CALM.composed_of, domain=None, range=Optional[Union[dict, ComposedOfRelationship]])

slots.options = Slot(uri=CALM.options, name="options", curie=CALM.curie('options'),
                   model_uri=CALM.options, domain=None, range=Optional[Union[Union[dict, Decision], list[Union[dict, Decision]]]])

slots.Architecture_nodes = Slot(uri=CALM.nodes, name="Architecture_nodes", curie=CALM.curie('nodes'),
                   model_uri=CALM.Architecture_nodes, domain=Architecture, range=Optional[Union[dict[Union[str, NodeUniqueId], Union[dict, "Node"]], list[Union[dict, "Node"]]]])

slots.Architecture_relationships = Slot(uri=CALM.relationships, name="Architecture_relationships", curie=CALM.curie('relationships'),
                   model_uri=CALM.Architecture_relationships, domain=Architecture, range=Optional[Union[dict[Union[str, RelationshipUniqueId], Union[dict, "Relationship"]], list[Union[dict, "Relationship"]]]])

slots.Architecture_flows = Slot(uri=CALM.flows, name="Architecture_flows", curie=CALM.curie('flows'),
                   model_uri=CALM.Architecture_flows, domain=Architecture, range=Optional[Union[dict[Union[str, FlowUniqueId], Union[dict, "Flow"]], list[Union[dict, "Flow"]]]])

slots.Node_interfaces = Slot(uri=CALM.interfaces, name="Node_interfaces", curie=CALM.curie('interfaces'),
                   model_uri=CALM.Node_interfaces, domain=Node, range=Optional[Union[dict[Union[str, InterfaceDefinitionUniqueId], Union[dict, "InterfaceDefinition"]], list[Union[dict, "InterfaceDefinition"]]]])

slots.Node_description = Slot(uri=DCT.description, name="Node_description", curie=DCT.curie('description'),
                   model_uri=CALM.Node_description, domain=Node, range=str)

slots.InteractsRelationship_nodes = Slot(uri=CALM.nodes, name="InteractsRelationship_nodes", curie=CALM.curie('nodes'),
                   model_uri=CALM.InteractsRelationship_nodes, domain=InteractsRelationship, range=Union[Union[str, NodeUniqueId], list[Union[str, NodeUniqueId]]])

slots.DeployedInRelationship_nodes = Slot(uri=CALM.nodes, name="DeployedInRelationship_nodes", curie=CALM.curie('nodes'),
                   model_uri=CALM.DeployedInRelationship_nodes, domain=DeployedInRelationship, range=Union[Union[str, NodeUniqueId], list[Union[str, NodeUniqueId]]])

slots.ComposedOfRelationship_nodes = Slot(uri=CALM.nodes, name="ComposedOfRelationship_nodes", curie=CALM.curie('nodes'),
                   model_uri=CALM.ComposedOfRelationship_nodes, domain=ComposedOfRelationship, range=Union[Union[str, NodeUniqueId], list[Union[str, NodeUniqueId]]])

slots.Decision_nodes = Slot(uri=CALM.nodes, name="Decision_nodes", curie=CALM.curie('nodes'),
                   model_uri=CALM.Decision_nodes, domain=Decision, range=Union[dict[Union[str, NodeUniqueId], Union[dict, Node]], list[Union[dict, Node]]])

slots.Decision_relationships = Slot(uri=CALM.relationships, name="Decision_relationships", curie=CALM.curie('relationships'),
                   model_uri=CALM.Decision_relationships, domain=Decision, range=Union[dict[Union[str, RelationshipUniqueId], Union[dict, Relationship]], list[Union[dict, Relationship]]])

slots.Decision_description = Slot(uri=DCT.description, name="Decision_description", curie=DCT.curie('description'),
                   model_uri=CALM.Decision_description, domain=Decision, range=str)

slots.ControlDetail_requirement_url = Slot(uri=SCHEMA.url, name="ControlDetail_requirement_url", curie=SCHEMA.curie('url'),
                   model_uri=CALM.ControlDetail_requirement_url, domain=ControlDetail, range=str)

slots.ControlRequirement_description = Slot(uri=DCT.description, name="ControlRequirement_description", curie=DCT.curie('description'),
                   model_uri=CALM.ControlRequirement_description, domain=ControlRequirement, range=str)

slots.Transition_description = Slot(uri=DCT.description, name="Transition_description", curie=DCT.curie('description'),
                   model_uri=CALM.Transition_description, domain=Transition, range=str)

slots.Flow_description = Slot(uri=DCT.description, name="Flow_description", curie=DCT.curie('description'),
                   model_uri=CALM.Flow_description, domain=Flow, range=str)

slots.InterfaceDefinition_config = Slot(uri=CALM.config, name="InterfaceDefinition_config", curie=CALM.curie('config'),
                   model_uri=CALM.InterfaceDefinition_config, domain=InterfaceDefinition, range=str)

slots.NodeInterface_interfaces = Slot(uri=CALM.interfaces, name="NodeInterface_interfaces", curie=CALM.curie('interfaces'),
                   model_uri=CALM.NodeInterface_interfaces, domain=NodeInterface, range=Optional[Union[dict[Union[str, InterfaceDefinitionUniqueId], Union[dict, InterfaceDefinition]], list[Union[dict, InterfaceDefinition]]]])

slots.NodeMoment_details = Slot(uri=CALM.details, name="NodeMoment_details", curie=CALM.curie('details'),
                   model_uri=CALM.NodeMoment_details, domain=NodeMoment, range=str)
