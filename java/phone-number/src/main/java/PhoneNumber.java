public class PhoneNumber {
  private String number;
  private final String WRONG_NUMBER = "0000000000";

  PhoneNumber(String input) {
    setNumber(input);
  }

  public final String getAreaCode() {
    return this.number.substring(0, 3);
  }

  public final String getNumber() {
    return this.number;
  }

  public final String pretty() {
    return String.format("(%s) %s-%s",
      this.getAreaCode(),
      this.number.substring(3, 6),
      this.number.substring(6));
  }

  private final void setNumber(String input) {
    String onlyDigits = input.replaceAll("\\D", "");
    if (isFullUSNumber(onlyDigits)) {
      this.number = onlyDigits.substring(1);
      return;
    }
    if (onlyDigits.length() != 10) {
      this.number = WRONG_NUMBER;
      return;
    }

    this.number = onlyDigits;
  }

  private static final boolean isFullUSNumber(String onlyDigits) {
    return onlyDigits.length() == 11 && onlyDigits.substring(0, 1).equals("1");
  }
}
