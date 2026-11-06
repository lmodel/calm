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
  An evidence document, which holds one piece of evidence for a control.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CalmEvidenceDocument  {

  private CalmEvidence evidence;


}