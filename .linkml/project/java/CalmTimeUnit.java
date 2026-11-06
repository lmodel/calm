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
  A unit of time with a value and a unit type.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CalmTimeUnit  {

  private String unitOfTime;
  private BigDecimal value;


}