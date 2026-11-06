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
  A unit representing a rate (e.g., operations per second).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CalmRateUnit  {

  private BigDecimal rate;
  private String per;


}