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
  A component of the architecture, such as a system, service, database or actor, with its interfaces and controls.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CalmNode  {

  private String uniqueId;
  private String nodeType;
  private String name;
  private String description;
  private CalmNodeDetails details;
  private List<String> interfaces;
  private CalmControls controls;
  private Object metadata;


}