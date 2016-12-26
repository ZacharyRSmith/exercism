import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DNA {

  private static final ArrayList<Character> validNucleotides
    = new ArrayList<Character>();

  static {
    validNucleotides.add('G');
    validNucleotides.add('A');
    validNucleotides.add('T');
    validNucleotides.add('C');
  }

  private static final HashMap<Character, Integer> nucleotideCounts
    = new HashMap<Character, Integer>();

  static String sequence;

  public DNA(String sequence) {
    this.sequence = sequence;

    for (Character nucleotide : validNucleotides) {
      this.nucleotideCounts.put(nucleotide, 0);
    }

    for (Map.Entry<Character, Integer> nucleotideCount : this.nucleotideCounts.entrySet()) {
      nucleotideCount.setValue(countPrivate(nucleotideCount.getKey()));
    }
  }

  public int count(char nucleotide) {
    if (!isValidNucleotide(nucleotide)) {
      throw new IllegalArgumentException(nucleotide + " is not a nucleotide!");
    }

    return this.nucleotideCounts.get(nucleotide);
  }

  public Map nucleotideCounts() {
    HashMap<Character, Integer> nucleotideCounts = new HashMap<Character, Integer>();

    for (Character nucleotide : validNucleotides) {
      nucleotideCounts.put(nucleotide, 0);
    }

    for (Map.Entry<Character, Integer> nucleotideCount : nucleotideCounts.entrySet()) {
      nucleotideCount.setValue(countPrivate(nucleotideCount.getKey()));
    }

    return nucleotideCounts;
  }

  private static boolean isValidNucleotide(char nucleotide) {
    return validNucleotides.contains(nucleotide);
  }

  private int countPrivate(char nucleotide) {
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
}
