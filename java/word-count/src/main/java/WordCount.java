import java.util.HashMap;
import java.util.Map;

public class WordCount {
  public Map<String, Integer> Phrase(String input) {
    Map<String, Integer> res = new HashMap<String, Integer>();

    String[] ary = input.toLowerCase().split("\\W+");

    for (String word : ary) {
      if (!res.containsKey(word)) res.put(word, 0);
      int crnt = res.get(word);

      res.put(word, crnt + 1);
    }

    return res;
  }
}
