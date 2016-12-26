import java.util.concurrent.ThreadLocalRandom;

/**
 * Manages robot factory settings.
 */
public class Robot {

  static String name;

  Robot() {
    this.name = genName();
  }

  public final String getName() {
    return this.name;
  }

  public final void reset() {
    this.name = genName();
  }

  // lazy impl
  private static final String genName() {
    int randomNum = ThreadLocalRandom.current().nextInt(100, 999);
    return "AA" + randomNum;
  }
}
