public class Bob {

  private static final String responseToExcitement = "Whoa, chill out!";

  private static final String responseToQuestion = "Sure.";

  private static final String petulantResponse = "Fine. Be that way!";

  private static final String desultoryResponse = "Whatever.";

  public final String hey(String goesInEar) {
    if (hasExcitement(goesInEar)) return responseToExcitement;
    if (isQuestion(goesInEar)) return responseToQuestion;
    if (isSilent(goesInEar)) return petulantResponse;

    return desultoryResponse;
  }

  private final boolean hasExcitement(String goesInEar) {
    return goesInEar.matches(".*[A-Z].*") && goesInEar.equals(goesInEar.toUpperCase());
  }

  private final boolean isSilent(String goesInEar) {
    return goesInEar.replaceAll("\\s+", "").length() == 0;
  }

  private final boolean isQuestion(String goesInEar) {
    return goesInEar.endsWith("?");
  }
}
