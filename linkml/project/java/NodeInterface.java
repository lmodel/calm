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
  Reference to one or more interfaces exposed by a node.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NodeInterface  {

  private String node;
  private List<InterfaceDefinition> interfaces;


}