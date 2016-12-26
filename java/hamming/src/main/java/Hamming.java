import java.util.stream.IntStream;

/**
 * Calculates the Hamming difference between two DNA strands.
 */
public class Hamming {
  /**
   * @param a: A strand to compare to @param b.
   * @param b: A strand to compare to @param a.
   * @return: The Hamming difference between @param a and @param b.
   */
  public static int compute(String a, String b) {
    if (a.length() != b.length()) {
      throw new IllegalArgumentException("Strands must be of equal length.");
    }

    return IntStream.range(0, a.length())
      .map(i ->
        a.charAt(i) == b.charAt(i)
          ? 0
          : 1)
      .sum();
  }
}
