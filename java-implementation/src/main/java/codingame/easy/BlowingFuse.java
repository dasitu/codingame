// https://www.codingame.com/ide/puzzle/blowing-fuse

package codingame.easy;

import java.util.Scanner;

public class BlowingFuse {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int numOfDevices = in.nextInt();
    int numOfClick = in.nextInt();
    int capacity = in.nextInt();
    int[] devices = new int[numOfDevices];
    int[] deviceStates = new int[numOfDevices];
    for (int i = 0; i < numOfDevices; i++) {
      devices[i] = in.nextInt();
      deviceStates[i] = 1; // 1 for off and -1 for on
    }
    int maxPowerConsume = 0;
    int currentPowerConsume = 0;
    for (int i = 0; i < numOfClick; i++) {
      int mx = in.nextInt();
      currentPowerConsume += devices[mx - 1] * deviceStates[mx - 1];
      deviceStates[mx - 1] *= -1;
      if (currentPowerConsume > capacity) {
        System.out.println("Fuse was blown.");
        return;
      }
      maxPowerConsume = Integer.max(maxPowerConsume, currentPowerConsume);
    }
    System.out.println("Fuse was not blown.");
    System.out.println("Maximal consumed current was " + maxPowerConsume + " A.");
  }
}
