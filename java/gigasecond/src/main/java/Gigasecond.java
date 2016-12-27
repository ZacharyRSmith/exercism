import java.time.LocalDate;
import java.time.LocalDateTime;

/**
 * Calculates the moment when someone has lived for a gigasecond (10^9 seconds).
 */
public class Gigasecond {
  static LocalDateTime date;
  static long GIGASECOND = (long)Math.pow(10, 9);

  Gigasecond(LocalDate birthdate) {
    this.date = birthdate.atTime(0, 0).plusSeconds(GIGASECOND);
  }

  Gigasecond(LocalDateTime birthdate) {
    this.date = birthdate.plusSeconds(GIGASECOND);
  }

  public final LocalDateTime getDate() {
    return this.date;
  }
}
