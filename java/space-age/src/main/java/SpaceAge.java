import java.util.HashMap;
import java.util.Map;

/**
 * Calculates how old someone is in terms of a given planet's solar years.
 */
public class SpaceAge {
  private static Map<String, Double> EARTH_YEARS_PER_ORBIT = new HashMap<String, Double>();

  static {
    EARTH_YEARS_PER_ORBIT.put("Mercury", 0.2408467);
    EARTH_YEARS_PER_ORBIT.put("Venus", 0.61519726);
    EARTH_YEARS_PER_ORBIT.put("Mars", 1.8808158);
    EARTH_YEARS_PER_ORBIT.put("Jupiter", 11.862615);
    EARTH_YEARS_PER_ORBIT.put("Saturn", 29.447498);
    EARTH_YEARS_PER_ORBIT.put("Uranus", 84.016846);
    EARTH_YEARS_PER_ORBIT.put("Neptune", 164.79132);
  }

  private long seconds;

  SpaceAge(long seconds) {
    this.seconds = seconds;
  }

  /**
   * @return The seconds used to construct this instance.
   */
  public final long getSeconds() {
    return this.seconds;
  }

  /**
   * @return Age in Earth years.
   */
  public final double onEarth() {
    return convertSecondsToDays(this.seconds) / 365.25;
  }

  /**
   * @return Age in Mercury years.
   */
  public final double onMercury() {
    return this.onEarth() / EARTH_YEARS_PER_ORBIT.get("Mercury");
  }

  /**
   * @return Age in Venus years.
   */
  public final double onVenus() {
    return this.onEarth() / EARTH_YEARS_PER_ORBIT.get("Venus");
  }

  /**
   * @return Age in Mars years.
   */
  public final double onMars() {
    return this.onEarth() / EARTH_YEARS_PER_ORBIT.get("Mars");
  }

  /**
   * @return Age in Jupiter years.
   */
  public final double onJupiter() {
    return this.onEarth() / EARTH_YEARS_PER_ORBIT.get("Jupiter");
  }

  /**
   * @return Age in Saturn years.
   */
  public final double onSaturn() {
    return this.onEarth() / EARTH_YEARS_PER_ORBIT.get("Saturn");
  }

  /**
   * @return Age in Uranus years.
   */
  public final double onUranus() {
    return this.onEarth() / EARTH_YEARS_PER_ORBIT.get("Uranus");
  }

  /**
   * @return Age in Neptune years.
   */
  public final double onNeptune() {
    return this.onEarth() / EARTH_YEARS_PER_ORBIT.get("Neptune");
  }

  private final double convertSecondsToDays(long seconds) {
    // seconds / (seconds/min) / (min/hr) / (hr/day)
    return this.seconds / 60 / 60 / 24;
  }
}
