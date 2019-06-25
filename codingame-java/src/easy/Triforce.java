//https://www.codingame.com/ide/puzzle/may-the-triforce-be-with-you
package easy;

import java.util.Scanner;

class Triforce {

  static private String[][] triforce;

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int N = in.nextInt();
    if( N == 1 ){
      triforce = new String[][]{{".","*"},{"*",null,"*"}};
    }
    else {
      int width = 1 + ((N-1)*2);
      triforce = new String[2*N][2*width + 1];
      triforce[0][0] = ".";
      // add first triforce
      int row = 0;
      int col = width;
      addOneTriforce(row, col, N);

      // add second triforce
      row = N;
      col = N - 1;
      addOneTriforce(row, col, N);

      // add third triforce
      col = col + width + 1;
      addOneTriforce(row, col, N);
    }

    for (String[] rows: triforce) {
      StringBuilder rowContent = new StringBuilder();
      for (String v: rows){
        if(v == null){
          v = " ";
        }
        rowContent.append(v);
      }
      System.out.println(rowContent.toString().replaceAll("\\s+$",""));
    }
  }

  private static void addOneTriforce(int row, int col, int size){
    for (int i = 1; i <= size; i++) {
      int width = 1 + ((i-1)*2);
      int startPos = -1 * (i - 1) + col;
      for (int j = 0; j < width; j++) {
        triforce[row + i - 1][j + startPos] = "*";
      }
    }
  }

}