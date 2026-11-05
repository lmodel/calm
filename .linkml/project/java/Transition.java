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
  A single step in a flow, anchored on a relationship.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Transition  {

  private String relationshipUniqueId;
  private int sequenceNumber;
  private String description;
  private String direction;


}