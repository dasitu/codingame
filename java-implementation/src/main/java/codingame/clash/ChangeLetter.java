package codingame.clash;

import java.util.Scanner;

public class ChangeLetter {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String S = in.nextLine();

    StringBuilder s = new StringBuilder();
    for (int i = 0; i < S.length() / 2; i++) {
      String w = S.substring(i * 2, 2 * i + 2);
      s.append(w.charAt(1));
      s.append(w.charAt(0));
    }
    if (S.length() - s.length() != 0) {
      String l = S.substring(s.length());
      s.append(l);
    }
    System.out.println(s.toString());
  }
}
