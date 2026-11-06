/**
* The protocol a relationship uses.
*/
export enum CalmProtocol {
    
    /** Hypertext Transfer Protocol. */
    HTTP = "HTTP",
    /** HTTP over TLS. */
    HTTPS = "HTTPS",
    /** File Transfer Protocol. */
    FTP = "FTP",
    /** SSH File Transfer Protocol. */
    SFTP = "SFTP",
    /** Java Database Connectivity. */
    JDBC = "JDBC",
    /** The WebSocket protocol. */
    WebSocket = "WebSocket",
    /** The Socket.IO protocol. */
    SocketIO = "SocketIO",
    /** Lightweight Directory Access Protocol. */
    LDAP = "LDAP",
    /** Advanced Message Queuing Protocol. */
    AMQP = "AMQP",
    /** Transport Layer Security. */
    TLS = "TLS",
    /** TLS in which both ends present a certificate. */
    mTLS = "mTLS",
    /** Transmission Control Protocol. */
    TCP = "TCP",
};
/**
* CALM's built-in node types. A node may also name a type of its own, so the build publishes this list open to any other string.
*/
export enum CalmNodeTypeDefinition {
    
    /** A person or system outside the architecture that acts on it. */
    actor = "actor",
    /** A group of systems that work together. */
    ecosystem = "ecosystem",
    /** A system made of other nodes. */
    system = "system",
    /** A service that runs in the architecture. */
    service = "service",
    /** A store of data. */
    database = "database",
    /** A network that nodes are deployed in. */
    network = "network",
    /** A directory service reached over LDAP. */
    ldap = "ldap",
    /** A client that runs in a web browser. */
    webclient = "webclient",
    /** A body of data the architecture holds or moves. */
    data_asset = "data-asset",
};
/**
* The direction of a transition along its relationship.
*/
export enum CalmTransitionDirection {
    
    /** From the relationship's source to its destination. */
    source_to_destination = "source-to-destination",
    /** From the relationship's destination back to its source. */
    destination_to_source = "destination-to-source",
};
/**
* The kinds of CALM document a decorator can target.
*/
export enum CalmDecoratorTargetType {
    
    /** An architecture document. */
    architecture = "architecture",
};
/**
* The units a time unit counts in.
*/
export enum CalmTimeUnitName {
    
    /** Billionths of a second. */
    nanoseconds = "nanoseconds",
    /** Millionths of a second. */
    microseconds = "microseconds",
    /** Thousandths of a second. */
    milliseconds = "milliseconds",
    /** Seconds. */
    seconds = "seconds",
    /** Minutes. */
    minutes = "minutes",
    /** Hours. */
    hours = "hours",
    /** Days. */
    days = "days",
    /** Weeks. */
    weeks = "weeks",
    /** Calendar months. */
    months = "months",
    /** Quarters of a year. */
    quarters = "quarters",
    /** Years. */
    years = "years",
};
/**
* The interval a rate is counted over.
*/
export enum CalmRateInterval {
    
    /** Per billionth of a second. */
    nanosecond = "nanosecond",
    /** Per millionth of a second. */
    microsecond = "microsecond",
    /** Per thousandth of a second. */
    millisecond = "millisecond",
    /** Per second. */
    second = "second",
    /** Per minute. */
    minute = "minute",
    /** Per hour. */
    hour = "hour",
    /** Per day. */
    day = "day",
    /** Per week. */
    week = "week",
    /** Per calendar month. */
    month = "month",
    /** Per quarter of a year. */
    quarter = "quarter",
    /** Per year. */
    year = "year",
};


/**
 * The controls that apply to an architecture element, each under a key of letters, digits and hyphens.
 */
export interface CalmControls {
}


/**
 * One control in a controls map, with the requirements that define it.
 */
export interface CalmControl {
    /** A description of a control and how it applies to a given architecture */
    description: string,
    /** The requirements this control applies, each with its configuration. */
    requirements: CalmControlDetail[],
}


/**
 * A control requirement this control applies, with its configuration given by address or inline, but not both.
 */
export interface CalmControlDetail {
    /** The requirement schema that specifies how a control should be defined */
    requirement_url: string,
    /** The configuration of how the control requirement schema is met */
    config_url?: string,
    /** Inline configuration of how the control requirement schema is met */
    config?: CalmControlConfig,
}


/**
 * A configuration object, free in shape, that meets a control requirement.
 */
export interface CalmControlConfig {
}


/**
 * A modular interface definition referencing an external schema
 */
export interface CalmInterfaceDefinition {
    /** Unique identifier for this interface instance */
    unique_id: string,
    /** URI of the external schema this interface configuration conforms to */
    definition_url: string,
    /** Inline configuration conforming to the external interface schema */
    config: CalmInterfaceConfig,
}


