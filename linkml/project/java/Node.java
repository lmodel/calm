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
  A logical or physical element of an architecture (system, service, actor, ...).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Node  {

  private String uniqueId;
  private String nodeType;
  private String name;
  private String description;
  private String details;
  private List<InterfaceDefinition> interfaces;
  private Control controls;
  private String metadata;


}