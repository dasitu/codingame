package codingame.clash;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class VowelOrder {

  public static void main(String[] args) {
    List<Character> vowel = Arrays.asList('A', 'E', 'I', 'O', 'U');
    Scanner in = new Scanner(System.in);
    int N = in.nextInt();
    if (in.hasNextLine()) {
      in.nextLine();
    }
    for (int i = 0; i < N; i++) {
      String WORD = in.nextLine();
      Character[] word = WORD.chars() 				// IntStream
              .mapToObj(ch -> (char) ch)            // Stream<Character>
              .toArray(Character[]::new);
      String finalStr = "NONE";
      Arrays.sort(word, Collections.reverseOrder());
      for (Character w: word){
        if (vowel.contains(Character.toUpperCase(w))){
          finalStr = String.valueOf(w);
          break;
        }
      }
      System.out.println(finalStr);
    }
  }
}