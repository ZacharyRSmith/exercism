public class HelloWorld {
    public static String hello(String name) {
      if (name == null || name == "") return "Hello, World!";
      return String.format("Hello, %s!", name);
    }
}
