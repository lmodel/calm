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
  One end of a connection, naming a node and, optionally, which of its interfaces.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CalmNodeInterface  {

  private String node;
  private List<String> interfaces;


}