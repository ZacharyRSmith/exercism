import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * When instantiated with a given word,
 * then this instance can select anagrams from a list of candidates.
 */
public class Anagram {

  private final String matcher;

  private final ArrayList<String> matcherLtrs;

  public Anagram(String matcher) {
    this.matcher = matcher.toLowerCase();

    this.matcherLtrs = this.getSortedLtrs(this.matcher);
  }

  /**
   * Returns the subset of @param candidates that are anagrams of this instance.
   */
  public final ArrayList<String> match(List<String> candidates) {
    ArrayList<String> res = new ArrayList<String>();

    for (String candidate : candidates) {
      if (isAnagram(candidate)) {
        res.add(candidate);
      }
    }

    return res;
  }

  private final ArrayList<String> getSortedLtrs(String word) {
    ArrayList<String> ltrs = new ArrayList<String>(Arrays.asList(word.split("")));
    Collections.sort(ltrs);
    return ltrs;
  }

  private final boolean isAnagram(String pCandidate) {
    String candidate = pCandidate.toLowerCase();
    if (candidate.equals(this.matcher)) return false;

    ArrayList<String> candidateLtrs = getSortedLtrs(candidate);

    return candidateLtrs.equals(this.matcherLtrs);
  }
}
