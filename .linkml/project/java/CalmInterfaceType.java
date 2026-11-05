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
  An interface given by its own keys, such as a host and port, rather than by an external schema.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CalmInterfaceType  {

  private String uniqueId;


}