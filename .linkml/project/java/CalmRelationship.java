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
  A link between nodes, of one of CALM's kinds, or a choice between options.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CalmRelationship  {

  private String uniqueId;
  private String description;
  private CalmRelationshipType relationshipType;
  private String protocol;
  private Object metadata;
  private CalmControls controls;


}