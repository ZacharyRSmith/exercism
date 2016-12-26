import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.List;

public class Anagram {

  private final String matcher;

  private final HashMap<Character, Integer> charCounts;

  public Anagram(String matcher) {
    this.matcher = matcher.toLowerCase();

    this.charCounts = getCharCounts(this.matcher);
  }

  public final ArrayList<String> match(List<String> candidates) {
    ArrayList<String> res = new ArrayList<String>();

    for (String candidate : candidates) {
      if (isCandidate(candidate)) {
        res.add(candidate);
      }
    }

    return res;
  }

  private final boolean isCandidate(String candidate) {
    candidate = candidate.toLowerCase();
    if (candidate.equals(this.matcher)) return false;
    HashMap<Character, Integer> candidateCharCounts = getCharCounts(candidate);
    if (candidateCharCounts.size() != this.charCounts.size()) return false;

    for (Map.Entry<Character, Integer> e : candidateCharCounts.entrySet()) {
      if (!isCountSame(e)) return false;
    }

    return true;
  }

  private final boolean isCountSame(final Map.Entry<Character, Integer> e) {
    if (!this.charCounts.containsKey(e.getKey())) return false;
    int matcherCounts = this.charCounts.get(e.getKey());
    int candidateCounts = e.getValue();

    return matcherCounts == candidateCounts;
  }

  private final HashMap<Character, Integer> getCharCounts(final String word) {
    HashMap<Character, Integer> res = new HashMap<Character, Integer>();

    for (char ch : word.toCharArray()) {
      if (!res.containsKey(ch)) res.put(ch, 0);
      res.put(ch, res.get(ch) + 1);
    }

    return res;
  }
}
