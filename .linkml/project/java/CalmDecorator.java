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
  Supplementary information about elements of one or more architectures, kept apart from the architectures themselves.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CalmDecorator  {

  private String decoratorSchema;
  private String uniqueId;
  private String decoratorType;
  private List<String> targetType;
  private List<String> targetArchitectures;
  private List<String> appliesTo;
  private CalmDecoratorData data;


}