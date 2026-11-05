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
  Domain-defined control requirement that controls can reference.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ControlRequirement  {

  private String controlId;
  private String name;
  private String description;


}