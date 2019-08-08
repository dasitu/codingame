package codingame.clash;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class CenturyName {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int y = in.nextInt();
    if (y == 0) {
      System.out.println("INVALID");
      return;
    }
    Map<Integer, String> n = new HashMap<>();
    n.put(1, "st");
    n.put(2, "nd");
    n.put(3, "rd");
    int m = Math.abs(y) / 100 + 1;

    StringBuilder f = new StringBuilder();
    f.append(m);
    f.append(n.getOrDefault(m % 10, "th"));
    f.append(" century ");
    if (y > 0) {
      f.append("CE");
    } else {
      f.append("BCE");
    }

    System.out.println(f.toString());
  }
}
