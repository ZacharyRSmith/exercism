import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.List;

/**
 * Stores students' names and grades.
 */
public class School {
  // key: Grade number.
  // value: List of students names.
  private Map<Integer, List<String>> db;

  School() {
    this.db = new HashMap<Integer, List<String>>();
  }

  /**
   * Adds student to a grade.
   *
   * @paran name: Name of student.
   * @param grade: Grade of student.
   */
  public final void add(String name, int grade) {
    createGrade(grade);
    List<String> studentsInGrade = this.db.get(grade);
    studentsInGrade.add(name);
  }

  /**
   * Returns this school's db.
   */
  public final Map<Integer, List<String>> db() {
    return this.db;
  }

  /**
   * Returns the list of student names in @param grade.
   */
  public final List<String> grade(int grade) {
    createGrade(grade);
    return this.db.get(grade);
  }

  /**
   * Sorts the school's db, then returns it.
   */
  public final Map<Integer, List<String>> sort() {
    for (Map.Entry<Integer, List<String>> gradePair : this.db().entrySet()) {
      List<String> names = gradePair.getValue();
      Collections.sort(names);
    }
    return this.db();
  }

  private final void createGrade(int grade) {
    if (this.db.containsKey(grade)) return;
    this.db.put(grade, new ArrayList<String>());
  }
}
