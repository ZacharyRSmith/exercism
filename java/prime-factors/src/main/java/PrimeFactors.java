import java.util.*;

/**
 * Computes the prime factors of a given natural number.
 */
public class PrimeFactors {
  public static List<Long> getForNumber(long num) {
    List<Long> res = new ArrayList<Long>();
    long divisor = 2L;

    while (num > 1) {
      if (num % divisor == 0) {
        num /= divisor;
        res.add(divisor);
      } else {
        divisor += 1;
      }
    }

    return res;
  }
}
