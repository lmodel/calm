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
  A control requirement: what a control must achieve, which a control detail's requirement-url points to.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CalmControlRequirement  {

  private String controlId;
  private String name;
  private String description;


}