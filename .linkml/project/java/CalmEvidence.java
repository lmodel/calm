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
  Evidence that a control's configuration is met, by the paths where it is kept.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CalmEvidence  {

  private String uniqueId;
  private List<String> evidencePaths;
  private String controlConfigUrl;


}