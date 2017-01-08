import java.util.*;

/**
 * Given a person's allergy score, then can tell whether or not they're allergic
 * to a given item, and can give their full list of allergies.
 */
public class Allergies {
  private List<Allergen> list;

  Allergies(int score) {
    this.list = genList(score);
  }

  public List<Allergen> getList() {
    return this.list;
  }

  public Boolean isAllergicTo(Allergen allergen) {
    return list.contains(allergen);
  }

  private static List<Allergen> genList(int score) {
    List<Allergen> res = new ArrayList<Allergen>();

    for (Allergen allergen : Allergen.values()) {
      if ((allergen.getScore() & score) != 0) res.add(allergen);
    }

    return res;
  }
}
