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
  An architecture moment - a point-in-time snapshot of the architecture.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NodeMoment extends Node {

  private LocalDate validFrom;
  private List<String> adrs;


}