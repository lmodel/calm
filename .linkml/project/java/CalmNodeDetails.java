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
  References from a node to a more detailed architecture and to the pattern it must follow.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CalmNodeDetails  {

  private String detailedArchitecture;
  private String requiredPattern;


}