# Auto generated from calm.yaml by pythongen.py version: 0.0.1
# Schema: calm
#
# id: https://w3id.org/lmodel/calm
# description: A LinkML model of CALM 1.3, the Common Architecture Language Model of FINOS's Architecture as Code project. Each module renders one file of the CALM Meta Schema and keeps CALM's keys, so a CALM document validates here unchanged, and CALM's JSON Schema files can be generated from the model.
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

metamodel_version = "1.12.0"
version = "1.3"

# Namespaces
CALM = CurieNamespace('calm', 'https://w3id.org/lmodel/calm/')
CALM_META = CurieNamespace('calm_meta', 'https://calm.finos.org/release/1.3/meta/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CALM


# Types
class CalmCronExpression(String):
    """ A valid Unix-style cron expression. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "CalmCronExpression"
    type_model_uri = CALM.CalmCronExpression


# Class references



@dataclass(repr=False)
class CalmArchitecture(YAMLRoot):
    """
    A CALM architecture document: the nodes of a system, the relationships between them, its business flows, and the
    controls that apply to it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmArchitecture"]
    class_class_curie: ClassVar[str] = "calm:CalmArchitecture"
    class_name: ClassVar[str] = "CalmArchitecture"
    class_model_uri: ClassVar[URIRef] = CALM.CalmArchitecture

    nodes: Optional[Union[Union[dict, "CalmNode"], list[Union[dict, "CalmNode"]]]] = empty_list()
    relationships: Optional[Union[Union[dict, "CalmRelationship"], list[Union[dict, "CalmRelationship"]]]] = empty_list()
    metadata: Optional[Union[dict, "CalmMetadata"]] = None
    controls: Optional[Union[dict, "CalmControls"]] = None
    flows: Optional[Union[Union[dict, "CalmFlow"], list[Union[dict, "CalmFlow"]]]] = empty_list()
    adrs: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="nodes", slot_type=CalmNode, key_name="unique-id", keyed=False)

        self._normalize_inlined_as_list(slot_name="relationships", slot_type=CalmRelationship, key_name="unique-id", keyed=False)

        if self.controls is not None and not isinstance(self.controls, CalmControls):
            self.controls = CalmControls()

        self._normalize_inlined_as_list(slot_name="flows", slot_type=CalmFlow, key_name="unique-id", keyed=False)

        if not isinstance(self.adrs, list):
            self.adrs = [self.adrs] if self.adrs is not None else []
        self.adrs = [v if isinstance(v, str) else str(v) for v in self.adrs]

        super().__post_init__(**kwargs)


