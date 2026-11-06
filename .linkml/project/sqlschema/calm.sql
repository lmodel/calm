-- # Class: CalmArchitecture Description: A CALM architecture document: the nodes of a system, the relationships between them, its business flows, and the controls that apply to it.
--     * Slot: id
--     * Slot: metadata_id Description: Free-form metadata about the architecture.
--     * Slot: controls_id Description: The controls that apply to the whole architecture.
-- # Class: CalmControls Description: The controls that apply to an architecture element, each under a key of letters, digits and hyphens.
--     * Slot: id
-- # Class: CalmControl Description: One control in a controls map, with the requirements that define it.
--     * Slot: id
--     * Slot: description Description: A description of a control and how it applies to a given architecture
-- # Class: CalmControlDetail Description: A control requirement this control applies, with its configuration given by address or inline, but not both.
--     * Slot: id
--     * Slot: requirement-url Description: The requirement schema that specifies how a control should be defined
--     * Slot: config-url Description: The configuration of how the control requirement schema is met
--     * Slot: CalmControl_id Description: Autocreated FK slot
--     * Slot: config_id Description: Inline configuration of how the control requirement schema is met
-- # Class: CalmControlConfig Description: A configuration object, free in shape, that meets a control requirement.
--     * Slot: id
-- # Class: CalmInterfaceDefinition Description: A modular interface definition referencing an external schema
--     * Slot: id
--     * Slot: unique-id Description: Unique identifier for this interface instance
--     * Slot: definition-url Description: URI of the external schema this interface configuration conforms to
--     * Slot: config_id Description: Inline configuration conforming to the external interface schema
-- # Class: CalmInterfaceConfig Description: A configuration object, free in shape, that an interface definition's schema checks.
--     * Slot: id
-- # Class: CalmInterfaceType Description: An interface given by its own keys, such as a host and port, rather than by an external schema.
--     * Slot: id
--     * Slot: unique-id Description: The interface's identifier, unique within the architecture.
-- # Class: CalmNodeInterface Description: One end of a connection, naming a node and, optionally, which of its interfaces.
--     * Slot: id
--     * Slot: node Description: The unique-id of the node at this end.
-- # Class: CalmNode Description: A component of the architecture, such as a system, service, database or actor, with its interfaces and controls.
--     * Slot: id
--     * Slot: unique-id Description: The node's identifier, unique within the architecture.
--     * Slot: node-type Description: What kind of node this is, one of CALM's built-in types or any other name.
--     * Slot: name Description: The node's name.
--     * Slot: description Description: What the node is and does.
--     * Slot: CalmArchitecture_id Description: Autocreated FK slot
--     * Slot: details_id Description: Where a more detailed architecture of this node is, and the pattern it must follow.
--     * Slot: controls_id Description: The controls that apply to this node.
--     * Slot: metadata_id Description: Free-form metadata about this node.
-- # Class: CalmNodeDetails Description: References from a node to a more detailed architecture and to the pattern it must follow.
--     * Slot: id
--     * Slot: detailed-architecture Description: The address of an architecture document that describes this node in detail.
--     * Slot: required-pattern Description: The address of a pattern that the detailed architecture must follow.
-- # Class: CalmRelationship Description: A link between nodes, of one of CALM's kinds, or a choice between options.
--     * Slot: id
--     * Slot: unique-id Description: The relationship's identifier, unique within the architecture.
--     * Slot: description Description: What the relationship is for.
--     * Slot: protocol Description: The protocol a connection uses.
--     * Slot: CalmArchitecture_id Description: Autocreated FK slot
--     * Slot: relationship-type_id Description: The kind of the relationship and the nodes it links.
--     * Slot: metadata_id Description: Free-form metadata about this relationship.
--     * Slot: controls_id Description: The controls that apply to this relationship.
-- # Class: CalmRelationshipType Description: The kind of a relationship, given by exactly one of its keys: interacts, connects, deployed-in, composed-of or options.
--     * Slot: id
--     * Slot: interacts_id Description: An actor that interacts with nodes.
--     * Slot: connects_id Description: A connection from one node's interfaces to another's.
--     * Slot: deployed-in_id Description: Nodes deployed in a container node.
--     * Slot: composed-of_id Description: Nodes that make up a container node.
-- # Class: CalmInteractsType Description: A relationship in which an actor interacts with nodes.
--     * Slot: id
--     * Slot: actor Description: The unique-id of the node that acts.
-- # Class: CalmConnectsType Description: A relationship in which one node connects to another through their interfaces.
--     * Slot: id
--     * Slot: source_end_id Description: The end that opens the connection.
--     * Slot: destination_end_id Description: The end the connection reaches.
-- # Class: CalmDeployedInType Description: A relationship in which nodes are deployed in a container node.
--     * Slot: id
--     * Slot: container Description: The unique-id of the node the others are deployed in.
-- # Class: CalmComposedOfType Description: A relationship in which nodes make up a container node.
--     * Slot: id
--     * Slot: container Description: The unique-id of the node the others make up.
-- # Class: CalmDecision Description: One option of a choice, naming the nodes, relationships and controls it would add.
--     * Slot: id
--     * Slot: description Description: What choosing this option means.
--     * Slot: CalmRelationshipType_id Description: Autocreated FK slot
-- # Class: CalmMetadata Description: Free-form metadata, as an object or a list of objects.
--     * Slot: id
-- # Class: CalmFlow Description: A business flow, as an ordered list of transitions across the architecture's relationships.
--     * Slot: id
--     * Slot: unique-id Description: Unique identifier for the flow
--     * Slot: name Description: Descriptive name for the business flow
--     * Slot: description Description: Detailed description of the flow's purpose
--     * Slot: requirement-url Description: Link to a detailed requirement document
--     * Slot: CalmArchitecture_id Description: Autocreated FK slot
--     * Slot: controls_id Description: The controls that apply to this flow.
--     * Slot: metadata_id Description: Free-form metadata about this flow.
-- # Class: CalmTransition Description: One step of a flow, across one relationship of the architecture.
--     * Slot: id
--     * Slot: relationship-unique-id Description: Unique identifier for the relationship in the architecture
--     * Slot: sequence-number Description: Indicates the sequence of the relationship in the flow
--     * Slot: description Description: Functional summary of what is happening in the transition
--     * Slot: direction Description: Which way along the relationship the step goes.
--     * Slot: CalmFlow_id Description: Autocreated FK slot
-- # Class: CalmTimeline Description: A timeline document, listing the moments of an architecture and naming the current one.
--     * Slot: id
--     * Slot: current-moment Description: The unique-id of the current architecture moment within the timeline.
--     * Slot: metadata_id Description: Free-form metadata about this timeline.
-- # Class: CalmNodeMoment Description: A moment of a timeline: a node of type moment, with no interfaces, whose details point to the architecture of that moment.
--     * Slot: id
--     * Slot: valid-from Description: The date when this architecture moment came into effect.
--     * Slot: unique-id Description: The node's identifier, unique within the architecture.
--     * Slot: node-type Description: What kind of node this is, one of CALM's built-in types or any other name.
--     * Slot: name Description: The node's name.
--     * Slot: description Description: What the node is and does.
--     * Slot: CalmTimeline_id Description: Autocreated FK slot
--     * Slot: details_id Description: Where a more detailed architecture of this node is, and the pattern it must follow.
--     * Slot: controls_id Description: The controls that apply to this node.
--     * Slot: metadata_id Description: Free-form metadata about this node.
-- # Class: CalmDecorator Description: Supplementary information about elements of one or more architectures, kept apart from the architectures themselves.
--     * Slot: id
--     * Slot: decorator_schema Description: URI of the schema that this decorator conforms to, for example a decorator standard
--     * Slot: unique-id Description: Unique identifier for this decorator
--     * Slot: decorator_type Description: Type of decorator - a free-form string identifying the decorator category
--     * Slot: data_id Description: Free-form JSON object containing the decorator's data
-- # Class: CalmDecoratorData Description: The decorator's data, an object free in shape.
--     * Slot: id
-- # Class: CalmEvidenceDocument Description: An evidence document, which holds one piece of evidence for a control.
--     * Slot: id
--     * Slot: evidence_id Description: The evidence this document holds.
-- # Class: CalmEvidence Description: Evidence that a control's configuration is met, by the paths where it is kept.
--     * Slot: id
--     * Slot: unique-id Description: CALM unique-id for future linking and uniquely defining this evidence
--     * Slot: control-config-url Description: URI for the control configuration this evidence relates to
-- # Class: CalmControlRequirement Description: A control requirement: what a control must achieve, which a control detail's requirement-url points to.
--     * Slot: id
--     * Slot: control-id Description: The unique identifier of this control, which has the potential to be used for linking evidence
--     * Slot: name Description: The name of the control requirement that provides contextual meaning within a given domain
--     * Slot: description Description: A more detailed description of the control and information on what a developer needs to consider
-- # Class: CalmTimeUnit Description: A unit of time with a value and a unit type.
--     * Slot: id
--     * Slot: unit_of_time Description: The unit of time (e.g., seconds, minutes, hours).
--     * Slot: value Description: The numeric value representing the amount of time.
-- # Class: CalmRateUnit Description: A unit representing a rate (e.g., operations per second).
--     * Slot: id
--     * Slot: rate Description: The numeric value representing the rate.
--     * Slot: per Description: The time unit defining the rate interval.
-- # Class: CalmArchitecture_adrs
--     * Slot: CalmArchitecture_id Description: Autocreated FK slot
--     * Slot: adrs Description: External links to ADRs (Architecture Decision Records) or similar documents that provide context or decisions related to the architecture. These can be URLs or references to internal documentation.
-- # Class: CalmNodeInterface_interfaces
--     * Slot: CalmNodeInterface_id Description: Autocreated FK slot
--     * Slot: interfaces Description: The unique-ids of the node's interfaces this end uses.
-- # Class: CalmNode_interfaces
--     * Slot: CalmNode_id Description: Autocreated FK slot
--     * Slot: interfaces Description: The interfaces the node exposes.
-- # Class: CalmInteractsType_nodes
--     * Slot: CalmInteractsType_id Description: Autocreated FK slot
--     * Slot: nodes Description: The unique-ids of the nodes it interacts with.
-- # Class: CalmDeployedInType_nodes
--     * Slot: CalmDeployedInType_id Description: Autocreated FK slot
--     * Slot: nodes Description: The unique-ids of the deployed nodes.
-- # Class: CalmComposedOfType_nodes
--     * Slot: CalmComposedOfType_id Description: Autocreated FK slot
--     * Slot: nodes Description: The unique-ids of the nodes it is made of.
-- # Class: CalmDecision_nodes
--     * Slot: CalmDecision_id Description: Autocreated FK slot
--     * Slot: nodes Description: The unique-ids of the nodes this option adds.
-- # Class: CalmDecision_relationships
--     * Slot: CalmDecision_id Description: Autocreated FK slot
--     * Slot: relationships Description: The unique-ids of the relationships this option adds.
-- # Class: CalmDecision_controls
--     * Slot: CalmDecision_id Description: Autocreated FK slot
--     * Slot: controls Description: The keys of the controls this option adds.
-- # Class: CalmNodeMoment_adrs
--     * Slot: CalmNodeMoment_id Description: Autocreated FK slot
--     * Slot: adrs Description: External links to ADRs (Architecture Decision Records) or similar documents that provide context or decisions related to why the architecture changed.
-- # Class: CalmNodeMoment_interfaces
--     * Slot: CalmNodeMoment_id Description: Autocreated FK slot
--     * Slot: interfaces Description: The interfaces the node exposes.
-- # Class: CalmDecorator_target-type
--     * Slot: CalmDecorator_id Description: Autocreated FK slot
--     * Slot: target-type Description: Optional array of the types of CALM document that this decorator can target. The only type is architecture, because applies-to holds the unique-ids of architecture elements.
-- # Class: CalmDecorator_target_architectures
--     * Slot: CalmDecorator_id Description: Autocreated FK slot
--     * Slot: target_architectures Description: Array of file paths or URLs referencing the CALM architectures this decorator targets
-- # Class: CalmDecorator_applies-to
--     * Slot: CalmDecorator_id Description: Autocreated FK slot
--     * Slot: applies-to Description: Array of unique-ids referencing nodes, relationships, flows, or other architecture elements
-- # Class: CalmEvidence_evidence-paths
--     * Slot: CalmEvidence_id Description: Autocreated FK slot
--     * Slot: evidence-paths Description: Paths to the evidence relating to a specific control

