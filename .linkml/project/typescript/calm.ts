export type NodeUniqueId = string;
export type RelationshipUniqueId = string;
export type ControlRequirementControlId = string;
export type DecoratorUniqueId = string;
export type FlowUniqueId = string;
export type InterfaceDefinitionUniqueId = string;
export type InterfaceTypeUniqueId = string;
export type NodeMomentUniqueId = string;
/**
* Wire-level protocol used by a relationship.
*/
export enum Protocol {
    
    /** The HTTP protocol. */
    HTTP = "HTTP",
    /** The HTTPS protocol. */
    HTTPS = "HTTPS",
    /** The FTP protocol. */
    FTP = "FTP",
    /** The SFTP protocol. */
    SFTP = "SFTP",
    /** The JDBC protocol. */
    JDBC = "JDBC",
    /** The WebSocket protocol. */
    WebSocket = "WebSocket",
    /** The SocketIO protocol. */
    SocketIO = "SocketIO",
    /** The LDAP protocol. */
    LDAP = "LDAP",
    /** The AMQP protocol. */
    AMQP = "AMQP",
    /** The TLS protocol. */
    TLS = "TLS",
    /** The mTLS protocol. */
    mTLS = "mTLS",
    /** The TCP protocol. */
    TCP = "TCP",
};
/**
* Category of architecture node. The CALM JSON-Schema allows arbitrary strings; this enum lists the canonical values plus an escape hatch via ``any_of`` on the slot.
*/
export enum NodeType {
    
    /** A actor node. */
    actor = "actor",
    /** A ecosystem node. */
    ecosystem = "ecosystem",
    /** A system node. */
    system = "system",
    /** A service node. */
    service = "service",
    /** A database node. */
    database = "database",
    /** A network node. */
    network = "network",
    /** A ldap node. */
    ldap = "ldap",
    /** A webclient node. */
    webclient = "webclient",
    /** A data-asset node. */
    data_asset = "data_asset",
};
/**
* Named unit of time used by ``TimeUnit``.
*/
export enum TimeUnitName {
    
    /** Time unit: nanoseconds. */
    nanoseconds = "nanoseconds",
    /** Time unit: microseconds. */
    microseconds = "microseconds",
    /** Time unit: milliseconds. */
    milliseconds = "milliseconds",
    /** Time unit: seconds. */
    seconds = "seconds",
    /** Time unit: minutes. */
    minutes = "minutes",
    /** Time unit: hours. */
    hours = "hours",
    /** Time unit: days. */
    days = "days",
    /** Time unit: weeks. */
    weeks = "weeks",
    /** Time unit: months. */
    months = "months",
    /** Time unit: quarters. */
    quarters = "quarters",
    /** Time unit: years. */
    years = "years",
};
/**
* Time interval denominator used by ``RateUnit``.
*/
export enum RatePerUnit {
    
    /** Rate denominator: per nanosecond. */
    nanosecond = "nanosecond",
    /** Rate denominator: per microsecond. */
    microsecond = "microsecond",
    /** Rate denominator: per millisecond. */
    millisecond = "millisecond",
    /** Rate denominator: per second. */
    second = "second",
    /** Rate denominator: per minute. */
    minute = "minute",
    /** Rate denominator: per hour. */
    hour = "hour",
    /** Rate denominator: per day. */
    day = "day",
    /** Rate denominator: per week. */
    week = "week",
    /** Rate denominator: per month. */
    month = "month",
    /** Rate denominator: per quarter. */
    quarter = "quarter",
    /** Rate denominator: per year. */
    year = "year",
};
/**
* Direction of flow on a transition.
*/
export enum TransitionDirection {
    
    /** Flow direction: source-to-destination. */
    source_to_destination = "source_to_destination",
    /** Flow direction: destination-to-source. */
    destination_to_source = "destination_to_source",
};
/**
* Discriminator for the variant of a ``relationship-type``: exactly one of the following keys is set on a relationship's ``relationship-type``.
*/
export enum RelationshipKind {
    
    /** Actor-to-nodes interaction. */
    interacts = "interacts",
    /** Interface-to-interface connection. */
    connects = "connects",
    /** Containment: nodes deployed in a container. */
    deployed_in = "deployed_in",
    /** Composition: nodes composed by a container. */
    composed_of = "composed_of",
    /** A set of alternative decisions. */
    options = "options",
};


/**
 * Top-level CALM architecture document.
 */
export interface Architecture {
    nodes?: Node[],
    relationships?: Relationship[],
    metadata?: string,
    controls?: Control,
    flows?: Flow[],
    /** External links to ADRs (Architecture Decision Records) or similar documents that provide context or decisions related to the architecture. These can be URLs or references to internal documentation. */
    adrs?: string[],
}


/**
 * A logical or physical element of an architecture (system, service, actor, ...).
 */
export interface Node {
    /** Stable opaque identifier used to cross-link CALM elements. */
    unique_id: string,
    /** Category of the node (system, service, actor, etc.). */
    node_type: string,
    /** Short human-readable name. */
    name: string,
    /** Free-form description of the element. */
    description: string,
    details?: string,
    /** Interface definitions exposed by nodes. */
    interfaces?: InterfaceDefinition[],
    controls?: Control,
    metadata?: string,
}


/**
 * A typed link between architecture elements.
 */
export interface Relationship {
    /** Stable opaque identifier used to cross-link CALM elements. */
    unique_id: string,
    /** Free-form description of the element. */
    description?: string,
    relationship_type: RelationshipType,
    protocol?: string,
    metadata?: string,
    controls?: Control,
}


/**
 * An ``interacts`` relationship between an actor and one or more nodes.
 */
