/**
 * Converts arabic numerals to Roman numerals.
 */
public class RomanNumeral {
  private String romanNumeral;

  RomanNumeral(final int arabicNumeral) {
    this.romanNumeral = genRomanNumeral(arabicNumeral);
  }

  public String getRomanNumeral() {
    return this.romanNumeral;
  }

  private static String genRomanNumeral(int num) {
    final StringBuilder res = new StringBuilder();
    // Init at the 1's place.
    // Note that `place = 2` will be 10's place, `place = 3` will be 100's place, etc.
    int place = 1;

    while (num >= 1) {
      res.append(getPlace(place, num % 10).reverse());
      place += 1;
      num /= 10;
    }

    return res.reverse().toString();
  }

  /**
   * Get the Roman numeral value of the current digits place.
   *
   * Eg, given the arabic numeral `34`, we would call `getPlace()` twice:
   * once like `getPlace(1, 4)` for the `4` at the "1's place", and
   * once like `getPlace(2, 3)` for the `3` at the "10's place".
   * @param place: The "digits place", eg "1's place", "10's place", etc.
   * @param num: The int at @param place's "digits place".
   */
  private static StringBuilder getPlace(final int place, final int num) {
    StringBuilder res = new StringBuilder();
    if (num == 0) return res;
    String one = "";
    String five = "";
    String ten = "";

    // Assign the Roman values for this digits place.
    switch (place) {
      case 1:
        one = "I";
        five = "V";
        ten = "X";
        break;
      case 2:
        one = "X";
        five = "L";
        ten = "C";
        break;
      case 3:
        one = "C";
        five = "D";
        ten = "M";
        break;
      case 4:
        one = "M";
        break;
    }

    // Return the Roman numerals that equal the int at this digits place.
    //
    // Eg, given `getPlace(1, 4)`,
    // then case 4: return "IV".
    //
    // Given `getPlace(2, 4)`,
    // then case 4: return "XL".
    switch (num) {
      case 9:
        return res.append(one + ten);
      case 8:
        return res.append(five + one + one + one);
      case 7:
        return res.append(five + one + one);
      case 6:
        return res.append(five + one);
      case 5:
        return res.append(five);
      case 4:
        return res.append(one + five);
      case 3:
        return res.append(one + one + one);
      case 2:
        return res.append(one + one);
      case 1:
        return res.append(one);
      default:
        return res;
    }
  }
}
