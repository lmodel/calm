package None;

/* metamodel_version: 1.11.0 */
/* version: 1.2 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A typed link between architecture elements.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Relationship  {

  private String uniqueId;
  private String description;
  private RelationshipType relationshipType;
  private String protocol;
  private String metadata;
  private Control controls;


}