import java.util.*;
import java.util.stream.Collectors;

/**
 * Converts a phrase to its acronym.
 */
public class Acronym {

  public static String generate(String phrase) {
    return Arrays.stream(phrase.split("\\W"))
      .map(word -> getInitials(word))
      .collect(Collectors.joining())
      .toUpperCase();
  }

  private static String getInitials(String word) {
    if (word.toLowerCase().equals(word)) {
      return word.isEmpty()
        ? ""
        : word.substring(0, 1);
    }

    return Arrays.stream(word.split("[^A-Z]"))
      .filter(fragment -> !fragment.isEmpty())
      .map(fragment -> fragment.substring(0, 1))
      .collect(Collectors.joining());
  }
}
