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
  Modular interface definition referencing an external schema.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InterfaceDefinition  {

  private String uniqueId;
  private String definitionUrl;
  private String config;


}