import java.util.*;

/**
 * An implementation of the atbash cipher.
 *
 * The atbash cipher is an ancient encryption system created in the Middle East.
 * The Atbash cipher is a simple substitution cipher that relies on
 * transposing all the letters in the alphabet such that the resulting
 * alphabet is backwards. The first letter is replaced with the last
 * letter, the second with the second-last, and so on.
 */
public class Atbash {
  public static String decode(String ciphertext) {
    StringBuilder res = new StringBuilder();

    for (char ch : ciphertext.toCharArray()) {
      if (ch == ' ') continue;

      if (Character.isDigit(ch)) {
        res.append(ch);
      } else {
        res.append(decodeChar(ch));
      }
    }

    return res.toString();
  }

  public static String encode(String plaintext) {
    StringBuilder res = new StringBuilder();

    int crntSegmentLength = 0;
    for (char ch : plaintext.toLowerCase().toCharArray()) {
      if (ch == ' ' || !Character.isDigit(ch) && !Character.isAlphabetic(ch)) continue;
      if (crntSegmentLength == 5) {
        res.append(' ');
        crntSegmentLength = 0;
      }

      if (Character.isDigit(ch)) {
        res.append(ch);
      } else {
        res.append(encodeChar(ch));
      }

      crntSegmentLength += 1;
    }

    return res.toString();
  }

  private static char decodeChar(final char ch) {
    return (char) ('a' - (ch - 'z'));
  }

  private static char encodeChar(final char ch) {
    return (char) ('z' - (ch - 'a'));
  }
}
