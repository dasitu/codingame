//https://www.codingame.com/ide/puzzle/may-the-triforce-be-with-you

package codingame.easy;

import java.util.Scanner;

public class Triforce {

  private static String[][] triforce;

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int singleHeight = in.nextInt();

    // n == 1 is the special case, handle it separately.
    if (singleHeight == 1) {
      triforce = new String[][]{{".", "*"}, {"*", null, "*"}};
    } else {
      // for "arithmetic sequence"
      // a_{1} is the first element
      // d is the common difference
      // then nth element value a_{n}=a_{1}+(n-1)d
      int singleWidth = 1 + ((singleHeight - 1) * 2);
      int maxHeight = 2 * singleHeight;
      int maxWidth = 2 * singleWidth + 1;
      triforce = new String[maxHeight][maxWidth];
      triforce[0][0] = ".";

      // draw three triangle at the same time
      // since they are the same, just the relevant position is different
      for (int currentRow = 1; currentRow <= singleHeight; currentRow++) {
        int currentWidth = 1 + ((currentRow - 1) * 2);
        int startCol = singleWidth + (-1 * (currentRow - 1));
        int startRow = 0;
        for (int currentCol = 0; currentCol < currentWidth; currentCol++) {
          // first triangle
          int firstRow = currentRow + startRow - 1;
          int firstCol = currentCol + startCol;
          //second triangle
          int secondRow = firstRow + singleHeight;
          int secondCol = firstCol - singleHeight;
          //third triangle, row is the same with second row
          int thirdCol = secondCol + singleWidth + 1;

          triforce[firstRow][firstCol] = "*";
          triforce[secondRow][secondCol] = "*";
          triforce[secondRow][thirdCol] = "*";
        }
      }
    }

    // print the triforce
    printTriforce();
  }

  private static void printTriforce() {
    for (String[] rows : triforce) {
      StringBuilder rowContent = new StringBuilder();
      for (String v : rows) {
        rowContent.append((v == null) ? " " : v);
      }
      System.out.println(rowContent.toString().replaceAll("\\s+$", ""));
    }
  }

}