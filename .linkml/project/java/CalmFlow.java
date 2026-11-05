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
  A business flow, as an ordered list of transitions across the architecture's relationships.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CalmFlow  {

  private String uniqueId;
  private String name;
  private String description;
  private String requirementUrl;
  private List<CalmTransition> transitions;
  private CalmControls controls;
  private Object metadata;


}