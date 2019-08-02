package codingame.easy;

import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class HappyNumbers {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int N = in.nextInt();
    if (in.hasNextLine()) {
      in.nextLine();
    }
    for (int i = 0; i < N; i++) {
      String x = in.nextLine();
      String symbol = isHappyNumber(x, new LinkedList<>()) ? " :)" : " :(";
      System.out.println(x + symbol);
    }
  }

  private static boolean isHappyNumber(String num, List<String> history) {
    if (num.equals("1")) {
      return true;
    }
    if (history.contains(num)) {
      return false;
    } else {
      history.add(num);
    }

    int nextNum = 0;
    for (char n : num.toCharArray()) {
      int v = Character.getNumericValue(n);
      nextNum += v * v;
    }
    return isHappyNumber(String.valueOf(nextNum), history);
  }
}
