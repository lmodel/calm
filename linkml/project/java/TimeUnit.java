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
  A quantity of time expressed as a numeric value and a unit.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TimeUnit  {

  private String unit;
  private float value;


}