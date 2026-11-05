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
  A relationship in which nodes are deployed in a container node.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CalmDeployedInType  {

  private String container;
  private List<String> nodes;


}