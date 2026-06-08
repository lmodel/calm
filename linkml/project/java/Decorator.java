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
  Cross-cutting annotation attached to nodes, relationships, or flows.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Decorator  {

  private String uniqueId;
  private String type;
  private List<String> target;
  private List<String> appliesTo;
  private String data;


}