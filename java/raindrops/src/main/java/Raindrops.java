public class Raindrops {
  public static String convert(int num) {
    StringBuilder res = new StringBuilder();

    if (num % 3 == 0) {
      res.append("Pling");
    }
    if (num % 5 == 0) {
      res.append("Plang");
    }
    if (num % 7 == 0) {
      res.append("Plong");
    }
    if (res.length() == 0) {
      res.append(num);
    }

    return res.toString();
  }
}
