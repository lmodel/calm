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
  A moment of a timeline: a node of type moment, with no interfaces, whose details point to the architecture of that moment.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CalmNodeMoment extends CalmNode {

  private LocalDate validFrom;
  private List<String> adrs;


}