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
  A single control requirement and its inline / referenced configuration.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ControlDetail  {

  private String requirementUrl;
  private String configUrl;
  private String config;


}