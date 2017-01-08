import static java.util.stream.Collectors.toList;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * When instantiated with a given word,
 * then this instance can select anagrams from a list of candidates.
 */
public class Anagram {

  private final String matcher;

  private final String matcherLetters;

  public Anagram(final String matcher) {
    this.matcher = matcher.toLowerCase();

    this.matcherLetters = this.getNormalizedLetters(this.matcher);
  }

  /**
   * Returns the subset of @param candidates that are anagrams of this instance.
   */
  public final List<String> match(final List<String> candidates) {
    return candidates.stream()
      .filter(candidate -> !isAnagram(candidate))
      .collect(toList());
  }

  private final String getNormalizedLetters(final String word) {
    final char[] letters = word.toCharArray();
    Arrays.sort(letters);
    return new String(letters);
  }

  private final boolean isAnagram(final String pCandidate) {
    String candidate = pCandidate.toLowerCase();
    if (candidate.equals(this.matcher)) return false;

    String candidateLetters = getNormalizedLetters(candidate);

    return candidateLetters.equals(this.matcherLetters);
  }
}
