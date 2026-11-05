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
  An ``interacts`` relationship between an actor and one or more nodes.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InteractsRelationship  {

  private String actor;
  private List<Node> nodes;


}