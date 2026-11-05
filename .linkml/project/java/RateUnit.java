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
  A rate (count per time unit), e.g. operations per second.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RateUnit  {

  private float rate;
  private String per;


}