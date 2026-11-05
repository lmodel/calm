# Chandralanka Vendor Fixtures

Test data derived from the CALM examples repository - real-world "in-the-wild" vendor
data representing a company's architecture-as-code practice.

## Source

`https://github.com/chandralanka/calm-examples`

The source data uses CALM 1.2 JSON Schema format with company-specific extensions
(custom `costCenter`, `owner`, `dataClassification`, `encrypted` fields defined by
company standards in `standards/`).

## Fixture Strategy

### valid/

| File | Source element | What it exercises |
|------|---------------|-------------------|
| `Architecture-ecommerce-platform.yaml` | Full architecture | 10 nodes (actor, api-gateway, service, database, system), 9 relationships (interacts, connects, composed-of), interfaces |
| `Node-actor.yaml` | Customer actor | Minimal node (no interfaces) |
| `Node-api-gateway.yaml` | API Gateway | Custom node-type string, multiple interfaces |
| `Node-database.yaml` | Payment Database | JDBC interface |
| `Node-service-with-events.yaml` | Order Service | REST + health-check + event-stream interfaces |
| `Node-system.yaml` | E-Commerce Platform | System boundary (no interfaces) |
| `Relationship-interacts.yaml` | Customer ->  Gateway | Actor interaction |
| `Relationship-connects-https.yaml` | Gateway ->  Service | HTTPS connection with interfaces |
| `Relationship-connects-jdbc.yaml` | Service ->  Database | JDBC connection with interfaces |
| `Relationship-composed-of.yaml` | Platform composition | System composed of 7 child nodes |

### invalid/

| File | Violation |
|------|-----------|
| `Node-missing-description.yaml` | `description` required but omitted |
| `Node-missing-unique-id.yaml` | `unique_id` identifier required but omitted |
| `Relationship-missing-type.yaml` | `relationship_type` required but omitted |

## Adaptation Notes

1. **Slot naming**: JSON kebab-case (`unique-id`, `node-type`, `relationship-type`, `composed-of`) converted to LinkML snake_case (`unique_id`, `node_type`, `relationship_type`, `composed_of`).

2. **Company extensions omitted**: `costCenter`, `owner`, `environment`, `dataClassification`, `encrypted` are company-standard fields not in the CALM
   LinkML schema - excluded from fixtures.

3. **Metadata flattened**: Vendor `metadata` arrays (with `owner`, `repository`, etc.) are not mapped because the LinkML `Metadata` type is an opaque JSON object; these fixtures test the structural schema, not extension data.

4. **Interface mapping**: Vendor `url`/`protocol`/`type` fields packed into `definition_url` + `config` JSON string to match the LinkML `InterfaceDefinition` class requirements.

