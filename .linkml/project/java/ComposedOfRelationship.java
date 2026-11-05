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
  A ``composed-of`` containment relationship.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ComposedOfRelationship  {

  private String container;
  private List<Node> nodes;


}