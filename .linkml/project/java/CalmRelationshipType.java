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
  The kind of a relationship, given by exactly one of its keys: interacts, connects, deployed-in, composed-of or options.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CalmRelationshipType  {

  private CalmInteractsType interacts;
  private CalmConnectsType connects;
  private CalmDeployedInType deployedIn;
  private CalmComposedOfType composedOf;
  private List<CalmDecision> options;


}