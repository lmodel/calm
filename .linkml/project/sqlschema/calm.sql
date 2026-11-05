-- # Class: Architecture Description: Top-level CALM architecture document.
--     * Slot: id
--     * Slot: metadata
--     * Slot: controls_id
-- # Class: Node Description: A logical or physical element of an architecture (system, service, actor, ...).
--     * Slot: unique_id Description: Stable opaque identifier used to cross-link CALM elements.
--     * Slot: node_type Description: Category of the node (system, service, actor, etc.).
--     * Slot: name Description: Short human-readable name.
--     * Slot: description Description: Free-form description of the element.
--     * Slot: details
--     * Slot: metadata
--     * Slot: Architecture_id Description: Autocreated FK slot
--     * Slot: Decision_id Description: Autocreated FK slot
--     * Slot: controls_id
-- # Class: Relationship Description: A typed link between architecture elements.
--     * Slot: unique_id Description: Stable opaque identifier used to cross-link CALM elements.
--     * Slot: description Description: Free-form description of the element.
--     * Slot: protocol
--     * Slot: metadata
--     * Slot: Architecture_id Description: Autocreated FK slot
--     * Slot: Decision_id Description: Autocreated FK slot
--     * Slot: relationship_type_id
--     * Slot: controls_id
-- # Class: InteractsRelationship Description: An ``interacts`` relationship between an actor and one or more nodes.
--     * Slot: id
--     * Slot: actor
-- # Class: ConnectsRelationship Description: A ``connects`` relationship between two node interfaces.
--     * Slot: id
--     * Slot: source_id
--     * Slot: destination_id
-- # Class: DeployedInRelationship Description: A ``deployed-in`` containment relationship.
--     * Slot: id
--     * Slot: container
-- # Class: ComposedOfRelationship Description: A ``composed-of`` containment relationship.
--     * Slot: id
--     * Slot: container
-- # Class: Decision Description: A candidate decision within an ``options`` relationship.
--     * Slot: id
--     * Slot: description Description: Free-form description of the element.
--     * Slot: OptionList_id Description: Autocreated FK slot
--     * Slot: RelationshipType_id Description: Autocreated FK slot
--     * Slot: controls_id
-- # Class: ControlDetail Description: A single control requirement and its inline / referenced configuration.
--     * Slot: id
--     * Slot: requirement_url Description: The requirement schema that specifies how a control should be defined
--     * Slot: config_url Description: The configuration of how the control requirement schema is met
--     * Slot: config Description: Inline configuration of how the control requirement schema is met
-- # Class: Control Description: A named control attached to an architecture element.
--     * Slot: id
-- # Class: ControlRequirement Description: Domain-defined control requirement that controls can reference.
--     * Slot: control_id Description: The unique identifier of this control, which has the potential to be used for linking evidence
--     * Slot: name Description: Short human-readable name.
--     * Slot: description Description: Free-form description of the element.
-- # Class: Decorator Description: Cross-cutting annotation attached to nodes, relationships, or flows.
--     * Slot: unique_id Description: Stable opaque identifier used to cross-link CALM elements.
--     * Slot: type Description: Type of decorator - a free-form string identifying the decorator category
--     * Slot: data Description: Free-form JSON object containing the decorator's data
-- # Class: EvidenceDocument Description: Top-level CALM evidence document linking control configurations to evidence artefacts.
--     * Slot: id
--     * Slot: evidence
-- # Class: Transition Description: A single step in a flow, anchored on a relationship.
--     * Slot: id
--     * Slot: relationship_unique_id Description: Unique identifier for the relationship in the architecture
--     * Slot: sequence_number Description: Indicates the sequence of the relationship in the flow
--     * Slot: description Description: Free-form description of the element.
--     * Slot: direction Description: Direction of flow on the transition.
-- # Class: Flow Description: Business flow mapped onto architecture relationships.
--     * Slot: unique_id Description: Stable opaque identifier used to cross-link CALM elements.
--     * Slot: name Description: Short human-readable name.
--     * Slot: description Description: Free-form description of the element.
--     * Slot: requirement_url Description: The requirement schema that specifies how a control should be defined
--     * Slot: metadata
--     * Slot: Architecture_id Description: Autocreated FK slot
--     * Slot: controls_id
-- # Class: InterfaceDefinition Description: Modular interface definition referencing an external schema.
--     * Slot: unique_id Description: Stable opaque identifier used to cross-link CALM elements.
--     * Slot: definition_url Description: URI of the external schema this interface configuration conforms to
--     * Slot: config Description: Inline configuration of how the control requirement schema is met
--     * Slot: Node_unique_id Description: Autocreated FK slot
--     * Slot: NodeInterface_id Description: Autocreated FK slot
--     * Slot: NodeMoment_unique_id Description: Autocreated FK slot
-- # Class: InterfaceType Description: Inline (free-form) interface definition keyed by unique-id.
--     * Slot: unique_id Description: Stable opaque identifier used to cross-link CALM elements.
-- # Class: NodeInterface Description: Reference to one or more interfaces exposed by a node.
--     * Slot: id
--     * Slot: node
-- # Class: Timeline Description: CALM timeline document capturing architecture moments over time.
--     * Slot: id
--     * Slot: current_moment Description: The unique-id of the current architecture moment within the timeline.
--     * Slot: metadata
-- # Class: NodeMoment Description: An architecture moment - a point-in-time snapshot of the architecture.
--     * Slot: node_type Description: Category of the node (system, service, actor, etc.).
--     * Slot: valid_from Description: The date when this architecture moment came into effect.
--     * Slot: unique_id Description: Stable opaque identifier used to cross-link CALM elements.
--     * Slot: name Description: Short human-readable name.
--     * Slot: description Description: Free-form description of the element.
--     * Slot: details
--     * Slot: metadata
--     * Slot: controls_id
-- # Class: TimeUnit Description: A quantity of time expressed as a numeric value and a unit.
--     * Slot: id
--     * Slot: unit Description: The unit of time (e.g., seconds, minutes, hours).
--     * Slot: value Description: The numeric value representing the amount of time.
-- # Class: RateUnit Description: A rate (count per time unit), e.g. operations per second.
--     * Slot: id
--     * Slot: rate Description: The numeric value representing the rate.
--     * Slot: per Description: The time unit defining the rate interval.
-- # Class: OptionList Description: Wrapper around the list of ``Decision`` alternatives in an options relationship.
--     * Slot: id
-- # Class: RelationshipType Description: Tagged-union container for the variant body of a relationship. Exactly one of ``interacts``, ``connects``, ``deployed_in``, ``composed_of``, ``options`` is populated; see ``RelationshipKind`` for the discriminator values.
--     * Slot: id
--     * Slot: interacts_id
--     * Slot: connects_id
--     * Slot: deployed_in_id
--     * Slot: composed_of_id
-- # Class: Architecture_adrs
--     * Slot: Architecture_id Description: Autocreated FK slot
--     * Slot: adrs Description: External links to ADRs (Architecture Decision Records) or similar documents that provide context or decisions related to the architecture. These can be URLs or references to internal documentation.
-- # Class: InteractsRelationship_nodes
--     * Slot: InteractsRelationship_id Description: Autocreated FK slot
--     * Slot: nodes_unique_id
-- # Class: DeployedInRelationship_nodes
--     * Slot: DeployedInRelationship_id Description: Autocreated FK slot
--     * Slot: nodes_unique_id
-- # Class: ComposedOfRelationship_nodes
--     * Slot: ComposedOfRelationship_id Description: Autocreated FK slot
--     * Slot: nodes_unique_id
-- # Class: Decorator_target
--     * Slot: Decorator_unique_id Description: Autocreated FK slot
--     * Slot: target Description: Array of file paths or URLs referencing the CALM documents (patterns, architectures, or controls) this decorator targets
-- # Class: Decorator_applies_to
--     * Slot: Decorator_unique_id Description: Autocreated FK slot
--     * Slot: applies_to Description: Array of unique-ids referencing nodes, relationships, flows, or other architecture elements
-- # Class: Flow_transitions
--     * Slot: Flow_unique_id Description: Autocreated FK slot
--     * Slot: transitions_id
-- # Class: Timeline_moments
--     * Slot: Timeline_id Description: Autocreated FK slot
--     * Slot: moments Description: A list of significant architecture states or points in time, each represented as a 'moment'.
-- # Class: NodeMoment_adrs
--     * Slot: NodeMoment_unique_id Description: Autocreated FK slot
--     * Slot: adrs Description: External links to ADRs (Architecture Decision Records) or similar documents that provide context or decisions related to the architecture. These can be URLs or references to internal documentation.