CREATE TABLE "CalmControls" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CalmControls_id" ON "CalmControls" (id);

CREATE TABLE "CalmControl" (
	id INTEGER NOT NULL,
	description TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CalmControl_id" ON "CalmControl" (id);

CREATE TABLE "CalmControlConfig" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CalmControlConfig_id" ON "CalmControlConfig" (id);

CREATE TABLE "CalmInterfaceConfig" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CalmInterfaceConfig_id" ON "CalmInterfaceConfig" (id);

CREATE TABLE "CalmInterfaceType" (
	id INTEGER NOT NULL,
	"unique-id" TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CalmInterfaceType_id" ON "CalmInterfaceType" (id);

CREATE TABLE "CalmNodeInterface" (
	id INTEGER NOT NULL,
	node TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CalmNodeInterface_id" ON "CalmNodeInterface" (id);

CREATE TABLE "CalmNodeDetails" (
	id INTEGER NOT NULL,
	"detailed-architecture" TEXT,
	"required-pattern" TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CalmNodeDetails_id" ON "CalmNodeDetails" (id);

CREATE TABLE "CalmInteractsType" (
	id INTEGER NOT NULL,
	actor TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CalmInteractsType_id" ON "CalmInteractsType" (id);

CREATE TABLE "CalmDeployedInType" (
	id INTEGER NOT NULL,
	container TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CalmDeployedInType_id" ON "CalmDeployedInType" (id);

CREATE TABLE "CalmComposedOfType" (
	id INTEGER NOT NULL,
	container TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CalmComposedOfType_id" ON "CalmComposedOfType" (id);

CREATE TABLE "CalmMetadata" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CalmMetadata_id" ON "CalmMetadata" (id);

CREATE TABLE "CalmDecoratorData" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CalmDecoratorData_id" ON "CalmDecoratorData" (id);

CREATE TABLE "CalmEvidence" (
	id INTEGER NOT NULL,
	"unique-id" TEXT NOT NULL,
	"control-config-url" TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CalmEvidence_id" ON "CalmEvidence" (id);

CREATE TABLE "CalmControlRequirement" (
	id INTEGER NOT NULL,
	"control-id" TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CalmControlRequirement_id" ON "CalmControlRequirement" (id);

CREATE TABLE "CalmTimeUnit" (
	id INTEGER NOT NULL,
	unit_of_time VARCHAR(12) NOT NULL,
	value FLOAT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CalmTimeUnit_id" ON "CalmTimeUnit" (id);

CREATE TABLE "CalmRateUnit" (
	id INTEGER NOT NULL,
	rate FLOAT NOT NULL,
	per VARCHAR(11) NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CalmRateUnit_id" ON "CalmRateUnit" (id);

CREATE TABLE "CalmArchitecture" (
	id INTEGER NOT NULL,
	metadata_id INTEGER,
	controls_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(metadata_id) REFERENCES "CalmMetadata" (id),
	FOREIGN KEY(controls_id) REFERENCES "CalmControls" (id)
);
CREATE INDEX "ix_CalmArchitecture_id" ON "CalmArchitecture" (id);

CREATE TABLE "CalmControlDetail" (
	id INTEGER NOT NULL,
	"requirement-url" TEXT NOT NULL,
	"config-url" TEXT,
	"CalmControl_id" INTEGER,
	config_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CalmControl_id") REFERENCES "CalmControl" (id),
	FOREIGN KEY(config_id) REFERENCES "CalmControlConfig" (id)
);
CREATE INDEX "ix_CalmControlDetail_id" ON "CalmControlDetail" (id);

CREATE TABLE "CalmInterfaceDefinition" (
	id INTEGER NOT NULL,
	"unique-id" TEXT NOT NULL,
	"definition-url" TEXT NOT NULL,
	config_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(config_id) REFERENCES "CalmInterfaceConfig" (id)
);
CREATE INDEX "ix_CalmInterfaceDefinition_id" ON "CalmInterfaceDefinition" (id);

CREATE TABLE "CalmConnectsType" (
	id INTEGER NOT NULL,
	source_end_id INTEGER NOT NULL,
	destination_end_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(source_end_id) REFERENCES "CalmNodeInterface" (id),
	FOREIGN KEY(destination_end_id) REFERENCES "CalmNodeInterface" (id)
);
CREATE INDEX "ix_CalmConnectsType_id" ON "CalmConnectsType" (id);

CREATE TABLE "CalmTimeline" (
	id INTEGER NOT NULL,
	"current-moment" TEXT,
	metadata_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(metadata_id) REFERENCES "CalmMetadata" (id)
);
CREATE INDEX "ix_CalmTimeline_id" ON "CalmTimeline" (id);

CREATE TABLE "CalmDecorator" (
	id INTEGER NOT NULL,
	decorator_schema TEXT,
	"unique-id" TEXT NOT NULL,
	decorator_type TEXT NOT NULL,
	data_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(data_id) REFERENCES "CalmDecoratorData" (id)
);
CREATE INDEX "ix_CalmDecorator_id" ON "CalmDecorator" (id);

CREATE TABLE "CalmEvidenceDocument" (
	id INTEGER NOT NULL,
	evidence_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(evidence_id) REFERENCES "CalmEvidence" (id)
);
CREATE INDEX "ix_CalmEvidenceDocument_id" ON "CalmEvidenceDocument" (id);

CREATE TABLE "CalmNodeInterface_interfaces" (
	"CalmNodeInterface_id" INTEGER,
	interfaces TEXT,
	PRIMARY KEY ("CalmNodeInterface_id", interfaces),
	FOREIGN KEY("CalmNodeInterface_id") REFERENCES "CalmNodeInterface" (id)
);
CREATE INDEX "ix_CalmNodeInterface_interfaces_interfaces" ON "CalmNodeInterface_interfaces" (interfaces);
CREATE INDEX "ix_CalmNodeInterface_interfaces_CalmNodeInterface_id" ON "CalmNodeInterface_interfaces" ("CalmNodeInterface_id");

CREATE TABLE "CalmInteractsType_nodes" (
	"CalmInteractsType_id" INTEGER,
	nodes TEXT NOT NULL,
	PRIMARY KEY ("CalmInteractsType_id", nodes),
	FOREIGN KEY("CalmInteractsType_id") REFERENCES "CalmInteractsType" (id)
);
CREATE INDEX "ix_CalmInteractsType_nodes_CalmInteractsType_id" ON "CalmInteractsType_nodes" ("CalmInteractsType_id");
CREATE INDEX "ix_CalmInteractsType_nodes_nodes" ON "CalmInteractsType_nodes" (nodes);

CREATE TABLE "CalmDeployedInType_nodes" (
	"CalmDeployedInType_id" INTEGER,
	nodes TEXT NOT NULL,
	PRIMARY KEY ("CalmDeployedInType_id", nodes),
	FOREIGN KEY("CalmDeployedInType_id") REFERENCES "CalmDeployedInType" (id)
);
CREATE INDEX "ix_CalmDeployedInType_nodes_nodes" ON "CalmDeployedInType_nodes" (nodes);
CREATE INDEX "ix_CalmDeployedInType_nodes_CalmDeployedInType_id" ON "CalmDeployedInType_nodes" ("CalmDeployedInType_id");

CREATE TABLE "CalmComposedOfType_nodes" (
	"CalmComposedOfType_id" INTEGER,
	nodes TEXT NOT NULL,
	PRIMARY KEY ("CalmComposedOfType_id", nodes),
	FOREIGN KEY("CalmComposedOfType_id") REFERENCES "CalmComposedOfType" (id)
);
CREATE INDEX "ix_CalmComposedOfType_nodes_nodes" ON "CalmComposedOfType_nodes" (nodes);
CREATE INDEX "ix_CalmComposedOfType_nodes_CalmComposedOfType_id" ON "CalmComposedOfType_nodes" ("CalmComposedOfType_id");

CREATE TABLE "CalmEvidence_evidence-paths" (
	"CalmEvidence_id" INTEGER,
	"evidence-paths" TEXT NOT NULL,
	PRIMARY KEY ("CalmEvidence_id", "evidence-paths"),
	FOREIGN KEY("CalmEvidence_id") REFERENCES "CalmEvidence" (id)
);
CREATE INDEX "ix_CalmEvidence_evidence-paths_CalmEvidence_id" ON "CalmEvidence_evidence-paths" ("CalmEvidence_id");
CREATE INDEX "ix_CalmEvidence_evidence-paths_evidence-paths" ON "CalmEvidence_evidence-paths" ("evidence-paths");

CREATE TABLE "CalmNode" (
	id INTEGER NOT NULL,
	"unique-id" TEXT NOT NULL,
	"node-type" TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	"CalmArchitecture_id" INTEGER,
	details_id INTEGER,
	controls_id INTEGER,
	metadata_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CalmArchitecture_id") REFERENCES "CalmArchitecture" (id),
	FOREIGN KEY(details_id) REFERENCES "CalmNodeDetails" (id),
	FOREIGN KEY(controls_id) REFERENCES "CalmControls" (id),
	FOREIGN KEY(metadata_id) REFERENCES "CalmMetadata" (id)
);
CREATE INDEX "ix_CalmNode_id" ON "CalmNode" (id);

CREATE TABLE "CalmRelationshipType" (
	id INTEGER NOT NULL,
	interacts_id INTEGER,
	connects_id INTEGER,
	"deployed-in_id" INTEGER,
	"composed-of_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(interacts_id) REFERENCES "CalmInteractsType" (id),
	FOREIGN KEY(connects_id) REFERENCES "CalmConnectsType" (id),
	FOREIGN KEY("deployed-in_id") REFERENCES "CalmDeployedInType" (id),
	FOREIGN KEY("composed-of_id") REFERENCES "CalmComposedOfType" (id)
);
CREATE INDEX "ix_CalmRelationshipType_id" ON "CalmRelationshipType" (id);

CREATE TABLE "CalmFlow" (
	id INTEGER NOT NULL,
	"unique-id" TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	"requirement-url" TEXT,
	"CalmArchitecture_id" INTEGER,
	controls_id INTEGER,
	metadata_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CalmArchitecture_id") REFERENCES "CalmArchitecture" (id),
	FOREIGN KEY(controls_id) REFERENCES "CalmControls" (id),
	FOREIGN KEY(metadata_id) REFERENCES "CalmMetadata" (id)
);
CREATE INDEX "ix_CalmFlow_id" ON "CalmFlow" (id);

CREATE TABLE "CalmNodeMoment" (
	id INTEGER NOT NULL,
	"valid-from" DATE,
	"unique-id" TEXT NOT NULL,
	"node-type" TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	"CalmTimeline_id" INTEGER,
	details_id INTEGER,
	controls_id INTEGER,
	metadata_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CalmTimeline_id") REFERENCES "CalmTimeline" (id),
	FOREIGN KEY(details_id) REFERENCES "CalmNodeDetails" (id),
	FOREIGN KEY(controls_id) REFERENCES "CalmControls" (id),
	FOREIGN KEY(metadata_id) REFERENCES "CalmMetadata" (id)
);
CREATE INDEX "ix_CalmNodeMoment_id" ON "CalmNodeMoment" (id);

CREATE TABLE "CalmArchitecture_adrs" (
	"CalmArchitecture_id" INTEGER,
	adrs TEXT,
	PRIMARY KEY ("CalmArchitecture_id", adrs),
	FOREIGN KEY("CalmArchitecture_id") REFERENCES "CalmArchitecture" (id)
);
CREATE INDEX "ix_CalmArchitecture_adrs_adrs" ON "CalmArchitecture_adrs" (adrs);
CREATE INDEX "ix_CalmArchitecture_adrs_CalmArchitecture_id" ON "CalmArchitecture_adrs" ("CalmArchitecture_id");

CREATE TABLE "CalmDecorator_target-type" (
	"CalmDecorator_id" INTEGER,
	"target-type" VARCHAR(12),
	PRIMARY KEY ("CalmDecorator_id", "target-type"),
	FOREIGN KEY("CalmDecorator_id") REFERENCES "CalmDecorator" (id)
);
CREATE INDEX "ix_CalmDecorator_target-type_CalmDecorator_id" ON "CalmDecorator_target-type" ("CalmDecorator_id");
CREATE INDEX "ix_CalmDecorator_target-type_target-type" ON "CalmDecorator_target-type" ("target-type");

CREATE TABLE "CalmDecorator_target_architectures" (
	"CalmDecorator_id" INTEGER,
	target_architectures TEXT NOT NULL,
	PRIMARY KEY ("CalmDecorator_id", target_architectures),
	FOREIGN KEY("CalmDecorator_id") REFERENCES "CalmDecorator" (id)
);
CREATE INDEX "ix_CalmDecorator_target_architectures_CalmDecorator_id" ON "CalmDecorator_target_architectures" ("CalmDecorator_id");
CREATE INDEX "ix_CalmDecorator_target_architectures_target_architectures" ON "CalmDecorator_target_architectures" (target_architectures);

CREATE TABLE "CalmDecorator_applies-to" (
	"CalmDecorator_id" INTEGER,
	"applies-to" TEXT NOT NULL,
	PRIMARY KEY ("CalmDecorator_id", "applies-to"),
	FOREIGN KEY("CalmDecorator_id") REFERENCES "CalmDecorator" (id)
);
CREATE INDEX "ix_CalmDecorator_applies-to_CalmDecorator_id" ON "CalmDecorator_applies-to" ("CalmDecorator_id");
CREATE INDEX "ix_CalmDecorator_applies-to_applies-to" ON "CalmDecorator_applies-to" ("applies-to");

CREATE TABLE "CalmRelationship" (
	id INTEGER NOT NULL,
	"unique-id" TEXT NOT NULL,
	description TEXT,
	protocol VARCHAR(9),
	"CalmArchitecture_id" INTEGER,
	"relationship-type_id" INTEGER NOT NULL,
	metadata_id INTEGER,
	controls_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CalmArchitecture_id") REFERENCES "CalmArchitecture" (id),
	FOREIGN KEY("relationship-type_id") REFERENCES "CalmRelationshipType" (id),
	FOREIGN KEY(metadata_id) REFERENCES "CalmMetadata" (id),
	FOREIGN KEY(controls_id) REFERENCES "CalmControls" (id)
);
CREATE INDEX "ix_CalmRelationship_id" ON "CalmRelationship" (id);

CREATE TABLE "CalmDecision" (
	id INTEGER NOT NULL,
	description TEXT NOT NULL,
	"CalmRelationshipType_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CalmRelationshipType_id") REFERENCES "CalmRelationshipType" (id)
);
CREATE INDEX "ix_CalmDecision_id" ON "CalmDecision" (id);

CREATE TABLE "CalmTransition" (
	id INTEGER NOT NULL,
	"relationship-unique-id" TEXT NOT NULL,
	"sequence-number" INTEGER NOT NULL,
	description TEXT NOT NULL,
	direction VARCHAR(21),
	"CalmFlow_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CalmFlow_id") REFERENCES "CalmFlow" (id)
);
CREATE INDEX "ix_CalmTransition_id" ON "CalmTransition" (id);

CREATE TABLE "CalmNode_interfaces" (
	"CalmNode_id" INTEGER,
	interfaces TEXT,
	PRIMARY KEY ("CalmNode_id", interfaces),
	FOREIGN KEY("CalmNode_id") REFERENCES "CalmNode" (id)
);
CREATE INDEX "ix_CalmNode_interfaces_CalmNode_id" ON "CalmNode_interfaces" ("CalmNode_id");
CREATE INDEX "ix_CalmNode_interfaces_interfaces" ON "CalmNode_interfaces" (interfaces);

CREATE TABLE "CalmNodeMoment_adrs" (
	"CalmNodeMoment_id" INTEGER,
	adrs TEXT,
	PRIMARY KEY ("CalmNodeMoment_id", adrs),
	FOREIGN KEY("CalmNodeMoment_id") REFERENCES "CalmNodeMoment" (id)
);
CREATE INDEX "ix_CalmNodeMoment_adrs_adrs" ON "CalmNodeMoment_adrs" (adrs);
CREATE INDEX "ix_CalmNodeMoment_adrs_CalmNodeMoment_id" ON "CalmNodeMoment_adrs" ("CalmNodeMoment_id");

CREATE TABLE "CalmNodeMoment_interfaces" (
	"CalmNodeMoment_id" INTEGER,
	interfaces TEXT,
	PRIMARY KEY ("CalmNodeMoment_id", interfaces),
	FOREIGN KEY("CalmNodeMoment_id") REFERENCES "CalmNodeMoment" (id)
);
CREATE INDEX "ix_CalmNodeMoment_interfaces_CalmNodeMoment_id" ON "CalmNodeMoment_interfaces" ("CalmNodeMoment_id");
CREATE INDEX "ix_CalmNodeMoment_interfaces_interfaces" ON "CalmNodeMoment_interfaces" (interfaces);

CREATE TABLE "CalmDecision_nodes" (
	"CalmDecision_id" INTEGER,
	nodes TEXT NOT NULL,
	PRIMARY KEY ("CalmDecision_id", nodes),
	FOREIGN KEY("CalmDecision_id") REFERENCES "CalmDecision" (id)
);
CREATE INDEX "ix_CalmDecision_nodes_CalmDecision_id" ON "CalmDecision_nodes" ("CalmDecision_id");
CREATE INDEX "ix_CalmDecision_nodes_nodes" ON "CalmDecision_nodes" (nodes);

CREATE TABLE "CalmDecision_relationships" (
	"CalmDecision_id" INTEGER,
	relationships TEXT NOT NULL,
	PRIMARY KEY ("CalmDecision_id", relationships),
	FOREIGN KEY("CalmDecision_id") REFERENCES "CalmDecision" (id)
);
CREATE INDEX "ix_CalmDecision_relationships_CalmDecision_id" ON "CalmDecision_relationships" ("CalmDecision_id");
CREATE INDEX "ix_CalmDecision_relationships_relationships" ON "CalmDecision_relationships" (relationships);

CREATE TABLE "CalmDecision_controls" (
	"CalmDecision_id" INTEGER,
	controls TEXT,
	PRIMARY KEY ("CalmDecision_id", controls),
	FOREIGN KEY("CalmDecision_id") REFERENCES "CalmDecision" (id)
);
CREATE INDEX "ix_CalmDecision_controls_controls" ON "CalmDecision_controls" (controls);
CREATE INDEX "ix_CalmDecision_controls_CalmDecision_id" ON "CalmDecision_controls" ("CalmDecision_id");
