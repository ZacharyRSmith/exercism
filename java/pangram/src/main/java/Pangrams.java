import java.util.Locale;
import java.util.stream.Collectors;

public class Pangrams {
    private static final String ALPHABET = "abcdefghijklmnopqrstuvwxyz";

    public static boolean isPangram(String sentence) {
        // return ALPHABET.equals(
        return sentence.toLowerCase(Locale.ENGLISH).chars()
                .mapToObj(i -> String.valueOf((char)i))
                .filter(ALPHABET::contains)
                // .distinct()
                .sorted()
                .collect(Collectors.joining())
                .length() == 26;
    }
}

// import java.util.stream.Collectors;

// public class Pangrams {
//   private static final String ALPHABET = "abcdefghijklmnopqrstuvwxyz";

//   public static boolean isPangram(final String input) {
//     String inputClean = input.toLowerCase().replace("[^a-z]", "");
//     if (inputClean.length() < 26) return false;

//     return inputClean.chars()
//       .mapToObj(i -> String.valueOf((char)i))
//       .filter(ALPHABET::contains)
//       .distinct()
//       .collect(Collectors.joining())
//       .length() == 26;
//   }
// }
