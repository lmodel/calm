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
  A modular interface definition referencing an external schema
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CalmInterfaceDefinition  {

  private String uniqueId;
  private String definitionUrl;
  private CalmInterfaceConfig config;


}