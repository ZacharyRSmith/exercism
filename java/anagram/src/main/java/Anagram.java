import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.List;

public class Anagram {

  private final String matcher;

  private final HashMap<Character, Integer> charCounts = new HashMap<Character, Integer>();

  public Anagram(String matcher) {
    this.matcher = matcher.toLowerCase();

    for (char ch : this.matcher.toCharArray()) {
      if (!charCounts.containsKey(ch)) charCounts.put(ch, 0);
      int crntCount = charCounts.get(ch);
      charCounts.put(ch, crntCount + 1);
    }
  }

  public final ArrayList<String> match(List<String> candidates) {
    ArrayList<String> res = new ArrayList<String>();

    for (String pCandidate : candidates) {
      String candidate = pCandidate.toLowerCase();
      if (candidate.equals(this.matcher)) continue;
      HashMap<Character, Integer> candidateCharCounts = new HashMap<Character, Integer>();

      for (char ch : candidate.toCharArray()) {
        if (!candidateCharCounts.containsKey(ch)) candidateCharCounts.put(ch, 0);
        int crntCount = candidateCharCounts.get(ch);
        candidateCharCounts.put(ch, crntCount + 1);
      }

      if (candidateCharCounts.size() != this.charCounts.size()) continue;

      res.add(pCandidate);

      for (Map.Entry<Character, Integer> e : candidateCharCounts.entrySet()) {
        if (!this.charCounts.containsKey(e.getKey())) {
          res.remove(pCandidate);
          break;
        }
        int matcherCounts = this.charCounts.get(e.getKey());
        int candidateCounts = e.getValue();
        if (matcherCounts != candidateCounts) {
          res.remove(pCandidate);
          break;
        }
      }
    }

    return res;
  }
}
