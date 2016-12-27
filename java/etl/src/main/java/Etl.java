import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Etl {
  public Map<String, Integer> transform(Map<Integer, List<String>> old) {
    Map<String, Integer> newFormat = new HashMap<>();

    old.forEach((score, letters) -> {
      setInNew(score, letters, newFormat);
    });

    return newFormat;
  }

  private void setInNew(Integer score, List<String> letters, Map<String, Integer> newMap) {
    letters.stream().forEach(letter -> {
      newMap.put(letter.toLowerCase(), score);
    });
  }
}