export interface InteractsRelationship {
    actor: string,
    nodes: NodeUniqueId[],
}


/**
 * A ``connects`` relationship between two node interfaces.
 */
export interface ConnectsRelationship {
    source: NodeInterface,
    destination: NodeInterface,
}


/**
 * A ``deployed-in`` containment relationship.
 */
export interface DeployedInRelationship {
    container: string,
    nodes: NodeUniqueId[],
}


/**
 * A ``composed-of`` containment relationship.
 */
export interface ComposedOfRelationship {
    container: string,
    nodes: NodeUniqueId[],
}


/**
 * A candidate decision within an ``options`` relationship.
 */
export interface Decision {
    /** Free-form description of the element. */
    description: string,
    nodes: Node[],
    relationships: Relationship[],
    controls?: Control,
}


/**
 * A single control requirement and its inline / referenced configuration.
 */
export interface ControlDetail {
    /** The requirement schema that specifies how a control should be defined */
    requirement_url: string,
    /** The configuration of how the control requirement schema is met */
    config_url?: string,
    /** Inline configuration of how the control requirement schema is met */
    config?: string,
}


/**
 * A named control attached to an architecture element.
 */
export interface Control {
}


/**
 * Domain-defined control requirement that controls can reference.
 */
export interface ControlRequirement {
    /** The unique identifier of this control, which has the potential to be used for linking evidence */
    control_id: string,
    /** Short human-readable name. */
    name: string,
    /** Free-form description of the element. */
    description: string,
}


/**
 * Cross-cutting annotation attached to nodes, relationships, or flows.
 */
export interface Decorator {
    /** Stable opaque identifier used to cross-link CALM elements. */
    unique_id: string,
    /** Type of decorator - a free-form string identifying the decorator category */
    type: string,
    /** Array of file paths or URLs referencing the CALM documents (patterns, architectures, or controls) this decorator targets */
    target: string[],
    /** Array of unique-ids referencing nodes, relationships, flows, or other architecture elements */
    applies_to: string[],
    /** Free-form JSON object containing the decorator's data */
    data: string,
}


/**
 * Top-level CALM evidence document linking control configurations to evidence artefacts.
 */
export interface EvidenceDocument {
    evidence: string,
}


/**
 * A single step in a flow, anchored on a relationship.
 */
export interface Transition {
    /** Unique identifier for the relationship in the architecture */
    relationship_unique_id: string,
    /** Indicates the sequence of the relationship in the flow */
    sequence_number: number,
    /** Free-form description of the element. */
    description: string,
    /** Direction of flow on the transition. */
    direction?: string,
}


/**
 * Business flow mapped onto architecture relationships.
 */
export interface Flow {
    /** Stable opaque identifier used to cross-link CALM elements. */
    unique_id: string,
    /** Short human-readable name. */
    name: string,
    /** Free-form description of the element. */
    description: string,
    /** The requirement schema that specifies how a control should be defined */
    requirement_url?: string,
    transitions: Transition[],
    controls?: Control,
    metadata?: string,
}


/**
 * Modular interface definition referencing an external schema.
 */
export interface InterfaceDefinition {
    /** Stable opaque identifier used to cross-link CALM elements. */
    unique_id: string,
    /** URI of the external schema this interface configuration conforms to */
    definition_url: string,
    /** Inline configuration of how the control requirement schema is met */
    config: string,
}


/**
 * Inline (free-form) interface definition keyed by unique-id.
 */
export interface InterfaceType {
    /** Stable opaque identifier used to cross-link CALM elements. */
    unique_id: string,
}


/**
 * Reference to one or more interfaces exposed by a node.
 */
export interface NodeInterface {
    node: string,
    /** Interface definitions exposed by nodes. */
    interfaces?: InterfaceDefinition[],
}


/**
 * CALM timeline document capturing architecture moments over time.
 */
export interface Timeline {
    /** The unique-id of the current architecture moment within the timeline. */
    current_moment?: string,
    /** A list of significant architecture states or points in time, each represented as a 'moment'. */
    moments: string[],
    metadata?: string,
}


/**
 * An architecture moment - a point-in-time snapshot of the architecture.
 */
export interface NodeMoment extends Node {
    /** Category of the node (system, service, actor, etc.). */
    node_type: string,
    /** The date when this architecture moment came into effect. */
    valid_from?: date,
    /** External links to ADRs (Architecture Decision Records) or similar documents that provide context or decisions related to the architecture. These can be URLs or references to internal documentation. */
    adrs?: string[],
    /** Interface definitions exposed by nodes. */
    interfaces?: InterfaceDefinition[],
}


/**
 * A quantity of time expressed as a numeric value and a unit.
 */
export interface TimeUnit {
    /** The unit of time (e.g., seconds, minutes, hours). */
    unit: string,
    /** The numeric value representing the amount of time. */
    value: number,
}


/**
 * A rate (count per time unit), e.g. operations per second.
 */
export interface RateUnit {
    /** The numeric value representing the rate. */
    rate: number,
    /** The time unit defining the rate interval. */
    per: string,
}


/**
 * Wrapper around the list of ``Decision`` alternatives in an options relationship.
 */
export interface OptionList {
    /** Alternative decisions under an ``options`` relationship. */
    decisions?: Decision[],
}


/**
 * Tagged-union container for the variant body of a relationship. Exactly one of ``interacts``, ``connects``, ``deployed_in``, ``composed_of``, ``options`` is populated; see ``RelationshipKind`` for the discriminator values.
 */
export interface RelationshipType {
    interacts?: InteractsRelationship,
    connects?: ConnectsRelationship,
    deployed_in?: DeployedInRelationship,
    composed_of?: ComposedOfRelationship,
    options?: Decision[],
}



