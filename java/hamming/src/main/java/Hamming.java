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

    int res = 0;

    for (int i = 0; i < a.length(); i++) {
      if (a.charAt(i) != b.charAt(i)) res++;
    }

    return res;
  }
}
