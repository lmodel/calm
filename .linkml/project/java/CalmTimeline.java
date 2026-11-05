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
  A timeline document, listing the moments of an architecture and naming the current one.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CalmTimeline  {

  private String currentMoment;
  private List<CalmNodeMoment> moments;
  private Object metadata;


}