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
  Top-level CALM evidence document linking control configurations to evidence artefacts.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EvidenceDocument  {

  private String evidence;


}