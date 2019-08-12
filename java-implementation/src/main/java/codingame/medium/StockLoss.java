// https://www.codingame.com/training/medium/stock-exchange-losses
package codingame.medium;

import java.util.Arrays;
import java.util.Scanner;

public class StockLoss {

  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    int[] allData = new int[n];
    for (int i = 0; i < n; i++) {
      int v = in.nextInt();
      allData[i] = v;
    }

    int biggestLoss = 0;
    int highestValue = 0;
    for (int i = 0; i < n-1; i++) {
      int currentValue = allData[i];
      if (currentValue <= highestValue){
        continue;
      }
      int[] laterData = Arrays.copyOfRange(allData, i+1, n);
      Arrays.sort(laterData);
      int loss = laterData[0] - currentValue;
      if (loss < biggestLoss) {
        biggestLoss = loss;
        highestValue = currentValue;
      }
    }
    System.out.println(biggestLoss);
  }
}