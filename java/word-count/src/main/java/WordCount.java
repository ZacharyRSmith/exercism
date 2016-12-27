import java.util.HashMap;
import java.util.Map;

public class WordCount {
  public Map<String, Integer> Phrase(String input) {
    Map<String, Integer> res = new HashMap<String, Integer>();

    for (String word : input.toLowerCase().split("\\W+")) {
      incrementCount(res, word);
    }

    return res;
  }

  private void incrementCount(Map<String, Integer> map, String word) {
    if (!map.containsKey(word)) map.put(word, 0);

    int crnt = map.get(word);

    map.put(word, crnt + 1);
  }
}
