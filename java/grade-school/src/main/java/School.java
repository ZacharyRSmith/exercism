import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

public class School {
  private HashMap<String, Integer> gradeDB;

  School(){
    gradeDB=new HashMap <String, Integer>();
  }

  public void add(String name, int grade){
    gradeDB.put(name, new Integer(grade));
  }

  public HashMap<Integer, List<String>> db(){
    HashMap<Integer, List<String>> gradeList = new HashMap<Integer, List<String>>();
    for(Integer grade: gradeDB.values()){
      List <String> sortedList = 
          gradeDB.keySet()
          .stream()
          .filter(p-> gradeDB
              .get(p)
              .equals(grade))
          .collect(Collectors.toList()); 
      Collections.sort(sortedList);
      gradeList.put(grade, sortedList);
    }
    return gradeList;
  }
  
  public List <String> grade(Integer grade){
    List <String> returnedList = db().get(grade);
    return (returnedList==null) ? new ArrayList<String>() : returnedList ;
  }
  
  public HashMap<Integer, List<String>> sort(){
    return this.db();
  }
}