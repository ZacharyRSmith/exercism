public class PhoneNumber {

  private static String number;

  PhoneNumber(String input) {
    String inputClean = input.replaceAll("[^\\d]", "");
    if (inputClean.length() == 10) {
      this.number = inputClean;
    } else {
      if (inputClean.substring(0, 1).equals("1") && inputClean.length() == 11) {
        this.number = inputClean.substring(1);
      } else {
        this.number = "0000000000";
      }
    }
  }

  public final String getAreaCode() {
    return this.number.substring(0, 3);
  }

  public final String getNumber() {
    return this.number;
  }

  public final String pretty() {
    String areaCode = this.getAreaCode();
    String num = this.number;
    return "(" + areaCode + ")" + " " + num.substring(3, 6) + "-" + num.substring(6);
  }
}