class CalmControls(YAMLRoot):
    """
    The controls that apply to an architecture element, each under a key of letters, digits and hyphens.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmControls"]
    class_class_curie: ClassVar[str] = "calm:CalmControls"
    class_name: ClassVar[str] = "CalmControls"
    class_model_uri: ClassVar[URIRef] = CALM.CalmControls


@dataclass(repr=False)
class CalmControl(YAMLRoot):
    """
    One control in a controls map, with the requirements that define it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmControl"]
    class_class_curie: ClassVar[str] = "calm:CalmControl"
    class_name: ClassVar[str] = "CalmControl"
    class_model_uri: ClassVar[URIRef] = CALM.CalmControl

    description: str = None
    requirements: Union[Union[dict, "CalmControlDetail"], list[Union[dict, "CalmControlDetail"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.requirements):
            self.MissingRequiredField("requirements")
        self._normalize_inlined_as_list(slot_name="requirements", slot_type=CalmControlDetail, key_name="requirement-url", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CalmControlDetail(YAMLRoot):
    """
    A control requirement this control applies, with its configuration given by address or inline, but not both.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmControlDetail"]
    class_class_curie: ClassVar[str] = "calm:CalmControlDetail"
    class_name: ClassVar[str] = "CalmControlDetail"
    class_model_uri: ClassVar[URIRef] = CALM.CalmControlDetail

    requirement_url: str = None
    config_url: Optional[str] = None
    config: Optional[Union[dict, "CalmControlConfig"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.requirement_url):
            self.MissingRequiredField("requirement_url")
        if not isinstance(self.requirement_url, str):
            self.requirement_url = str(self.requirement_url)

        if self.config_url is not None and not isinstance(self.config_url, str):
            self.config_url = str(self.config_url)

        if self.config is not None and not isinstance(self.config, CalmControlConfig):
            self.config = CalmControlConfig()

        super().__post_init__(**kwargs)


class CalmControlConfig(YAMLRoot):
    """
    A configuration object, free in shape, that meets a control requirement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmControlConfig"]
    class_class_curie: ClassVar[str] = "calm:CalmControlConfig"
    class_name: ClassVar[str] = "CalmControlConfig"
    class_model_uri: ClassVar[URIRef] = CALM.CalmControlConfig


@dataclass(repr=False)
class CalmInterfaceDefinition(YAMLRoot):
    """
    A modular interface definition referencing an external schema
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmInterfaceDefinition"]
    class_class_curie: ClassVar[str] = "calm:CalmInterfaceDefinition"
    class_name: ClassVar[str] = "CalmInterfaceDefinition"
    class_model_uri: ClassVar[URIRef] = CALM.CalmInterfaceDefinition

    unique_id: str = None
    definition_url: str = None
    config: Union[dict, "CalmInterfaceConfig"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.unique_id):
            self.MissingRequiredField("unique_id")
        if not isinstance(self.unique_id, str):
            self.unique_id = str(self.unique_id)

        if self._is_empty(self.definition_url):
            self.MissingRequiredField("definition_url")
        if not isinstance(self.definition_url, str):
            self.definition_url = str(self.definition_url)

        if self._is_empty(self.config):
            self.MissingRequiredField("config")
        if not isinstance(self.config, CalmInterfaceConfig):
            self.config = CalmInterfaceConfig()

        super().__post_init__(**kwargs)


class CalmInterfaceConfig(YAMLRoot):
    """
    A configuration object, free in shape, that an interface definition's schema checks.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmInterfaceConfig"]
    class_class_curie: ClassVar[str] = "calm:CalmInterfaceConfig"
    class_name: ClassVar[str] = "CalmInterfaceConfig"
    class_model_uri: ClassVar[URIRef] = CALM.CalmInterfaceConfig


@dataclass(repr=False)
class CalmInterfaceType(YAMLRoot):
    """
    An interface given by its own keys, such as a host and port, rather than by an external schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmInterfaceType"]
    class_class_curie: ClassVar[str] = "calm:CalmInterfaceType"
    class_name: ClassVar[str] = "CalmInterfaceType"
    class_model_uri: ClassVar[URIRef] = CALM.CalmInterfaceType

    unique_id: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.unique_id):
            self.MissingRequiredField("unique_id")
        if not isinstance(self.unique_id, str):
            self.unique_id = str(self.unique_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CalmNodeInterface(YAMLRoot):
    """
    One end of a connection, naming a node and, optionally, which of its interfaces.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmNodeInterface"]
    class_class_curie: ClassVar[str] = "calm:CalmNodeInterface"
    class_name: ClassVar[str] = "CalmNodeInterface"
    class_model_uri: ClassVar[URIRef] = CALM.CalmNodeInterface

    node: str = None
    interfaces: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.node):
            self.MissingRequiredField("node")
        if not isinstance(self.node, str):
            self.node = str(self.node)

        if not isinstance(self.interfaces, list):
            self.interfaces = [self.interfaces] if self.interfaces is not None else []
        self.interfaces = [v if isinstance(v, str) else str(v) for v in self.interfaces]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CalmNode(YAMLRoot):
    """
    A component of the architecture, such as a system, service, database or actor, with its interfaces and controls.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmNode"]
    class_class_curie: ClassVar[str] = "calm:CalmNode"
    class_name: ClassVar[str] = "CalmNode"
    class_model_uri: ClassVar[URIRef] = CALM.CalmNode

    unique_id: str = None
    node_type: Union[str, "CalmNodeTypeDefinition"] = None
    name: str = None
    description: str = None
    details: Optional[Union[dict, "CalmNodeDetails"]] = None
    interfaces: Optional[Union[str, list[str]]] = empty_list()
    controls: Optional[Union[dict, CalmControls]] = None
    metadata: Optional[Union[dict, "CalmMetadata"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.unique_id):
            self.MissingRequiredField("unique_id")
        if not isinstance(self.unique_id, str):
            self.unique_id = str(self.unique_id)

        if self._is_empty(self.node_type):
            self.MissingRequiredField("node_type")
        if not isinstance(self.node_type, (CalmNodeTypeDefinition, str)):
            value = self.node_type
            for _coerce in (lambda: CalmNodeTypeDefinition(value), lambda: str(value)):
                try:
                    self.node_type = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[CalmNodeTypeDefinition, str] could be constructed from {value!r} for slot node_type")

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.details is not None and not isinstance(self.details, CalmNodeDetails):
            self.details = CalmNodeDetails(**as_dict(self.details))

        if not isinstance(self.interfaces, list):
            self.interfaces = [self.interfaces] if self.interfaces is not None else []
        self.interfaces = [v if isinstance(v, str) else str(v) for v in self.interfaces]

        if self.controls is not None and not isinstance(self.controls, CalmControls):
            self.controls = CalmControls()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CalmNodeDetails(YAMLRoot):
    """
    References from a node to a more detailed architecture and to the pattern it must follow.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmNodeDetails"]
    class_class_curie: ClassVar[str] = "calm:CalmNodeDetails"
    class_name: ClassVar[str] = "CalmNodeDetails"
    class_model_uri: ClassVar[URIRef] = CALM.CalmNodeDetails

    detailed_architecture: Optional[str] = None
    required_pattern: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.detailed_architecture is not None and not isinstance(self.detailed_architecture, str):
            self.detailed_architecture = str(self.detailed_architecture)

        if self.required_pattern is not None and not isinstance(self.required_pattern, str):
            self.required_pattern = str(self.required_pattern)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CalmRelationship(YAMLRoot):
    """
    A link between nodes, of one of CALM's kinds, or a choice between options.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmRelationship"]
    class_class_curie: ClassVar[str] = "calm:CalmRelationship"
    class_name: ClassVar[str] = "CalmRelationship"
    class_model_uri: ClassVar[URIRef] = CALM.CalmRelationship

    unique_id: str = None
    relationship_type: Union[dict, "CalmRelationshipType"] = None
    description: Optional[str] = None
    protocol: Optional[Union[str, "CalmProtocol"]] = None
    metadata: Optional[Union[dict, "CalmMetadata"]] = None
    controls: Optional[Union[dict, CalmControls]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.unique_id):
            self.MissingRequiredField("unique_id")
        if not isinstance(self.unique_id, str):
            self.unique_id = str(self.unique_id)

        if self._is_empty(self.relationship_type):
            self.MissingRequiredField("relationship_type")
        if not isinstance(self.relationship_type, CalmRelationshipType):
            self.relationship_type = CalmRelationshipType(**as_dict(self.relationship_type))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.protocol is not None and not isinstance(self.protocol, CalmProtocol):
            self.protocol = CalmProtocol(self.protocol)

        if self.controls is not None and not isinstance(self.controls, CalmControls):
            self.controls = CalmControls()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CalmRelationshipType(YAMLRoot):
    """
    The kind of a relationship, given by exactly one of its keys: interacts, connects, deployed-in, composed-of or
    options.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmRelationshipType"]
    class_class_curie: ClassVar[str] = "calm:CalmRelationshipType"
    class_name: ClassVar[str] = "CalmRelationshipType"
    class_model_uri: ClassVar[URIRef] = CALM.CalmRelationshipType

    interacts: Optional[Union[dict, "CalmInteractsType"]] = None
    connects: Optional[Union[dict, "CalmConnectsType"]] = None
    deployed_in: Optional[Union[dict, "CalmDeployedInType"]] = None
    composed_of: Optional[Union[dict, "CalmComposedOfType"]] = None
    options: Optional[Union[Union[dict, "CalmDecision"], list[Union[dict, "CalmDecision"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.interacts is not None and not isinstance(self.interacts, CalmInteractsType):
            self.interacts = CalmInteractsType(**as_dict(self.interacts))

        if self.connects is not None and not isinstance(self.connects, CalmConnectsType):
            self.connects = CalmConnectsType(**as_dict(self.connects))

        if self.deployed_in is not None and not isinstance(self.deployed_in, CalmDeployedInType):
            self.deployed_in = CalmDeployedInType(**as_dict(self.deployed_in))

        if self.composed_of is not None and not isinstance(self.composed_of, CalmComposedOfType):
            self.composed_of = CalmComposedOfType(**as_dict(self.composed_of))

        self._normalize_inlined_as_list(slot_name="options", slot_type=CalmDecision, key_name="description", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CalmInteractsType(YAMLRoot):
    """
    A relationship in which an actor interacts with nodes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmInteractsType"]
    class_class_curie: ClassVar[str] = "calm:CalmInteractsType"
    class_name: ClassVar[str] = "CalmInteractsType"
    class_model_uri: ClassVar[URIRef] = CALM.CalmInteractsType

    actor: str = None
    nodes: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.actor):
            self.MissingRequiredField("actor")
        if not isinstance(self.actor, str):
            self.actor = str(self.actor)

        if self._is_empty(self.nodes):
            self.MissingRequiredField("nodes")
        if not isinstance(self.nodes, list):
            self.nodes = [self.nodes] if self.nodes is not None else []
        self.nodes = [v if isinstance(v, str) else str(v) for v in self.nodes]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CalmConnectsType(YAMLRoot):
    """
    A relationship in which one node connects to another through their interfaces.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmConnectsType"]
    class_class_curie: ClassVar[str] = "calm:CalmConnectsType"
    class_name: ClassVar[str] = "CalmConnectsType"
    class_model_uri: ClassVar[URIRef] = CALM.CalmConnectsType

    source_end: Union[dict, CalmNodeInterface] = None
    destination_end: Union[dict, CalmNodeInterface] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source_end):
            self.MissingRequiredField("source_end")
        if not isinstance(self.source_end, CalmNodeInterface):
            self.source_end = CalmNodeInterface(**as_dict(self.source_end))

        if self._is_empty(self.destination_end):
            self.MissingRequiredField("destination_end")
        if not isinstance(self.destination_end, CalmNodeInterface):
            self.destination_end = CalmNodeInterface(**as_dict(self.destination_end))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CalmDeployedInType(YAMLRoot):
    """
    A relationship in which nodes are deployed in a container node.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmDeployedInType"]
    class_class_curie: ClassVar[str] = "calm:CalmDeployedInType"
    class_name: ClassVar[str] = "CalmDeployedInType"
    class_model_uri: ClassVar[URIRef] = CALM.CalmDeployedInType

    container: str = None
    nodes: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.container):
            self.MissingRequiredField("container")
        if not isinstance(self.container, str):
            self.container = str(self.container)

        if self._is_empty(self.nodes):
            self.MissingRequiredField("nodes")
        if not isinstance(self.nodes, list):
            self.nodes = [self.nodes] if self.nodes is not None else []
        self.nodes = [v if isinstance(v, str) else str(v) for v in self.nodes]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CalmComposedOfType(YAMLRoot):
    """
    A relationship in which nodes make up a container node.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmComposedOfType"]
    class_class_curie: ClassVar[str] = "calm:CalmComposedOfType"
    class_name: ClassVar[str] = "CalmComposedOfType"
    class_model_uri: ClassVar[URIRef] = CALM.CalmComposedOfType

    container: str = None
    nodes: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.container):
            self.MissingRequiredField("container")
        if not isinstance(self.container, str):
            self.container = str(self.container)

        if self._is_empty(self.nodes):
            self.MissingRequiredField("nodes")
        if not isinstance(self.nodes, list):
            self.nodes = [self.nodes] if self.nodes is not None else []
        self.nodes = [v if isinstance(v, str) else str(v) for v in self.nodes]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CalmDecision(YAMLRoot):
    """
    One option of a choice, naming the nodes, relationships and controls it would add.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmDecision"]
    class_class_curie: ClassVar[str] = "calm:CalmDecision"
    class_name: ClassVar[str] = "CalmDecision"
    class_model_uri: ClassVar[URIRef] = CALM.CalmDecision

    description: str = None
    nodes: Union[str, list[str]] = None
    relationships: Union[str, list[str]] = None
    controls: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.nodes):
            self.MissingRequiredField("nodes")
        if not isinstance(self.nodes, list):
            self.nodes = [self.nodes] if self.nodes is not None else []
        self.nodes = [v if isinstance(v, str) else str(v) for v in self.nodes]

        if self._is_empty(self.relationships):
            self.MissingRequiredField("relationships")
        if not isinstance(self.relationships, list):
            self.relationships = [self.relationships] if self.relationships is not None else []
        self.relationships = [v if isinstance(v, str) else str(v) for v in self.relationships]

        if not isinstance(self.controls, list):
            self.controls = [self.controls] if self.controls is not None else []
        self.controls = [v if isinstance(v, str) else str(v) for v in self.controls]

        super().__post_init__(**kwargs)


CalmMetadata = Any

@dataclass(repr=False)
class CalmFlow(YAMLRoot):
    """
    A business flow, as an ordered list of transitions across the architecture's relationships.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmFlow"]
    class_class_curie: ClassVar[str] = "calm:CalmFlow"
    class_name: ClassVar[str] = "CalmFlow"
    class_model_uri: ClassVar[URIRef] = CALM.CalmFlow

    unique_id: str = None
    name: str = None
    description: str = None
    transitions: Union[Union[dict, "CalmTransition"], list[Union[dict, "CalmTransition"]]] = None
    requirement_url: Optional[str] = None
    controls: Optional[Union[dict, CalmControls]] = None
    metadata: Optional[Union[dict, CalmMetadata]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.unique_id):
            self.MissingRequiredField("unique_id")
        if not isinstance(self.unique_id, str):
            self.unique_id = str(self.unique_id)

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
        self._normalize_inlined_as_list(slot_name="transitions", slot_type=CalmTransition, key_name="relationship-unique-id", keyed=False)

        if self.requirement_url is not None and not isinstance(self.requirement_url, str):
            self.requirement_url = str(self.requirement_url)

        if self.controls is not None and not isinstance(self.controls, CalmControls):
            self.controls = CalmControls()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CalmTransition(YAMLRoot):
    """
    One step of a flow, across one relationship of the architecture.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmTransition"]
    class_class_curie: ClassVar[str] = "calm:CalmTransition"
    class_name: ClassVar[str] = "CalmTransition"
    class_model_uri: ClassVar[URIRef] = CALM.CalmTransition

    relationship_unique_id: str = None
    sequence_number: int = None
    description: str = None
    direction: Optional[Union[str, "CalmTransitionDirection"]] = 'source-to-destination'

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

        if self.direction is not None and not isinstance(self.direction, CalmTransitionDirection):
            self.direction = CalmTransitionDirection(self.direction)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CalmTimeline(YAMLRoot):
    """
    A timeline document, listing the moments of an architecture and naming the current one.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmTimeline"]
    class_class_curie: ClassVar[str] = "calm:CalmTimeline"
    class_name: ClassVar[str] = "CalmTimeline"
    class_model_uri: ClassVar[URIRef] = CALM.CalmTimeline

    moments: Union[Union[dict, "CalmNodeMoment"], list[Union[dict, "CalmNodeMoment"]]] = None
    current_moment: Optional[str] = None
    metadata: Optional[Union[dict, CalmMetadata]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.moments):
            self.MissingRequiredField("moments")
        self._normalize_inlined_as_list(slot_name="moments", slot_type=CalmNodeMoment, key_name="unique-id", keyed=False)

        if self.current_moment is not None and not isinstance(self.current_moment, str):
            self.current_moment = str(self.current_moment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CalmNodeMoment(CalmNode):
    """
    A moment of a timeline: a node of type moment, with no interfaces, whose details point to the architecture of that
    moment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmNodeMoment"]
    class_class_curie: ClassVar[str] = "calm:CalmNodeMoment"
    class_name: ClassVar[str] = "CalmNodeMoment"
    class_model_uri: ClassVar[URIRef] = CALM.CalmNodeMoment

    unique_id: str = None
    node_type: Union[str, "CalmNodeTypeDefinition"] = None
    name: str = None
    description: str = None
    valid_from: Optional[Union[str, XSDDate]] = None
    adrs: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.valid_from is not None and not isinstance(self.valid_from, XSDDate):
            self.valid_from = XSDDate(self.valid_from)

        if not isinstance(self.adrs, list):
            self.adrs = [self.adrs] if self.adrs is not None else []
        self.adrs = [v if isinstance(v, str) else str(v) for v in self.adrs]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CalmDecorator(YAMLRoot):
    """
    Supplementary information about elements of one or more architectures, kept apart from the architectures
    themselves.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmDecorator"]
    class_class_curie: ClassVar[str] = "calm:CalmDecorator"
    class_name: ClassVar[str] = "CalmDecorator"
    class_model_uri: ClassVar[URIRef] = CALM.CalmDecorator

    unique_id: str = None
    decorator_type: str = None
    target_architectures: Union[str, list[str]] = None
    applies_to: Union[str, list[str]] = None
    data: Union[dict, "CalmDecoratorData"] = None
    decorator_schema: Optional[str] = None
    target_type: Optional[Union[Union[str, "CalmDecoratorTargetType"], list[Union[str, "CalmDecoratorTargetType"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.unique_id):
            self.MissingRequiredField("unique_id")
        if not isinstance(self.unique_id, str):
            self.unique_id = str(self.unique_id)

        if self._is_empty(self.decorator_type):
            self.MissingRequiredField("decorator_type")
        if not isinstance(self.decorator_type, str):
            self.decorator_type = str(self.decorator_type)

        if self._is_empty(self.target_architectures):
            self.MissingRequiredField("target_architectures")
        if not isinstance(self.target_architectures, list):
            self.target_architectures = [self.target_architectures] if self.target_architectures is not None else []
        self.target_architectures = [v if isinstance(v, str) else str(v) for v in self.target_architectures]

        if self._is_empty(self.applies_to):
            self.MissingRequiredField("applies_to")
        if not isinstance(self.applies_to, list):
            self.applies_to = [self.applies_to] if self.applies_to is not None else []
        self.applies_to = [v if isinstance(v, str) else str(v) for v in self.applies_to]

        if self._is_empty(self.data):
            self.MissingRequiredField("data")
        if not isinstance(self.data, CalmDecoratorData):
            self.data = CalmDecoratorData()

        if self.decorator_schema is not None and not isinstance(self.decorator_schema, str):
            self.decorator_schema = str(self.decorator_schema)

        if not isinstance(self.target_type, list):
            self.target_type = [self.target_type] if self.target_type is not None else []
        self.target_type = [v if isinstance(v, CalmDecoratorTargetType) else CalmDecoratorTargetType(v) for v in self.target_type]

        super().__post_init__(**kwargs)


class CalmDecoratorData(YAMLRoot):
    """
    The decorator's data, an object free in shape.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmDecoratorData"]
    class_class_curie: ClassVar[str] = "calm:CalmDecoratorData"
    class_name: ClassVar[str] = "CalmDecoratorData"
    class_model_uri: ClassVar[URIRef] = CALM.CalmDecoratorData


@dataclass(repr=False)
class CalmEvidenceDocument(YAMLRoot):
    """
    An evidence document, which holds one piece of evidence for a control.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmEvidenceDocument"]
    class_class_curie: ClassVar[str] = "calm:CalmEvidenceDocument"
    class_name: ClassVar[str] = "CalmEvidenceDocument"
    class_model_uri: ClassVar[URIRef] = CALM.CalmEvidenceDocument

    evidence: Union[dict, "CalmEvidence"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.evidence):
            self.MissingRequiredField("evidence")
        if not isinstance(self.evidence, CalmEvidence):
            self.evidence = CalmEvidence(**as_dict(self.evidence))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CalmEvidence(YAMLRoot):
    """
    Evidence that a control's configuration is met, by the paths where it is kept.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmEvidence"]
    class_class_curie: ClassVar[str] = "calm:CalmEvidence"
    class_name: ClassVar[str] = "CalmEvidence"
    class_model_uri: ClassVar[URIRef] = CALM.CalmEvidence

    unique_id: str = None
    evidence_paths: Union[str, list[str]] = None
    control_config_url: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.unique_id):
            self.MissingRequiredField("unique_id")
        if not isinstance(self.unique_id, str):
            self.unique_id = str(self.unique_id)

        if self._is_empty(self.evidence_paths):
            self.MissingRequiredField("evidence_paths")
        if not isinstance(self.evidence_paths, list):
            self.evidence_paths = [self.evidence_paths] if self.evidence_paths is not None else []
        self.evidence_paths = [v if isinstance(v, str) else str(v) for v in self.evidence_paths]

        if self._is_empty(self.control_config_url):
            self.MissingRequiredField("control_config_url")
        if not isinstance(self.control_config_url, str):
            self.control_config_url = str(self.control_config_url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CalmControlRequirement(YAMLRoot):
    """
    A control requirement: what a control must achieve, which a control detail's requirement-url points to.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmControlRequirement"]
    class_class_curie: ClassVar[str] = "calm:CalmControlRequirement"
    class_name: ClassVar[str] = "CalmControlRequirement"
    class_model_uri: ClassVar[URIRef] = CALM.CalmControlRequirement

    control_id: str = None
    name: str = None
    description: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.control_id):
            self.MissingRequiredField("control_id")
        if not isinstance(self.control_id, str):
            self.control_id = str(self.control_id)

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
class CalmTimeUnit(YAMLRoot):
    """
    A unit of time with a value and a unit type.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmTimeUnit"]
    class_class_curie: ClassVar[str] = "calm:CalmTimeUnit"
    class_name: ClassVar[str] = "CalmTimeUnit"
    class_model_uri: ClassVar[URIRef] = CALM.CalmTimeUnit

    unit_of_time: Union[str, "CalmTimeUnitName"] = None
    value: float = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.unit_of_time):
            self.MissingRequiredField("unit_of_time")
        if not isinstance(self.unit_of_time, CalmTimeUnitName):
            self.unit_of_time = CalmTimeUnitName(self.unit_of_time)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, float):
            self.value = float(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CalmRateUnit(YAMLRoot):
    """
    A unit representing a rate (e.g., operations per second).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CALM["CalmRateUnit"]
    class_class_curie: ClassVar[str] = "calm:CalmRateUnit"
    class_name: ClassVar[str] = "CalmRateUnit"
    class_model_uri: ClassVar[URIRef] = CALM.CalmRateUnit

    rate: float = None
    per: Union[str, "CalmRateInterval"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.rate):
            self.MissingRequiredField("rate")
        if not isinstance(self.rate, float):
            self.rate = float(self.rate)

        if self._is_empty(self.per):
            self.MissingRequiredField("per")
        if not isinstance(self.per, CalmRateInterval):
            self.per = CalmRateInterval(self.per)

        super().__post_init__(**kwargs)


# Enumerations
class CalmProtocol(EnumDefinitionImpl):
    """
    The protocol a relationship uses.
    """
    HTTP = PermissibleValue(
        text="HTTP",
        description="Hypertext Transfer Protocol.")
    HTTPS = PermissibleValue(
        text="HTTPS",
        description="HTTP over TLS.")
    FTP = PermissibleValue(
        text="FTP",
        description="File Transfer Protocol.")
    SFTP = PermissibleValue(
        text="SFTP",
        description="SSH File Transfer Protocol.")
    JDBC = PermissibleValue(
        text="JDBC",
        description="Java Database Connectivity.")
    WebSocket = PermissibleValue(
        text="WebSocket",
        description="The WebSocket protocol.")
    SocketIO = PermissibleValue(
        text="SocketIO",
        description="The Socket.IO protocol.")
    LDAP = PermissibleValue(
        text="LDAP",
        description="Lightweight Directory Access Protocol.")
    AMQP = PermissibleValue(
        text="AMQP",
        description="Advanced Message Queuing Protocol.")
    TLS = PermissibleValue(
        text="TLS",
        description="Transport Layer Security.")
    mTLS = PermissibleValue(
        text="mTLS",
        description="TLS in which both ends present a certificate.")
    TCP = PermissibleValue(
        text="TCP",
        description="Transmission Control Protocol.")

    _defn = EnumDefinition(
        name="CalmProtocol",
        description="The protocol a relationship uses.",
    )

class CalmNodeTypeDefinition(EnumDefinitionImpl):
    """
    CALM's built-in node types. A node may also name a type of its own, so the build publishes this list open to any
    other string.
    """
    actor = PermissibleValue(
        text="actor",
        description="A person or system outside the architecture that acts on it.")
    ecosystem = PermissibleValue(
        text="ecosystem",
        description="A group of systems that work together.")
    system = PermissibleValue(
        text="system",
        description="A system made of other nodes.")
    service = PermissibleValue(
        text="service",
        description="A service that runs in the architecture.")
    database = PermissibleValue(
        text="database",
        description="A store of data.")
    network = PermissibleValue(
        text="network",
        description="A network that nodes are deployed in.")
    ldap = PermissibleValue(
        text="ldap",
        description="A directory service reached over LDAP.")
    webclient = PermissibleValue(
        text="webclient",
        description="A client that runs in a web browser.")

    _defn = EnumDefinition(
        name="CalmNodeTypeDefinition",
        description="""CALM's built-in node types. A node may also name a type of its own, so the build publishes this list open to any other string.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "data-asset",
            PermissibleValue(
                text="data-asset",
                title="data asset",
                description="A body of data the architecture holds or moves."))

class CalmTransitionDirection(EnumDefinitionImpl):
    """
    The direction of a transition along its relationship.
    """
    _defn = EnumDefinition(
        name="CalmTransitionDirection",
        description="The direction of a transition along its relationship.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "source-to-destination",
            PermissibleValue(
                text="source-to-destination",
                title="source to destination",
                description="From the relationship's source to its destination."))
        setattr(cls, "destination-to-source",
            PermissibleValue(
                text="destination-to-source",
                title="destination to source",
                description="From the relationship's destination back to its source."))

class CalmDecoratorTargetType(EnumDefinitionImpl):
    """
    The kinds of CALM document a decorator can target.
    """
    architecture = PermissibleValue(
        text="architecture",
        description="An architecture document.")

    _defn = EnumDefinition(
        name="CalmDecoratorTargetType",
        description="The kinds of CALM document a decorator can target.",
    )

class CalmTimeUnitName(EnumDefinitionImpl):
    """
    The units a time unit counts in.
    """
    nanoseconds = PermissibleValue(
        text="nanoseconds",
        description="Billionths of a second.")
    microseconds = PermissibleValue(
        text="microseconds",
        description="Millionths of a second.")
    milliseconds = PermissibleValue(
        text="milliseconds",
        description="Thousandths of a second.")
    seconds = PermissibleValue(
        text="seconds",
        description="Seconds.")
    minutes = PermissibleValue(
        text="minutes",
        description="Minutes.")
    hours = PermissibleValue(
        text="hours",
        description="Hours.")
    days = PermissibleValue(
        text="days",
        description="Days.")
    weeks = PermissibleValue(
        text="weeks",
        description="Weeks.")
    months = PermissibleValue(
        text="months",
        description="Calendar months.")
    quarters = PermissibleValue(
        text="quarters",
        description="Quarters of a year.")
    years = PermissibleValue(
        text="years",
        description="Years.")

    _defn = EnumDefinition(
        name="CalmTimeUnitName",
        description="The units a time unit counts in.",
    )

class CalmRateInterval(EnumDefinitionImpl):
    """
    The interval a rate is counted over.
    """
    nanosecond = PermissibleValue(
        text="nanosecond",
        description="Per billionth of a second.")
    microsecond = PermissibleValue(
        text="microsecond",
        description="Per millionth of a second.")
    millisecond = PermissibleValue(
        text="millisecond",
        description="Per thousandth of a second.")
    second = PermissibleValue(
        text="second",
        description="Per second.")
    minute = PermissibleValue(
        text="minute",
        description="Per minute.")
    hour = PermissibleValue(
        text="hour",
        description="Per hour.")
    day = PermissibleValue(
        text="day",
        description="Per day.")
    week = PermissibleValue(
        text="week",
        description="Per week.")
    month = PermissibleValue(
        text="month",
        description="Per calendar month.")
    quarter = PermissibleValue(
        text="quarter",
        description="Per quarter of a year.")
    year = PermissibleValue(
        text="year",
        description="Per year.")

    _defn = EnumDefinition(
        name="CalmRateInterval",
        description="The interval a rate is counted over.",
    )

# Slots
class slots:
    pass

slots.calmArchitecture__nodes = Slot(uri=CALM.nodes, name="calmArchitecture__nodes", curie=CALM.curie('nodes'),
                   model_uri=CALM.calmArchitecture__nodes, domain=None, range=Optional[Union[Union[dict, CalmNode], list[Union[dict, CalmNode]]]])

slots.calmArchitecture__relationships = Slot(uri=CALM.relationships, name="calmArchitecture__relationships", curie=CALM.curie('relationships'),
                   model_uri=CALM.calmArchitecture__relationships, domain=None, range=Optional[Union[Union[dict, CalmRelationship], list[Union[dict, CalmRelationship]]]])

slots.calmArchitecture__metadata = Slot(uri=CALM.metadata, name="calmArchitecture__metadata", curie=CALM.curie('metadata'),
                   model_uri=CALM.calmArchitecture__metadata, domain=None, range=Optional[Union[dict, CalmMetadata]])

slots.calmArchitecture__controls = Slot(uri=CALM.controls, name="calmArchitecture__controls", curie=CALM.curie('controls'),
                   model_uri=CALM.calmArchitecture__controls, domain=None, range=Optional[Union[dict, CalmControls]])

slots.calmArchitecture__flows = Slot(uri=CALM.flows, name="calmArchitecture__flows", curie=CALM.curie('flows'),
                   model_uri=CALM.calmArchitecture__flows, domain=None, range=Optional[Union[Union[dict, CalmFlow], list[Union[dict, CalmFlow]]]])

slots.calmArchitecture__adrs = Slot(uri=CALM.adrs, name="calmArchitecture__adrs", curie=CALM.curie('adrs'),
                   model_uri=CALM.calmArchitecture__adrs, domain=None, range=Optional[Union[str, list[str]]])

slots.calmControl__description = Slot(uri=SCHEMA.description, name="calmControl__description", curie=SCHEMA.curie('description'),
                   model_uri=CALM.calmControl__description, domain=None, range=str)

slots.calmControl__requirements = Slot(uri=CALM.requirements, name="calmControl__requirements", curie=CALM.curie('requirements'),
                   model_uri=CALM.calmControl__requirements, domain=None, range=Union[Union[dict, CalmControlDetail], list[Union[dict, CalmControlDetail]]])

slots.calmControlDetail__requirement_url = Slot(uri=CALM.requirement_url, name="calmControlDetail__requirement_url", curie=CALM.curie('requirement_url'),
                   model_uri=CALM.calmControlDetail__requirement_url, domain=None, range=str)

slots.calmControlDetail__config_url = Slot(uri=CALM.config_url, name="calmControlDetail__config_url", curie=CALM.curie('config_url'),
                   model_uri=CALM.calmControlDetail__config_url, domain=None, range=Optional[str])

slots.calmControlDetail__config = Slot(uri=CALM.config, name="calmControlDetail__config", curie=CALM.curie('config'),
                   model_uri=CALM.calmControlDetail__config, domain=None, range=Optional[Union[dict, CalmControlConfig]])

slots.calmInterfaceDefinition__unique_id = Slot(uri=CALM.unique_id, name="calmInterfaceDefinition__unique_id", curie=CALM.curie('unique_id'),
                   model_uri=CALM.calmInterfaceDefinition__unique_id, domain=None, range=str)

slots.calmInterfaceDefinition__definition_url = Slot(uri=CALM.definition_url, name="calmInterfaceDefinition__definition_url", curie=CALM.curie('definition_url'),
                   model_uri=CALM.calmInterfaceDefinition__definition_url, domain=None, range=str)

slots.calmInterfaceDefinition__config = Slot(uri=CALM.config, name="calmInterfaceDefinition__config", curie=CALM.curie('config'),
                   model_uri=CALM.calmInterfaceDefinition__config, domain=None, range=Union[dict, CalmInterfaceConfig])

slots.calmInterfaceType__unique_id = Slot(uri=CALM.unique_id, name="calmInterfaceType__unique_id", curie=CALM.curie('unique_id'),
                   model_uri=CALM.calmInterfaceType__unique_id, domain=None, range=str)

slots.calmNodeInterface__node = Slot(uri=CALM.node, name="calmNodeInterface__node", curie=CALM.curie('node'),
                   model_uri=CALM.calmNodeInterface__node, domain=None, range=str)

slots.calmNodeInterface__interfaces = Slot(uri=CALM.interfaces, name="calmNodeInterface__interfaces", curie=CALM.curie('interfaces'),
                   model_uri=CALM.calmNodeInterface__interfaces, domain=None, range=Optional[Union[str, list[str]]])

slots.calmNode__unique_id = Slot(uri=CALM.unique_id, name="calmNode__unique_id", curie=CALM.curie('unique_id'),
                   model_uri=CALM.calmNode__unique_id, domain=None, range=str)

slots.calmNode__node_type = Slot(uri=CALM.node_type, name="calmNode__node_type", curie=CALM.curie('node_type'),
                   model_uri=CALM.calmNode__node_type, domain=None, range=Union[str, "CalmNodeTypeDefinition"])

slots.calmNode__name = Slot(uri=SCHEMA.name, name="calmNode__name", curie=SCHEMA.curie('name'),
                   model_uri=CALM.calmNode__name, domain=None, range=str)

slots.calmNode__description = Slot(uri=SCHEMA.description, name="calmNode__description", curie=SCHEMA.curie('description'),
                   model_uri=CALM.calmNode__description, domain=None, range=str)

slots.calmNode__details = Slot(uri=CALM.details, name="calmNode__details", curie=CALM.curie('details'),
                   model_uri=CALM.calmNode__details, domain=None, range=Optional[Union[dict, CalmNodeDetails]])

slots.calmNode__interfaces = Slot(uri=CALM.interfaces, name="calmNode__interfaces", curie=CALM.curie('interfaces'),
                   model_uri=CALM.calmNode__interfaces, domain=None, range=Optional[Union[str, list[str]]])

slots.calmNode__controls = Slot(uri=CALM.controls, name="calmNode__controls", curie=CALM.curie('controls'),
                   model_uri=CALM.calmNode__controls, domain=None, range=Optional[Union[dict, CalmControls]])

slots.calmNode__metadata = Slot(uri=CALM.metadata, name="calmNode__metadata", curie=CALM.curie('metadata'),
                   model_uri=CALM.calmNode__metadata, domain=None, range=Optional[Union[dict, CalmMetadata]])

slots.calmNodeDetails__detailed_architecture = Slot(uri=CALM.detailed_architecture, name="calmNodeDetails__detailed_architecture", curie=CALM.curie('detailed_architecture'),
                   model_uri=CALM.calmNodeDetails__detailed_architecture, domain=None, range=Optional[str])

slots.calmNodeDetails__required_pattern = Slot(uri=CALM.required_pattern, name="calmNodeDetails__required_pattern", curie=CALM.curie('required_pattern'),
                   model_uri=CALM.calmNodeDetails__required_pattern, domain=None, range=Optional[str])

slots.calmRelationship__unique_id = Slot(uri=CALM.unique_id, name="calmRelationship__unique_id", curie=CALM.curie('unique_id'),
                   model_uri=CALM.calmRelationship__unique_id, domain=None, range=str)

slots.calmRelationship__description = Slot(uri=SCHEMA.description, name="calmRelationship__description", curie=SCHEMA.curie('description'),
                   model_uri=CALM.calmRelationship__description, domain=None, range=Optional[str])

slots.calmRelationship__relationship_type = Slot(uri=CALM.relationship_type, name="calmRelationship__relationship_type", curie=CALM.curie('relationship_type'),
                   model_uri=CALM.calmRelationship__relationship_type, domain=None, range=Union[dict, CalmRelationshipType])

slots.calmRelationship__protocol = Slot(uri=CALM.protocol, name="calmRelationship__protocol", curie=CALM.curie('protocol'),
                   model_uri=CALM.calmRelationship__protocol, domain=None, range=Optional[Union[str, "CalmProtocol"]])

slots.calmRelationship__metadata = Slot(uri=CALM.metadata, name="calmRelationship__metadata", curie=CALM.curie('metadata'),
                   model_uri=CALM.calmRelationship__metadata, domain=None, range=Optional[Union[dict, CalmMetadata]])

slots.calmRelationship__controls = Slot(uri=CALM.controls, name="calmRelationship__controls", curie=CALM.curie('controls'),
                   model_uri=CALM.calmRelationship__controls, domain=None, range=Optional[Union[dict, CalmControls]])

slots.calmRelationshipType__interacts = Slot(uri=CALM.interacts, name="calmRelationshipType__interacts", curie=CALM.curie('interacts'),
                   model_uri=CALM.calmRelationshipType__interacts, domain=None, range=Optional[Union[dict, CalmInteractsType]])

slots.calmRelationshipType__connects = Slot(uri=CALM.connects, name="calmRelationshipType__connects", curie=CALM.curie('connects'),
                   model_uri=CALM.calmRelationshipType__connects, domain=None, range=Optional[Union[dict, CalmConnectsType]])

slots.calmRelationshipType__deployed_in = Slot(uri=CALM.deployed_in, name="calmRelationshipType__deployed_in", curie=CALM.curie('deployed_in'),
                   model_uri=CALM.calmRelationshipType__deployed_in, domain=None, range=Optional[Union[dict, CalmDeployedInType]])

slots.calmRelationshipType__composed_of = Slot(uri=CALM.composed_of, name="calmRelationshipType__composed_of", curie=CALM.curie('composed_of'),
                   model_uri=CALM.calmRelationshipType__composed_of, domain=None, range=Optional[Union[dict, CalmComposedOfType]])

slots.calmRelationshipType__options = Slot(uri=CALM.options, name="calmRelationshipType__options", curie=CALM.curie('options'),
                   model_uri=CALM.calmRelationshipType__options, domain=None, range=Optional[Union[Union[dict, CalmDecision], list[Union[dict, CalmDecision]]]])

slots.calmInteractsType__actor = Slot(uri=CALM.actor, name="calmInteractsType__actor", curie=CALM.curie('actor'),
                   model_uri=CALM.calmInteractsType__actor, domain=None, range=str)

slots.calmInteractsType__nodes = Slot(uri=CALM.nodes, name="calmInteractsType__nodes", curie=CALM.curie('nodes'),
                   model_uri=CALM.calmInteractsType__nodes, domain=None, range=Union[str, list[str]])

slots.calmConnectsType__source_end = Slot(uri=CALM.source_end, name="calmConnectsType__source_end", curie=CALM.curie('source_end'),
                   model_uri=CALM.calmConnectsType__source_end, domain=None, range=Union[dict, CalmNodeInterface])

slots.calmConnectsType__destination_end = Slot(uri=CALM.destination_end, name="calmConnectsType__destination_end", curie=CALM.curie('destination_end'),
                   model_uri=CALM.calmConnectsType__destination_end, domain=None, range=Union[dict, CalmNodeInterface])

slots.calmDeployedInType__container = Slot(uri=CALM.container, name="calmDeployedInType__container", curie=CALM.curie('container'),
                   model_uri=CALM.calmDeployedInType__container, domain=None, range=str)

slots.calmDeployedInType__nodes = Slot(uri=CALM.nodes, name="calmDeployedInType__nodes", curie=CALM.curie('nodes'),
                   model_uri=CALM.calmDeployedInType__nodes, domain=None, range=Union[str, list[str]])

slots.calmComposedOfType__container = Slot(uri=CALM.container, name="calmComposedOfType__container", curie=CALM.curie('container'),
                   model_uri=CALM.calmComposedOfType__container, domain=None, range=str)

slots.calmComposedOfType__nodes = Slot(uri=CALM.nodes, name="calmComposedOfType__nodes", curie=CALM.curie('nodes'),
                   model_uri=CALM.calmComposedOfType__nodes, domain=None, range=Union[str, list[str]])

slots.calmDecision__description = Slot(uri=SCHEMA.description, name="calmDecision__description", curie=SCHEMA.curie('description'),
                   model_uri=CALM.calmDecision__description, domain=None, range=str)

slots.calmDecision__nodes = Slot(uri=CALM.nodes, name="calmDecision__nodes", curie=CALM.curie('nodes'),
                   model_uri=CALM.calmDecision__nodes, domain=None, range=Union[str, list[str]])

slots.calmDecision__relationships = Slot(uri=CALM.relationships, name="calmDecision__relationships", curie=CALM.curie('relationships'),
                   model_uri=CALM.calmDecision__relationships, domain=None, range=Union[str, list[str]])

slots.calmDecision__controls = Slot(uri=CALM.controls, name="calmDecision__controls", curie=CALM.curie('controls'),
                   model_uri=CALM.calmDecision__controls, domain=None, range=Optional[Union[str, list[str]]])

slots.calmFlow__unique_id = Slot(uri=CALM.unique_id, name="calmFlow__unique_id", curie=CALM.curie('unique_id'),
                   model_uri=CALM.calmFlow__unique_id, domain=None, range=str)

slots.calmFlow__name = Slot(uri=SCHEMA.name, name="calmFlow__name", curie=SCHEMA.curie('name'),
                   model_uri=CALM.calmFlow__name, domain=None, range=str)

slots.calmFlow__description = Slot(uri=SCHEMA.description, name="calmFlow__description", curie=SCHEMA.curie('description'),
                   model_uri=CALM.calmFlow__description, domain=None, range=str)

slots.calmFlow__requirement_url = Slot(uri=CALM.requirement_url, name="calmFlow__requirement_url", curie=CALM.curie('requirement_url'),
                   model_uri=CALM.calmFlow__requirement_url, domain=None, range=Optional[str])

slots.calmFlow__transitions = Slot(uri=CALM.transitions, name="calmFlow__transitions", curie=CALM.curie('transitions'),
                   model_uri=CALM.calmFlow__transitions, domain=None, range=Union[Union[dict, CalmTransition], list[Union[dict, CalmTransition]]])

slots.calmFlow__controls = Slot(uri=CALM.controls, name="calmFlow__controls", curie=CALM.curie('controls'),
                   model_uri=CALM.calmFlow__controls, domain=None, range=Optional[Union[dict, CalmControls]])

slots.calmFlow__metadata = Slot(uri=CALM.metadata, name="calmFlow__metadata", curie=CALM.curie('metadata'),
                   model_uri=CALM.calmFlow__metadata, domain=None, range=Optional[Union[dict, CalmMetadata]])

slots.calmTransition__relationship_unique_id = Slot(uri=CALM.relationship_unique_id, name="calmTransition__relationship_unique_id", curie=CALM.curie('relationship_unique_id'),
                   model_uri=CALM.calmTransition__relationship_unique_id, domain=None, range=str)

slots.calmTransition__sequence_number = Slot(uri=CALM.sequence_number, name="calmTransition__sequence_number", curie=CALM.curie('sequence_number'),
                   model_uri=CALM.calmTransition__sequence_number, domain=None, range=int)

slots.calmTransition__description = Slot(uri=SCHEMA.description, name="calmTransition__description", curie=SCHEMA.curie('description'),
                   model_uri=CALM.calmTransition__description, domain=None, range=str)

slots.calmTransition__direction = Slot(uri=CALM.direction, name="calmTransition__direction", curie=CALM.curie('direction'),
                   model_uri=CALM.calmTransition__direction, domain=None, range=Optional[Union[str, "CalmTransitionDirection"]])

slots.calmTimeline__current_moment = Slot(uri=CALM.current_moment, name="calmTimeline__current_moment", curie=CALM.curie('current_moment'),
                   model_uri=CALM.calmTimeline__current_moment, domain=None, range=Optional[str])

slots.calmTimeline__moments = Slot(uri=CALM.moments, name="calmTimeline__moments", curie=CALM.curie('moments'),
                   model_uri=CALM.calmTimeline__moments, domain=None, range=Union[Union[dict, CalmNodeMoment], list[Union[dict, CalmNodeMoment]]])

slots.calmTimeline__metadata = Slot(uri=CALM.metadata, name="calmTimeline__metadata", curie=CALM.curie('metadata'),
                   model_uri=CALM.calmTimeline__metadata, domain=None, range=Optional[Union[dict, CalmMetadata]])

slots.calmNodeMoment__valid_from = Slot(uri=CALM.valid_from, name="calmNodeMoment__valid_from", curie=CALM.curie('valid_from'),
                   model_uri=CALM.calmNodeMoment__valid_from, domain=None, range=Optional[Union[str, XSDDate]])

slots.calmNodeMoment__adrs = Slot(uri=CALM.adrs, name="calmNodeMoment__adrs", curie=CALM.curie('adrs'),
                   model_uri=CALM.calmNodeMoment__adrs, domain=None, range=Optional[Union[str, list[str]]])

slots.calmDecorator__decorator_schema = Slot(uri=CALM.decorator_schema, name="calmDecorator__decorator_schema", curie=CALM.curie('decorator_schema'),
                   model_uri=CALM.calmDecorator__decorator_schema, domain=None, range=Optional[str])

slots.calmDecorator__unique_id = Slot(uri=CALM.unique_id, name="calmDecorator__unique_id", curie=CALM.curie('unique_id'),
                   model_uri=CALM.calmDecorator__unique_id, domain=None, range=str)

slots.calmDecorator__decorator_type = Slot(uri=CALM.decorator_type, name="calmDecorator__decorator_type", curie=CALM.curie('decorator_type'),
                   model_uri=CALM.calmDecorator__decorator_type, domain=None, range=str)

slots.calmDecorator__target_type = Slot(uri=CALM.target_type, name="calmDecorator__target_type", curie=CALM.curie('target_type'),
                   model_uri=CALM.calmDecorator__target_type, domain=None, range=Optional[Union[Union[str, "CalmDecoratorTargetType"], list[Union[str, "CalmDecoratorTargetType"]]]])

slots.calmDecorator__target_architectures = Slot(uri=CALM.target_architectures, name="calmDecorator__target_architectures", curie=CALM.curie('target_architectures'),
                   model_uri=CALM.calmDecorator__target_architectures, domain=None, range=Union[str, list[str]])

slots.calmDecorator__applies_to = Slot(uri=CALM.applies_to, name="calmDecorator__applies_to", curie=CALM.curie('applies_to'),
                   model_uri=CALM.calmDecorator__applies_to, domain=None, range=Union[str, list[str]])

slots.calmDecorator__data = Slot(uri=CALM.data, name="calmDecorator__data", curie=CALM.curie('data'),
                   model_uri=CALM.calmDecorator__data, domain=None, range=Union[dict, CalmDecoratorData])

slots.calmEvidenceDocument__evidence = Slot(uri=CALM.evidence, name="calmEvidenceDocument__evidence", curie=CALM.curie('evidence'),
                   model_uri=CALM.calmEvidenceDocument__evidence, domain=None, range=Union[dict, CalmEvidence])

slots.calmEvidence__unique_id = Slot(uri=CALM.unique_id, name="calmEvidence__unique_id", curie=CALM.curie('unique_id'),
                   model_uri=CALM.calmEvidence__unique_id, domain=None, range=str)

slots.calmEvidence__evidence_paths = Slot(uri=CALM.evidence_paths, name="calmEvidence__evidence_paths", curie=CALM.curie('evidence_paths'),
                   model_uri=CALM.calmEvidence__evidence_paths, domain=None, range=Union[str, list[str]])

slots.calmEvidence__control_config_url = Slot(uri=CALM.control_config_url, name="calmEvidence__control_config_url", curie=CALM.curie('control_config_url'),
                   model_uri=CALM.calmEvidence__control_config_url, domain=None, range=str)

slots.calmControlRequirement__control_id = Slot(uri=CALM.control_id, name="calmControlRequirement__control_id", curie=CALM.curie('control_id'),
                   model_uri=CALM.calmControlRequirement__control_id, domain=None, range=str)

slots.calmControlRequirement__name = Slot(uri=SCHEMA.name, name="calmControlRequirement__name", curie=SCHEMA.curie('name'),
                   model_uri=CALM.calmControlRequirement__name, domain=None, range=str)

slots.calmControlRequirement__description = Slot(uri=SCHEMA.description, name="calmControlRequirement__description", curie=SCHEMA.curie('description'),
                   model_uri=CALM.calmControlRequirement__description, domain=None, range=str)

slots.calmTimeUnit__unit_of_time = Slot(uri=CALM.unit_of_time, name="calmTimeUnit__unit_of_time", curie=CALM.curie('unit_of_time'),
                   model_uri=CALM.calmTimeUnit__unit_of_time, domain=None, range=Union[str, "CalmTimeUnitName"])

slots.calmTimeUnit__value = Slot(uri=CALM.value, name="calmTimeUnit__value", curie=CALM.curie('value'),
                   model_uri=CALM.calmTimeUnit__value, domain=None, range=float)

slots.calmRateUnit__rate = Slot(uri=CALM.rate, name="calmRateUnit__rate", curie=CALM.curie('rate'),
                   model_uri=CALM.calmRateUnit__rate, domain=None, range=float)

slots.calmRateUnit__per = Slot(uri=CALM.per, name="calmRateUnit__per", curie=CALM.curie('per'),
                   model_uri=CALM.calmRateUnit__per, domain=None, range=Union[str, "CalmRateInterval"])
