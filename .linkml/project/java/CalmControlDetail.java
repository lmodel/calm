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
  A control requirement this control applies, with its configuration given by address or inline, but not both.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CalmControlDetail  {

  private String requirementUrl;
  private String configUrl;
  private CalmControlConfig config;


}