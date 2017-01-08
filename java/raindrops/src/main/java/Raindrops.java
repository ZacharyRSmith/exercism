public class Raindrops {
  public static String convert(int num) {
    StringBuilder builder = new StringBuilder();

    if (num % 3 == 0) {
      builder.append("Pling");
    }
    if (num % 5 == 0) {
      builder.append("Plang");
    }
    if (num % 7 == 0) {
      builder.append("Plong");
    }
    String res = builder.toString();

    if (res.length() == 0) return Integer.toString(num);
    return res;
  }
}
