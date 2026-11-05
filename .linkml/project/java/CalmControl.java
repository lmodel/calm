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
  One control in a controls map, with the requirements that define it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CalmControl  {

  private String description;
  private List<CalmControlDetail> requirements;


}