/**
 * A configuration object, free in shape, that an interface definition's schema checks.
 */
export interface CalmInterfaceConfig {
}


/**
 * An interface given by its own keys, such as a host and port, rather than by an external schema.
 */
export interface CalmInterfaceType {
    /** The interface's identifier, unique within the architecture. */
    unique_id: string,
}


/**
 * One end of a connection, naming a node and, optionally, which of its interfaces.
 */
export interface CalmNodeInterface {
    /** The unique-id of the node at this end. */
    node: string,
    /** The unique-ids of the node's interfaces this end uses. */
    interfaces?: string[],
}


/**
 * A component of the architecture, such as a system, service, database or actor, with its interfaces and controls.
 */
export interface CalmNode {
    /** The node's identifier, unique within the architecture. */
    unique_id: string,
    /** What kind of node this is, one of CALM's built-in types or any other name. */
    node_type: string,
    /** The node's name. */
    name: string,
    /** What the node is and does. */
    description: string,
    /** Where a more detailed architecture of this node is, and the pattern it must follow. */
    details?: CalmNodeDetails,
    /** The interfaces the node exposes. */
    interfaces?: string[],
    /** The controls that apply to this node. */
    controls?: CalmControls,
    /** Free-form metadata about this node. */
    metadata?: CalmMetadata,
}


/**
 * References from a node to a more detailed architecture and to the pattern it must follow.
 */
export interface CalmNodeDetails {
    /** The address of an architecture document that describes this node in detail. */
    detailed_architecture?: string,
    /** The address of a pattern that the detailed architecture must follow. */
    required_pattern?: string,
}


/**
 * A link between nodes, of one of CALM's kinds, or a choice between options.
 */
export interface CalmRelationship {
    /** The relationship's identifier, unique within the architecture. */
    unique_id: string,
    /** What the relationship is for. */
    description?: string,
    /** The kind of the relationship and the nodes it links. */
    relationship_type: CalmRelationshipType,
    /** The protocol a connection uses. */
    protocol?: string,
    /** Free-form metadata about this relationship. */
    metadata?: CalmMetadata,
    /** The controls that apply to this relationship. */
    controls?: CalmControls,
}


/**
 * The kind of a relationship, given by exactly one of its keys: interacts, connects, deployed-in, composed-of or options.
 */
export interface CalmRelationshipType {
    /** An actor that interacts with nodes. */
    interacts?: CalmInteractsType,
    /** A connection from one node's interfaces to another's. */
    connects?: CalmConnectsType,
    /** Nodes deployed in a container node. */
    deployed_in?: CalmDeployedInType,
    /** Nodes that make up a container node. */
    composed_of?: CalmComposedOfType,
    /** Decisions between options, each naming the nodes and relationships it would add. */
    options?: CalmDecision[],
}


/**
 * A relationship in which an actor interacts with nodes.
 */
export interface CalmInteractsType {
    /** The unique-id of the node that acts. */
    actor: string,
    /** The unique-ids of the nodes it interacts with. */
    nodes: string[],
}


/**
 * A relationship in which one node connects to another through their interfaces.
 */
export interface CalmConnectsType {
    /** The end that opens the connection. */
    source_end: CalmNodeInterface,
    /** The end the connection reaches. */
    destination_end: CalmNodeInterface,
}


/**
 * A relationship in which nodes are deployed in a container node.
 */
export interface CalmDeployedInType {
    /** The unique-id of the node the others are deployed in. */
    container: string,
    /** The unique-ids of the deployed nodes. */
    nodes: string[],
}


/**
 * A relationship in which nodes make up a container node.
 */
export interface CalmComposedOfType {
    /** The unique-id of the node the others make up. */
    container: string,
    /** The unique-ids of the nodes it is made of. */
    nodes: string[],
}


/**
 * One option of a choice, naming the nodes, relationships and controls it would add.
 */
export interface CalmDecision {
    /** What choosing this option means. */
    description: string,
    /** The unique-ids of the nodes this option adds. */
    nodes: string[],
    /** The unique-ids of the relationships this option adds. */
    relationships: string[],
    /** The keys of the controls this option adds. */
    controls?: string[],
}


/**
 * Free-form metadata, as an object or a list of objects.
 */
export interface CalmMetadata {
}


/**
 * A business flow, as an ordered list of transitions across the architecture's relationships.
 */
