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
  Top-level CALM architecture document.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Architecture  {

  private List<Node> nodes;
  private List<Relationship> relationships;
  private String metadata;
  private Control controls;
  private List<Flow> flows;
  private List<String> adrs;


}