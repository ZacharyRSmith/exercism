import java.util.HashMap;
import java.util.Map;

public class WordCount {
  public Map<String, Integer> Phrase(String input) {
    Map<String, Integer> res = new HashMap<String, Integer>();

    res.put(input, 1);

    return res;
  }
}
