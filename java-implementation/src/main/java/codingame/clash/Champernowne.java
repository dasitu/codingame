package codingame.clash;

import java.util.*;

class Champernowne {

  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    StringBuilder s = new StringBuilder();
    for (int i = 1; i < n + 2; i++) {
      s.append(i);
    }
    System.out.println(s.toString().toCharArray()[n-1]);
  }
}