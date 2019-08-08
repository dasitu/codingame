package codingame.clash;

import java.util.Scanner;

public class Ostrich {

  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    String G = in.next();
    int W = in.nextInt();

    String s = "UNKNOWN";
    if (G.equals("F")){
      s = String.valueOf((int)(W*1.2));
    } else if (G.equals("M")){
      s = String.valueOf((int)(W/1.2));
    }
    System.out.println(s);
  }
}
