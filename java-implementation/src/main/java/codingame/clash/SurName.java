package codingame.clash;

import java.util.Scanner;

public class SurName {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int a = in.nextInt();
    if (in.hasNextLine()) {
      in.nextLine();
    }
    for (int i = 0; i < a; i++) {
      String name = in.nextLine();
      String[] c = name.split(",");
      String b = "N/A";
      if (c.length > 1) {
        b = c[c.length - 1];
      }
      System.out.println(b.trim());
    }
  }
}
