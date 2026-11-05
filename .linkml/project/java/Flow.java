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
  Business flow mapped onto architecture relationships.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Flow  {

  private String uniqueId;
  private String name;
  private String description;
  private String requirementUrl;
  private List<Transition> transitions;
  private Control controls;
  private String metadata;


}