CREATE TABLE "InteractsRelationship" (
	id INTEGER NOT NULL,
	actor TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InteractsRelationship_id" ON "InteractsRelationship" (id);

CREATE TABLE "DeployedInRelationship" (
	id INTEGER NOT NULL,
	container TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DeployedInRelationship_id" ON "DeployedInRelationship" (id);

CREATE TABLE "ComposedOfRelationship" (
	id INTEGER NOT NULL,
	container TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ComposedOfRelationship_id" ON "ComposedOfRelationship" (id);

CREATE TABLE "ControlDetail" (
	id INTEGER NOT NULL,
	requirement_url TEXT NOT NULL,
	config_url TEXT,
	config TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ControlDetail_id" ON "ControlDetail" (id);

CREATE TABLE "Control" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Control_id" ON "Control" (id);

CREATE TABLE "ControlRequirement" (
	control_id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	PRIMARY KEY (control_id)
);
CREATE INDEX "ix_ControlRequirement_control_id" ON "ControlRequirement" (control_id);

CREATE TABLE "Decorator" (
	unique_id TEXT NOT NULL,
	type TEXT NOT NULL,
	data TEXT NOT NULL,
	PRIMARY KEY (unique_id)
);
CREATE INDEX "ix_Decorator_unique_id" ON "Decorator" (unique_id);

CREATE TABLE "EvidenceDocument" (
	id INTEGER NOT NULL,
	evidence TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_EvidenceDocument_id" ON "EvidenceDocument" (id);

CREATE TABLE "Transition" (
	id INTEGER NOT NULL,
	relationship_unique_id TEXT NOT NULL,
	sequence_number INTEGER NOT NULL,
	description TEXT NOT NULL,
	direction VARCHAR(21),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Transition_id" ON "Transition" (id);

CREATE TABLE "InterfaceType" (
	unique_id TEXT NOT NULL,
	PRIMARY KEY (unique_id)
);
CREATE INDEX "ix_InterfaceType_unique_id" ON "InterfaceType" (unique_id);

CREATE TABLE "NodeInterface" (
	id INTEGER NOT NULL,
	node TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NodeInterface_id" ON "NodeInterface" (id);

CREATE TABLE "Timeline" (
	id INTEGER NOT NULL,
	current_moment TEXT,
	metadata TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Timeline_id" ON "Timeline" (id);

CREATE TABLE "TimeUnit" (
	id INTEGER NOT NULL,
	unit VARCHAR(12) NOT NULL,
	value FLOAT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_TimeUnit_id" ON "TimeUnit" (id);

CREATE TABLE "RateUnit" (
	id INTEGER NOT NULL,
	rate FLOAT NOT NULL,
	per VARCHAR(11) NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_RateUnit_id" ON "RateUnit" (id);

CREATE TABLE "OptionList" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OptionList_id" ON "OptionList" (id);

CREATE TABLE "Architecture" (
	id INTEGER NOT NULL,
	metadata TEXT,
	controls_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(controls_id) REFERENCES "Control" (id)
);
CREATE INDEX "ix_Architecture_id" ON "Architecture" (id);

CREATE TABLE "ConnectsRelationship" (
	id INTEGER NOT NULL,
	source_id INTEGER NOT NULL,
	destination_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(source_id) REFERENCES "NodeInterface" (id),
	FOREIGN KEY(destination_id) REFERENCES "NodeInterface" (id)
);
CREATE INDEX "ix_ConnectsRelationship_id" ON "ConnectsRelationship" (id);

CREATE TABLE "NodeMoment" (
	node_type VARCHAR(10) NOT NULL,
	valid_from DATE,
	unique_id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	details TEXT NOT NULL,
	metadata TEXT,
	controls_id INTEGER,
	PRIMARY KEY (unique_id),
	FOREIGN KEY(controls_id) REFERENCES "Control" (id)
);
CREATE INDEX "ix_NodeMoment_unique_id" ON "NodeMoment" (unique_id);

CREATE TABLE "Decorator_target" (
	"Decorator_unique_id" TEXT,
	target TEXT NOT NULL,
	PRIMARY KEY ("Decorator_unique_id", target),
	FOREIGN KEY("Decorator_unique_id") REFERENCES "Decorator" (unique_id)
);
CREATE INDEX "ix_Decorator_target_Decorator_unique_id" ON "Decorator_target" ("Decorator_unique_id");
CREATE INDEX "ix_Decorator_target_target" ON "Decorator_target" (target);

CREATE TABLE "Decorator_applies_to" (
	"Decorator_unique_id" TEXT,
	applies_to TEXT NOT NULL,
	PRIMARY KEY ("Decorator_unique_id", applies_to),
	FOREIGN KEY("Decorator_unique_id") REFERENCES "Decorator" (unique_id)
);
CREATE INDEX "ix_Decorator_applies_to_Decorator_unique_id" ON "Decorator_applies_to" ("Decorator_unique_id");
CREATE INDEX "ix_Decorator_applies_to_applies_to" ON "Decorator_applies_to" (applies_to);

CREATE TABLE "Timeline_moments" (
	"Timeline_id" INTEGER,
	moments TEXT NOT NULL,
	PRIMARY KEY ("Timeline_id", moments),
	FOREIGN KEY("Timeline_id") REFERENCES "Timeline" (id)
);
CREATE INDEX "ix_Timeline_moments_Timeline_id" ON "Timeline_moments" ("Timeline_id");
CREATE INDEX "ix_Timeline_moments_moments" ON "Timeline_moments" (moments);

CREATE TABLE "Flow" (
	unique_id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	requirement_url TEXT,
	metadata TEXT,
	"Architecture_id" INTEGER,
	controls_id INTEGER,
	PRIMARY KEY (unique_id),
	FOREIGN KEY("Architecture_id") REFERENCES "Architecture" (id),
	FOREIGN KEY(controls_id) REFERENCES "Control" (id)
);
CREATE INDEX "ix_Flow_unique_id" ON "Flow" (unique_id);

CREATE TABLE "RelationshipType" (
	id INTEGER NOT NULL,
	interacts_id INTEGER,
	connects_id INTEGER,
	deployed_in_id INTEGER,
	composed_of_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(interacts_id) REFERENCES "InteractsRelationship" (id),
	FOREIGN KEY(connects_id) REFERENCES "ConnectsRelationship" (id),
	FOREIGN KEY(deployed_in_id) REFERENCES "DeployedInRelationship" (id),
	FOREIGN KEY(composed_of_id) REFERENCES "ComposedOfRelationship" (id)
);
CREATE INDEX "ix_RelationshipType_id" ON "RelationshipType" (id);

CREATE TABLE "Architecture_adrs" (
	"Architecture_id" INTEGER,
	adrs TEXT,
	PRIMARY KEY ("Architecture_id", adrs),
	FOREIGN KEY("Architecture_id") REFERENCES "Architecture" (id)
);
CREATE INDEX "ix_Architecture_adrs_adrs" ON "Architecture_adrs" (adrs);
CREATE INDEX "ix_Architecture_adrs_Architecture_id" ON "Architecture_adrs" ("Architecture_id");

CREATE TABLE "NodeMoment_adrs" (
	"NodeMoment_unique_id" TEXT,
	adrs TEXT,
	PRIMARY KEY ("NodeMoment_unique_id", adrs),
	FOREIGN KEY("NodeMoment_unique_id") REFERENCES "NodeMoment" (unique_id)
);
CREATE INDEX "ix_NodeMoment_adrs_adrs" ON "NodeMoment_adrs" (adrs);
CREATE INDEX "ix_NodeMoment_adrs_NodeMoment_unique_id" ON "NodeMoment_adrs" ("NodeMoment_unique_id");

CREATE TABLE "Decision" (
	id INTEGER NOT NULL,
	description TEXT NOT NULL,
	"OptionList_id" INTEGER,
	"RelationshipType_id" INTEGER,
	controls_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("OptionList_id") REFERENCES "OptionList" (id),
	FOREIGN KEY("RelationshipType_id") REFERENCES "RelationshipType" (id),
	FOREIGN KEY(controls_id) REFERENCES "Control" (id)
);
CREATE INDEX "ix_Decision_id" ON "Decision" (id);

CREATE TABLE "Flow_transitions" (
	"Flow_unique_id" TEXT,
	transitions_id INTEGER NOT NULL,
	PRIMARY KEY ("Flow_unique_id", transitions_id),
	FOREIGN KEY("Flow_unique_id") REFERENCES "Flow" (unique_id),
	FOREIGN KEY(transitions_id) REFERENCES "Transition" (id)
);
CREATE INDEX "ix_Flow_transitions_transitions_id" ON "Flow_transitions" (transitions_id);
CREATE INDEX "ix_Flow_transitions_Flow_unique_id" ON "Flow_transitions" ("Flow_unique_id");

CREATE TABLE "Node" (
	unique_id TEXT NOT NULL,
	node_type VARCHAR(10) NOT NULL,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	details TEXT,
	metadata TEXT,
	"Architecture_id" INTEGER,
	"Decision_id" INTEGER,
	controls_id INTEGER,
	PRIMARY KEY (unique_id),
	FOREIGN KEY("Architecture_id") REFERENCES "Architecture" (id),
	FOREIGN KEY("Decision_id") REFERENCES "Decision" (id),
	FOREIGN KEY(controls_id) REFERENCES "Control" (id)
);
CREATE INDEX "ix_Node_unique_id" ON "Node" (unique_id);

CREATE TABLE "Relationship" (
	unique_id TEXT NOT NULL,
	description TEXT,
	protocol VARCHAR(9),
	metadata TEXT,
	"Architecture_id" INTEGER,
	"Decision_id" INTEGER,
	relationship_type_id INTEGER NOT NULL,
	controls_id INTEGER,
	PRIMARY KEY (unique_id),
	FOREIGN KEY("Architecture_id") REFERENCES "Architecture" (id),
	FOREIGN KEY("Decision_id") REFERENCES "Decision" (id),
	FOREIGN KEY(relationship_type_id) REFERENCES "RelationshipType" (id),
	FOREIGN KEY(controls_id) REFERENCES "Control" (id)
);
CREATE INDEX "ix_Relationship_unique_id" ON "Relationship" (unique_id);

CREATE TABLE "InterfaceDefinition" (
	unique_id TEXT NOT NULL,
	definition_url TEXT NOT NULL,
	config TEXT NOT NULL,
	"Node_unique_id" TEXT,
	"NodeInterface_id" INTEGER,
	"NodeMoment_unique_id" TEXT,
	PRIMARY KEY (unique_id),
	FOREIGN KEY("Node_unique_id") REFERENCES "Node" (unique_id),
	FOREIGN KEY("NodeInterface_id") REFERENCES "NodeInterface" (id),
	FOREIGN KEY("NodeMoment_unique_id") REFERENCES "NodeMoment" (unique_id)
);
CREATE INDEX "ix_InterfaceDefinition_unique_id" ON "InterfaceDefinition" (unique_id);

CREATE TABLE "InteractsRelationship_nodes" (
	"InteractsRelationship_id" INTEGER,
	nodes_unique_id TEXT NOT NULL,
	PRIMARY KEY ("InteractsRelationship_id", nodes_unique_id),
	FOREIGN KEY("InteractsRelationship_id") REFERENCES "InteractsRelationship" (id),
	FOREIGN KEY(nodes_unique_id) REFERENCES "Node" (unique_id)
);
CREATE INDEX "ix_InteractsRelationship_nodes_InteractsRelationship_id" ON "InteractsRelationship_nodes" ("InteractsRelationship_id");
CREATE INDEX "ix_InteractsRelationship_nodes_nodes_unique_id" ON "InteractsRelationship_nodes" (nodes_unique_id);

CREATE TABLE "DeployedInRelationship_nodes" (
	"DeployedInRelationship_id" INTEGER,
	nodes_unique_id TEXT NOT NULL,
	PRIMARY KEY ("DeployedInRelationship_id", nodes_unique_id),
	FOREIGN KEY("DeployedInRelationship_id") REFERENCES "DeployedInRelationship" (id),
	FOREIGN KEY(nodes_unique_id) REFERENCES "Node" (unique_id)
);
CREATE INDEX "ix_DeployedInRelationship_nodes_DeployedInRelationship_id" ON "DeployedInRelationship_nodes" ("DeployedInRelationship_id");
CREATE INDEX "ix_DeployedInRelationship_nodes_nodes_unique_id" ON "DeployedInRelationship_nodes" (nodes_unique_id);

CREATE TABLE "ComposedOfRelationship_nodes" (
	"ComposedOfRelationship_id" INTEGER,
	nodes_unique_id TEXT NOT NULL,
	PRIMARY KEY ("ComposedOfRelationship_id", nodes_unique_id),
	FOREIGN KEY("ComposedOfRelationship_id") REFERENCES "ComposedOfRelationship" (id),
	FOREIGN KEY(nodes_unique_id) REFERENCES "Node" (unique_id)
);
CREATE INDEX "ix_ComposedOfRelationship_nodes_nodes_unique_id" ON "ComposedOfRelationship_nodes" (nodes_unique_id);
CREATE INDEX "ix_ComposedOfRelationship_nodes_ComposedOfRelationship_id" ON "ComposedOfRelationship_nodes" ("ComposedOfRelationship_id");
