package codingame.clash;

import java.util.Scanner;

public class RepeatLetters {

  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    int N = in.nextInt();
    if (in.hasNextLine()) {
      in.nextLine();
    }
    StringBuilder s = new StringBuilder();
    for (int i = 0; i < N; i++) {
      String S = in.nextLine();
      for(int j = 0; j < S.length() - 1; j++) {
        char c = S.charAt(j);
        if ( S.substring(j + 1).contains(Character.toString(c))){
          if (Character.isLetter(c)) {
            s.append(c);
          }
        }
      }
    }
    System.out.println(s.length()==0 ? "NONE":s.toString());
  }
}