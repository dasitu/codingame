package codingame.clash;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class WebAddress {

  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    String w = in.nextLine();

    int a = 0;
    for (char c: w.toCharArray()){
      a += c;
    }

    List<String> s = new ArrayList<>();
    for (int i = 1; i < 5; i++) {
      s.add(String.valueOf((a*i) % 256));
    }
    System.out.println(String.join(".", s));
  }
}
