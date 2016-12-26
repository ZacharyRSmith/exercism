import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DNA {

  private static final List<Character> validNucleotides = new ArrayList<Character>();

  static {
    validNucleotides.add('G');
    validNucleotides.add('A');
    validNucleotides.add('T');
    validNucleotides.add('C');
  }

  static String sequence;
  static HashMap<Character, Integer> nucleotideCounts = new HashMap<>();

  public DNA(String sequence) {
    this.sequence = sequence;
  }

  public int count(char nucleotide) {
    if (!isValidNucleotide(nucleotide)) {
      throw new IllegalArgumentException(nucleotide + " is not a nucleotide!");
    }

    int count = 0;

    for (char sequenceNucleotide : this.sequence.toCharArray()) {
      if (sequenceNucleotide == nucleotide) {
        count++;
      }
    }

    return count;
  }

  public Map nucleotideCounts() {
    HashMap<Character, Integer> nucleotideCounts = new HashMap<Character, Integer>();

    for (Character nucleotide : validNucleotides) {
      nucleotideCounts.put(nucleotide, 0);
    }

    for (Map.Entry<Character, Integer> nucleotideCount : nucleotideCounts.entrySet()) {
      nucleotideCount.setValue(count(nucleotideCount.getKey()));
    }

    return nucleotideCounts;
  }

  private static boolean isValidNucleotide(char nucleotide) {
    return validNucleotides.contains(nucleotide);
  }
}
