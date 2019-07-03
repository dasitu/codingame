// https://www.codingame.com/ide/puzzle/rectangular-block-spinner

package codingame.easy;

import java.util.Scanner;

public class RectangularBlockSpinner {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int size = in.nextInt();
    int angle = in.nextInt();

    int longerSize = 2 * size - 1;

    // final output diamond shape
    char[][] diamond = new char[longerSize][longerSize];
    // inital the diamond with blank
//    for (int lineIndex = 0; lineIndex < diamond.length; lineIndex++) {
//      char[] allBlank = String.join("",
//              Collections.nCopies(diamond[0].length, " "))
//              .toCharArray();
//      diamond[lineIndex] = allBlank;
//    }
    // actual rotate count since every 360 degree is the same
    int rotateCount = (angle / 45) % 8;

    if (in.hasNextLine()) {
      in.nextLine();
    }

    // read from the square and write to the diamond
    for (int row = 0; row < size; row++) {
      String line = in.nextLine();

      for (int col = 0; col < size; col++) {
        int startRow = 0;
        int startCol = 0;
        char value = line.charAt(col * 2);
        switch (rotateCount) {
          case 1: // rotate 45 * 1 = 45
            startRow = size - 1;
            startCol = 0;
            diamond[startRow + row - col][startCol + row + col] = value;
            break;
          case 3: // rotate 45 * 3 = 135
            startRow = longerSize - 1;
            startCol = size - 1;
            diamond[startRow - row - col][startCol + row - col] = value;
            break;
          case 5: // rotate 45 * 5 = 225
            startRow = size - 1;
            startCol = longerSize - 1;
            diamond[startRow + row - col][startCol - row - col] = value;
            break;
          case 7: // rotate 45 * 7 = 315
            startRow = 0;
            startCol = size - 1;
            diamond[startRow + row + col][startCol - row + col] = value;
            break;
          default:
            break;
        }
      }
    }

    // print the diamond
    // replace inital value with blank
    for (char[] line : diamond) {
      for (int i = 0; i < line.length; i++) {
        line[i] = line[i] == '\u0000' ? ' ' : line[i];
      }
      System.out.println(String.valueOf(line));
    }
  }
}