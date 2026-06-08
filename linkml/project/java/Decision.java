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
  A candidate decision within an ``options`` relationship.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Decision  {

  private String description;
  private List<Node> nodes;
  private List<Relationship> relationships;
  private Control controls;


}