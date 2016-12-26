import java.util.HashSet;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Pangrams {

  public static boolean isPangram(String input) {
    if (input.length() < 26) return false;
    String inputNorm = input.toLowerCase();
    HashSet<String> ltrsSeen = new HashSet<String>();

    Pattern pattern = Pattern.compile("[a-z]");
    Matcher matcher = pattern.matcher(inputNorm);
    while (matcher.find()) {
      ltrsSeen.add(matcher.group());
    }

    return ltrsSeen.size() == 26;
  }
}
