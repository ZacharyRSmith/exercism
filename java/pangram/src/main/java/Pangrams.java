public class Pangrams {

  public static boolean isPangram(final String input) {
    String inputClean = input.toLowerCase().replace("[^a-z]", "");
    if (inputClean.length() < 26) return false;

    for (char ch = 'a'; ch <= 'z'; ch++) {
      if (inputClean.indexOf(ch) < 0) return false;
    }

    return true;
  }
}
