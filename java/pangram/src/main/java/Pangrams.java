import java.util.HashMap;

public class Pangrams {

  public static boolean isPangram(String input) {
    if (input.length() < 26) return false;
    String inputClean = input.toLowerCase().replaceAll("[^a-z]", "");
    // TODO use Set instead of HashMap
    HashMap<Character, Boolean> numChars = new HashMap<Character, Boolean>();

    for (int i = 0; i < inputClean.length(); i++) {
      char ltr = inputClean.charAt(i);
      if (numChars.containsKey(ltr)) continue;

      numChars.put(ltr, true);

      if (numChars.size() == 26) {
        return true;
      }
    }

    return false;
  }
}
