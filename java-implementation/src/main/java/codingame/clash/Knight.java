package codingame.clash;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Knight {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int col = 0;
    int row = 0;
    for (int i = 0; i < 8; i++) {
      String n = in.next();
      if (n.contains("N")) {
        col = n.indexOf("N") + 1;
        row = 8 - i;
        break;
      }
    }

    List<Integer> colPossible = Arrays.asList(-1, -1, +1, +1, +2, +2, -2, -2);
    List<Integer> rowPossible = Arrays.asList(+2, -2, +2, -2, +1, -1, +1, -1);
    List<String> finalResult = new ArrayList<>();
    for (int i = 0; i < colPossible.size(); i++) {
      int colP = col + colPossible.get(i);
      int rowP = row + rowPossible.get(i);
      StringBuilder tempPos = new StringBuilder();
      if (colP < 9 && colP > 0 && rowP < 9 && rowP > 0) {
        String colSymbol = String.valueOf((char) ((int) 'a' + colP - 1));
        tempPos.append(colSymbol);
        tempPos.append(rowP);
        finalResult.add(tempPos.toString());
      }
    }

    Collections.sort(finalResult);
    for (String pos : finalResult) {
      System.out.println(pos);
    }
  }
}
