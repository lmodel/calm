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
  One option of a choice, naming the nodes, relationships and controls it would add.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CalmDecision  {

  private String description;
  private List<String> nodes;
  private List<String> relationships;
  private List<String> controls;


}