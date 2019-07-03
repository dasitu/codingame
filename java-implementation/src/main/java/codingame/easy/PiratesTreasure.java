// https://www.codingame.com/ide/puzzle/pirates-treasure

package codingame.easy;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class PiratesTreasure {

  private static final int[] INC_ROW = {-1, -1, -1, 0, 0, 1, 1, 1};
  private static final int[] INC_COL = {-1, 0, 1, -1, 1, -1, 0, 1};

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    int width = in.nextInt();
    int height = in.nextInt();
    Integer[][] treasureMapMatrix = new Integer[height][width];
    ArrayList<ArrayList<Integer>> zeroPosition = new ArrayList<>();
    ArrayList<Integer> treasurePosition = new ArrayList<>();
    for (int i = 0; i < height; i++) {
      for (int j = 0; j < width; j++) {
        int v = in.nextInt();
        treasureMapMatrix[i][j] = v;
        if (v == 0) {
          zeroPosition.add(new ArrayList<>(Arrays.asList(i, j)));
        }
      }
    }

    for (ArrayList<Integer> pos : zeroPosition) {
      int j;
      for (j = 0; j < 8; j++) {
        int toBeCheckedRow = pos.get(0) + INC_ROW[j];
        int toBeCheckedCol = pos.get(1) + INC_COL[j];

        // prevent out of index error
        if (toBeCheckedRow < 0 || toBeCheckedRow > height - 1
                || toBeCheckedCol < 0 || toBeCheckedCol > width - 1) {
          continue;
        }
        // not treasure, break
        if (treasureMapMatrix[toBeCheckedRow][toBeCheckedCol] == 0) {
          break;
        }
      }
      if (j == INC_ROW.length) {
        treasurePosition = pos;
        break;
      }
    }

    System.err.println("treasureMapMatrix:" + Arrays.deepToString(treasureMapMatrix));
    System.err.println("zeroPosition:" + zeroPosition.toString());
    System.out.println(treasurePosition.get(1) + " " + treasurePosition.get(0));
  }
}
