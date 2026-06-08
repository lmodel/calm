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
  A ``connects`` relationship between two node interfaces.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ConnectsRelationship  {

  private NodeInterface source;
  private NodeInterface destination;


}