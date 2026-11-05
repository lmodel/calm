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
  One step of a flow, across one relationship of the architecture.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CalmTransition  {

  private String relationshipUniqueId;
  private int sequenceNumber;
  private String description;
  private String direction;


}