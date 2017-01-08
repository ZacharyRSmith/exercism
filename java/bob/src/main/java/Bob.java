public class Bob {

  private static final String insouciantResponse = "Whoa, chill out!";

  private static final String lackadaisicalAnswer = "Sure.";

  private static final String petulantResponse = "Fine. Be that way!";

  private static final String desultoryResponse = "Whatever.";

  public final String hey(String goesInEar) {
    if (hasExcitement(goesInEar)) return insouciantResponse;
    if (isQuestion(goesInEar)) return lackadaisicalAnswer;
    if (isSilent(goesInEar)) return petulantResponse;

    return desultoryResponse;
  }

  private final boolean hasExcitement(String goesInEar) {
    return goesInEar.chars().anyMatch(Character::isLetter)
      && goesInEar.equals(goesInEar.toUpperCase());
  }

  private final boolean isSilent(String goesInEar) {
    return goesInEar.trim().isEmpty();
  }

  private final boolean isQuestion(String goesInEar) {
    return goesInEar.endsWith("?");
  }
}