export interface CalmFlow {
    /** Unique identifier for the flow */
    unique_id: string,
    /** Descriptive name for the business flow */
    name: string,
    /** Detailed description of the flow's purpose */
    description: string,
    /** Link to a detailed requirement document */
    requirement_url?: string,
    /** The steps of the flow, each across one relationship. */
    transitions: CalmTransition[],
    /** The controls that apply to this flow. */
    controls?: CalmControls,
    /** Free-form metadata about this flow. */
    metadata?: CalmMetadata,
}


/**
 * One step of a flow, across one relationship of the architecture.
 */
export interface CalmTransition {
    /** Unique identifier for the relationship in the architecture */
    relationship_unique_id: string,
    /** Indicates the sequence of the relationship in the flow */
    sequence_number: number,
    /** Functional summary of what is happening in the transition */
    description: string,
    /** Which way along the relationship the step goes. */
    direction?: string,
}


/**
 * A timeline document, listing the moments of an architecture and naming the current one.
 */
export interface CalmTimeline {
    /** The unique-id of the current architecture moment within the timeline. */
    current_moment?: string,
    /** A list of significant architecture states or points in time, each represented as a 'moment'. */
    moments: CalmNodeMoment[],
    /** Free-form metadata about this timeline. */
    metadata?: CalmMetadata,
}


/**
 * A moment of a timeline: a node of type moment, with no interfaces, whose details point to the architecture of that moment.
 */
export interface CalmNodeMoment extends CalmNode {
    /** The date when this architecture moment came into effect. */
    valid_from?: date,
    /** External links to ADRs (Architecture Decision Records) or similar documents that provide context or decisions related to why the architecture changed. */
    adrs?: string[],
}


/**
 * Supplementary information about elements of one or more architectures, kept apart from the architectures themselves.
 */
export interface CalmDecorator {
    /** URI of the schema that this decorator conforms to, for example a decorator standard */
    decorator_schema?: string,
    /** Unique identifier for this decorator */
    unique_id: string,
    /** Type of decorator - a free-form string identifying the decorator category */
    decorator_type: string,
    /** Optional array of the types of CALM document that this decorator can target. The only type is architecture, because applies-to holds the unique-ids of architecture elements. */
    target_type?: string,
    /** Array of file paths or URLs referencing the CALM architectures this decorator targets */
    target_architectures: string[],
    /** Array of unique-ids referencing nodes, relationships, flows, or other architecture elements */
    applies_to: string[],
    /** Free-form JSON object containing the decorator's data */
    data: CalmDecoratorData,
}


/**
 * The decorator's data, an object free in shape.
 */
export interface CalmDecoratorData {
}


/**
 * An evidence document, which holds one piece of evidence for a control.
 */
export interface CalmEvidenceDocument {
    /** The evidence this document holds. */
    evidence: CalmEvidence,
}


/**
 * Evidence that a control's configuration is met, by the paths where it is kept.
 */
export interface CalmEvidence {
    /** CALM unique-id for future linking and uniquely defining this evidence */
    unique_id: string,
    /** Paths to the evidence relating to a specific control */
    evidence_paths: string[],
    /** URI for the control configuration this evidence relates to */
    control_config_url: string,
}


/**
 * A control requirement: what a control must achieve, which a control detail's requirement-url points to.
 */
export interface CalmControlRequirement {
    /** The unique identifier of this control, which has the potential to be used for linking evidence */
    control_id: string,
    /** The name of the control requirement that provides contextual meaning within a given domain */
    name: string,
    /** A more detailed description of the control and information on what a developer needs to consider */
    description: string,
}


/**
 * A unit of time with a value and a unit type.
 */
export interface CalmTimeUnit {
    /** The unit of time (e.g., seconds, minutes, hours). */
    unit_of_time: string,
    /** The numeric value representing the amount of time. */
    value: number,
}


/**
 * A unit representing a rate (e.g., operations per second).
 */
export interface CalmRateUnit {
    /** The numeric value representing the rate. */
    rate: number,
    /** The time unit defining the rate interval. */
    per: string,
}


/**
 * A CALM architecture document: the nodes of a system, the relationships between them, its business flows, and the controls that apply to it.
 */
export interface CalmArchitecture {
    /** The components of the architecture. */
    nodes?: CalmNode[],
    /** The links between the architecture's nodes. */
    relationships?: CalmRelationship[],
    /** Free-form metadata about the architecture. */
    metadata?: CalmMetadata,
    /** The controls that apply to the whole architecture. */
    controls?: CalmControls,
    /** The business flows that run across the architecture. */
    flows?: CalmFlow[],
    /** External links to ADRs (Architecture Decision Records) or similar documents that provide context or decisions related to the architecture. These can be URLs or references to internal documentation. */
    adrs?: string[],
}



