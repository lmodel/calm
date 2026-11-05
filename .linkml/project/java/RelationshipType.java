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
  Tagged-union container for the variant body of a relationship. Exactly one of ``interacts``, ``connects``, ``deployed_in``, ``composed_of``, ``options`` is populated; see ``RelationshipKind`` for the discriminator values.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RelationshipType  {

  private InteractsRelationship interacts;
  private ConnectsRelationship connects;
  private DeployedInRelationship deployedIn;
  private ComposedOfRelationship composedOf;
  private List<Decision> options;


}