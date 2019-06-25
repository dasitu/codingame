//https://www.codingame.com/ide/puzzle/may-the-triforce-be-with-you

package easy;

import java.util.Scanner;

class Triforce {

  private static String[][] triforce;

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int height = in.nextInt();

    // n == 1 is the special case, handle it separately.
    if (height == 1) {
      triforce = new String[][]{{".", "*"}, {"*", null, "*"}};
    } else {
      // for "arithmetic sequence"
      // a_{1} is the first element
      // d is the common difference
      // then nth element value a_{n}=a_{1}+(n-1)d
      int width = 1 + ((height - 1) * 2);
      triforce = new String[2 * height][2 * width + 1];
      triforce[0][0] = ".";
      // add first triforce
      int row = 0;
      int col = width;
      addOneTriforce(row, col, height);

      // add second triforce, col move height step on the left
      row = height;
      col -= height;
      addOneTriforce(row, col, height);

      // add third triforce, col move width+1 step on the right
      col += width + 1;
      addOneTriforce(row, col, height);
    }

    // print the triforce
    printTriforce();
  }

  private static void addOneTriforce(int topMostRow, int topMostCol, int height) {
    // row, col defined the top most point of the triangle
    // size is the height of the triangle
    for (int i = 1; i <= height; i++) {
      int width = 1 + ((i - 1) * 2);
      int startCol = -1 * (i - 1) + topMostCol;
      for (int j = 0; j < width; j++) {
        triforce[topMostRow + i - 1][j + startCol] = "*";
      }
    }
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