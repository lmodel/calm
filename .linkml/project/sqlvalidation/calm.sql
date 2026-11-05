-- ====================================================================
-- SQL Validation Queries
-- Generated from LinkML schema
-- LinkML v1.11.1
-- Generator: sqlvalidationgen.py v0.1.0
-- Dialect: sqlite
-- ====================================================================

SELECT 'Node' AS table_name, 'unique_id' AS column_name, 'required' AS constraint_type, unique_id AS record_id, NULL AS invalid_value 
FROM "Node" 
WHERE "Node".unique_id IS NULL

UNION ALL

SELECT 'Node' AS table_name, 'unique_id' AS column_name, 'identifier' AS constraint_type, unique_id AS record_id, unique_id AS invalid_value 
FROM "Node" 
WHERE "Node".unique_id IN (SELECT unique_id 
FROM "Node" GROUP BY unique_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'Node' AS table_name, 'node_type' AS column_name, 'required' AS constraint_type, unique_id AS record_id, NULL AS invalid_value 
FROM "Node" 
WHERE "Node".node_type IS NULL

UNION ALL

SELECT 'Node' AS table_name, 'node_type' AS column_name, 'enum' AS constraint_type, unique_id AS record_id, node_type AS invalid_value 
FROM "Node" 
WHERE "Node".node_type IS NOT NULL AND ("Node".node_type NOT IN ('actor', 'ecosystem', 'system', 'service', 'database', 'network', 'ldap', 'webclient', 'data_asset'))

UNION ALL

SELECT 'Node' AS table_name, 'name' AS column_name, 'required' AS constraint_type, unique_id AS record_id, NULL AS invalid_value 
FROM "Node" 
WHERE "Node".name IS NULL

UNION ALL

SELECT 'Node' AS table_name, 'description' AS column_name, 'required' AS constraint_type, unique_id AS record_id, NULL AS invalid_value 
FROM "Node" 
WHERE "Node".description IS NULL

UNION ALL

SELECT 'Relationship' AS table_name, 'unique_id' AS column_name, 'required' AS constraint_type, unique_id AS record_id, NULL AS invalid_value 
FROM "Relationship" 
WHERE "Relationship".unique_id IS NULL

UNION ALL

SELECT 'Relationship' AS table_name, 'unique_id' AS column_name, 'identifier' AS constraint_type, unique_id AS record_id, unique_id AS invalid_value 
FROM "Relationship" 
WHERE "Relationship".unique_id IN (SELECT unique_id 
FROM "Relationship" GROUP BY unique_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'Relationship' AS table_name, 'relationship_type' AS column_name, 'required' AS constraint_type, unique_id AS record_id, NULL AS invalid_value 
FROM "Relationship" 
WHERE "Relationship".relationship_type IS NULL

UNION ALL

SELECT 'Relationship' AS table_name, 'protocol' AS column_name, 'enum' AS constraint_type, unique_id AS record_id, protocol AS invalid_value 
FROM "Relationship" 
WHERE "Relationship".protocol IS NOT NULL AND ("Relationship".protocol NOT IN ('HTTP', 'HTTPS', 'FTP', 'SFTP', 'JDBC', 'WebSocket', 'SocketIO', 'LDAP', 'AMQP', 'TLS', 'mTLS', 'TCP'))

UNION ALL

SELECT 'InteractsRelationship' AS table_name, 'actor' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InteractsRelationship" 
WHERE "InteractsRelationship".actor IS NULL

UNION ALL

SELECT 'InteractsRelationship' AS table_name, 'nodes' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InteractsRelationship" 
WHERE "InteractsRelationship".nodes IS NULL

UNION ALL

SELECT 'ConnectsRelationship' AS table_name, 'source' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ConnectsRelationship" 
WHERE "ConnectsRelationship".source IS NULL

UNION ALL

SELECT 'ConnectsRelationship' AS table_name, 'destination' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ConnectsRelationship" 
WHERE "ConnectsRelationship".destination IS NULL

UNION ALL

SELECT 'DeployedInRelationship' AS table_name, 'container' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "DeployedInRelationship" 
WHERE "DeployedInRelationship".container IS NULL

UNION ALL

SELECT 'DeployedInRelationship' AS table_name, 'nodes' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "DeployedInRelationship" 
WHERE "DeployedInRelationship".nodes IS NULL

UNION ALL

SELECT 'ComposedOfRelationship' AS table_name, 'container' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ComposedOfRelationship" 
WHERE "ComposedOfRelationship".container IS NULL

UNION ALL

SELECT 'ComposedOfRelationship' AS table_name, 'nodes' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ComposedOfRelationship" 
WHERE "ComposedOfRelationship".nodes IS NULL

UNION ALL

SELECT 'Decision' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Decision" 
WHERE "Decision".description IS NULL

UNION ALL

SELECT 'Decision' AS table_name, 'nodes' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Decision" 
WHERE "Decision".nodes IS NULL

UNION ALL

SELECT 'Decision' AS table_name, 'relationships' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Decision" 
WHERE "Decision".relationships IS NULL

UNION ALL

SELECT 'ControlDetail' AS table_name, 'requirement_url' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ControlDetail" 
WHERE "ControlDetail".requirement_url IS NULL

UNION ALL

SELECT 'ControlRequirement' AS table_name, 'control_id' AS column_name, 'required' AS constraint_type, control_id AS record_id, NULL AS invalid_value 
FROM "ControlRequirement" 
WHERE "ControlRequirement".control_id IS NULL

UNION ALL

SELECT 'ControlRequirement' AS table_name, 'control_id' AS column_name, 'identifier' AS constraint_type, control_id AS record_id, control_id AS invalid_value 
FROM "ControlRequirement" 
WHERE "ControlRequirement".control_id IN (SELECT control_id 
FROM "ControlRequirement" GROUP BY control_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'ControlRequirement' AS table_name, 'name' AS column_name, 'required' AS constraint_type, control_id AS record_id, NULL AS invalid_value 
FROM "ControlRequirement" 
WHERE "ControlRequirement".name IS NULL

UNION ALL

SELECT 'ControlRequirement' AS table_name, 'description' AS column_name, 'required' AS constraint_type, control_id AS record_id, NULL AS invalid_value 
FROM "ControlRequirement" 
WHERE "ControlRequirement".description IS NULL

UNION ALL

SELECT 'Decorator' AS table_name, 'unique_id' AS column_name, 'required' AS constraint_type, unique_id AS record_id, NULL AS invalid_value 
FROM "Decorator" 
WHERE "Decorator".unique_id IS NULL

UNION ALL

SELECT 'Decorator' AS table_name, 'unique_id' AS column_name, 'identifier' AS constraint_type, unique_id AS record_id, unique_id AS invalid_value 
FROM "Decorator" 
WHERE "Decorator".unique_id IN (SELECT unique_id 
FROM "Decorator" GROUP BY unique_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'Decorator' AS table_name, 'type' AS column_name, 'required' AS constraint_type, unique_id AS record_id, NULL AS invalid_value 
FROM "Decorator" 
WHERE "Decorator".type IS NULL

UNION ALL

SELECT 'Decorator' AS table_name, 'target' AS column_name, 'required' AS constraint_type, unique_id AS record_id, NULL AS invalid_value 
FROM "Decorator" 
WHERE "Decorator".target IS NULL

UNION ALL

SELECT 'Decorator' AS table_name, 'applies_to' AS column_name, 'required' AS constraint_type, unique_id AS record_id, NULL AS invalid_value 
FROM "Decorator" 
WHERE "Decorator".applies_to IS NULL

UNION ALL

SELECT 'Decorator' AS table_name, 'data' AS column_name, 'required' AS constraint_type, unique_id AS record_id, NULL AS invalid_value 
FROM "Decorator" 
WHERE "Decorator".data IS NULL

UNION ALL

SELECT 'EvidenceDocument' AS table_name, 'evidence' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "EvidenceDocument" 
WHERE "EvidenceDocument".evidence IS NULL

UNION ALL

SELECT 'Transition' AS table_name, 'relationship_unique_id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Transition" 
WHERE "Transition".relationship_unique_id IS NULL

UNION ALL

SELECT 'Transition' AS table_name, 'sequence_number' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Transition" 
WHERE "Transition".sequence_number IS NULL

UNION ALL

SELECT 'Transition' AS table_name, 'sequence_number' AS column_name, 'range' AS constraint_type, id AS record_id, sequence_number AS invalid_value 
FROM "Transition" 
WHERE "Transition".sequence_number < 1

UNION ALL

SELECT 'Transition' AS table_name, 'description' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Transition" 
WHERE "Transition".description IS NULL

UNION ALL

SELECT 'Transition' AS table_name, 'direction' AS column_name, 'enum' AS constraint_type, id AS record_id, direction AS invalid_value 
FROM "Transition" 
WHERE "Transition".direction IS NOT NULL AND ("Transition".direction NOT IN ('source_to_destination', 'destination_to_source'))

UNION ALL

SELECT 'Flow' AS table_name, 'unique_id' AS column_name, 'required' AS constraint_type, unique_id AS record_id, NULL AS invalid_value 
FROM "Flow" 
WHERE "Flow".unique_id IS NULL

UNION ALL

SELECT 'Flow' AS table_name, 'unique_id' AS column_name, 'identifier' AS constraint_type, unique_id AS record_id, unique_id AS invalid_value 
FROM "Flow" 
WHERE "Flow".unique_id IN (SELECT unique_id 
FROM "Flow" GROUP BY unique_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'Flow' AS table_name, 'name' AS column_name, 'required' AS constraint_type, unique_id AS record_id, NULL AS invalid_value 
FROM "Flow" 
WHERE "Flow".name IS NULL

UNION ALL

SELECT 'Flow' AS table_name, 'description' AS column_name, 'required' AS constraint_type, unique_id AS record_id, NULL AS invalid_value 
FROM "Flow" 
WHERE "Flow".description IS NULL

UNION ALL

SELECT 'Flow' AS table_name, 'transitions' AS column_name, 'required' AS constraint_type, unique_id AS record_id, NULL AS invalid_value 
FROM "Flow" 
WHERE "Flow".transitions IS NULL

UNION ALL

SELECT 'InterfaceDefinition' AS table_name, 'unique_id' AS column_name, 'required' AS constraint_type, unique_id AS record_id, NULL AS invalid_value 
FROM "InterfaceDefinition" 
WHERE "InterfaceDefinition".unique_id IS NULL

UNION ALL

SELECT 'InterfaceDefinition' AS table_name, 'unique_id' AS column_name, 'identifier' AS constraint_type, unique_id AS record_id, unique_id AS invalid_value 
FROM "InterfaceDefinition" 
WHERE "InterfaceDefinition".unique_id IN (SELECT unique_id 
FROM "InterfaceDefinition" GROUP BY unique_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'InterfaceDefinition' AS table_name, 'definition_url' AS column_name, 'required' AS constraint_type, unique_id AS record_id, NULL AS invalid_value 
FROM "InterfaceDefinition" 
WHERE "InterfaceDefinition".definition_url IS NULL

UNION ALL

SELECT 'InterfaceDefinition' AS table_name, 'config' AS column_name, 'required' AS constraint_type, unique_id AS record_id, NULL AS invalid_value 
FROM "InterfaceDefinition" 
WHERE "InterfaceDefinition".config IS NULL

UNION ALL

SELECT 'InterfaceType' AS table_name, 'unique_id' AS column_name, 'required' AS constraint_type, unique_id AS record_id, NULL AS invalid_value 
FROM "InterfaceType" 
WHERE "InterfaceType".unique_id IS NULL

UNION ALL

SELECT 'InterfaceType' AS table_name, 'unique_id' AS column_name, 'identifier' AS constraint_type, unique_id AS record_id, unique_id AS invalid_value 
FROM "InterfaceType" 
WHERE "InterfaceType".unique_id IN (SELECT unique_id 
FROM "InterfaceType" GROUP BY unique_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'NodeInterface' AS table_name, 'node' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "NodeInterface" 
WHERE "NodeInterface".node IS NULL

UNION ALL

SELECT 'Timeline' AS table_name, 'moments' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "Timeline" 
WHERE "Timeline".moments IS NULL

UNION ALL

SELECT 'NodeMoment' AS table_name, 'unique_id' AS column_name, 'required' AS constraint_type, unique_id AS record_id, NULL AS invalid_value 
FROM "NodeMoment" 
WHERE "NodeMoment".unique_id IS NULL

UNION ALL

SELECT 'NodeMoment' AS table_name, 'unique_id' AS column_name, 'identifier' AS constraint_type, unique_id AS record_id, unique_id AS invalid_value 
FROM "NodeMoment" 
WHERE "NodeMoment".unique_id IN (SELECT unique_id 
FROM "NodeMoment" GROUP BY unique_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'NodeMoment' AS table_name, 'name' AS column_name, 'required' AS constraint_type, unique_id AS record_id, NULL AS invalid_value 
FROM "NodeMoment" 
WHERE "NodeMoment".name IS NULL

UNION ALL

SELECT 'NodeMoment' AS table_name, 'description' AS column_name, 'required' AS constraint_type, unique_id AS record_id, NULL AS invalid_value 
FROM "NodeMoment" 
WHERE "NodeMoment".description IS NULL

UNION ALL

SELECT 'NodeMoment' AS table_name, 'node_type' AS column_name, 'required' AS constraint_type, unique_id AS record_id, NULL AS invalid_value 
FROM "NodeMoment" 
WHERE "NodeMoment".node_type IS NULL

UNION ALL

SELECT 'NodeMoment' AS table_name, 'node_type' AS column_name, 'enum' AS constraint_type, unique_id AS record_id, node_type AS invalid_value 
FROM "NodeMoment" 
WHERE "NodeMoment".node_type IS NOT NULL AND ("NodeMoment".node_type NOT IN ('actor', 'ecosystem', 'system', 'service', 'database', 'network', 'ldap', 'webclient', 'data_asset'))

UNION ALL

SELECT 'NodeMoment' AS table_name, 'details' AS column_name, 'required' AS constraint_type, unique_id AS record_id, NULL AS invalid_value 
FROM "NodeMoment" 
WHERE "NodeMoment".details IS NULL

UNION ALL

SELECT 'TimeUnit' AS table_name, 'unit' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "TimeUnit" 
WHERE "TimeUnit".unit IS NULL

UNION ALL

SELECT 'TimeUnit' AS table_name, 'unit' AS column_name, 'enum' AS constraint_type, id AS record_id, unit AS invalid_value 
FROM "TimeUnit" 
WHERE "TimeUnit".unit IS NOT NULL AND ("TimeUnit".unit NOT IN ('nanoseconds', 'microseconds', 'milliseconds', 'seconds', 'minutes', 'hours', 'days', 'weeks', 'months', 'quarters', 'years'))

UNION ALL

SELECT 'TimeUnit' AS table_name, 'value' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "TimeUnit" 
WHERE "TimeUnit".value IS NULL

UNION ALL

SELECT 'TimeUnit' AS table_name, 'value' AS column_name, 'range' AS constraint_type, id AS record_id, value AS invalid_value 
FROM "TimeUnit" 
WHERE "TimeUnit".value < 0

UNION ALL

SELECT 'RateUnit' AS table_name, 'rate' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RateUnit" 
WHERE "RateUnit".rate IS NULL

UNION ALL

SELECT 'RateUnit' AS table_name, 'rate' AS column_name, 'range' AS constraint_type, id AS record_id, rate AS invalid_value 
FROM "RateUnit" 
WHERE "RateUnit".rate < 0

UNION ALL

SELECT 'RateUnit' AS table_name, 'per' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "RateUnit" 
WHERE "RateUnit".per IS NULL

UNION ALL

SELECT 'RateUnit' AS table_name, 'per' AS column_name, 'enum' AS constraint_type, id AS record_id, per AS invalid_value 
FROM "RateUnit" 
WHERE "RateUnit".per IS NOT NULL AND ("RateUnit".per NOT IN ('nanosecond', 'microsecond', 'millisecond', 'second', 'minute', 'hour', 'day', 'week', 'month', 'quarter', 'year'));

