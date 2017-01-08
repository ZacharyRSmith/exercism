import java.util.*;
import java.util.function.Predicate;
import java.util.stream.Collectors;

/**
 * Replicates the `keep` and `discard` operations on collections.
 */
public class Strain {
  public static <T> List<T> discard(List<T> input, Predicate<T> op) {
    return input.stream()
      .filter(op.negate())
      .collect(Collectors.toList());

    // List<T> res = new ArrayList<T>();

    // for (T num : input) {
    //   if (op.negate().test(num)) res.add(num);
    // }

    // return res;
  }

  public static <T> List<T> keep(List<T> input, Predicate<T> op) {
    return input.stream()
      .filter(op)
      .collect(Collectors.toList());

    // List<T> res = new ArrayList<T>();

    // for (T num : input) {
    //   if (op.test(num)) res.add(num);
    // }

    // return res;
  }
}
