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
  CALM timeline document capturing architecture moments over time.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Timeline  {

  private String currentMoment;
  private List<String> moments;
  private String metadata;


}