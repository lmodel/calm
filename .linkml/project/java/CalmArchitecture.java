package example;

/* metamodel_version: 1.12.0 */
/* version: 1.3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A CALM architecture document: the nodes of a system, the relationships between them, its business flows, and the controls that apply to it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CalmArchitecture  {

  private List<CalmNode> nodes;
  private List<CalmRelationship> relationships;
  private Object metadata;
  private CalmControls controls;
  private List<CalmFlow> flows;
  private List<String> adrs;


}