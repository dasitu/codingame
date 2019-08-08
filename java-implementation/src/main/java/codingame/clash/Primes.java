package codingame.clash;

import java.util.Scanner;

public class Primes {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    int c = 0;
    for (int i = 0; i < n; i++) {
      if (isPrime(i)) {
        System.err.println(i);
        c++;
      }
    }
    System.out.println(c);
  }

  private static boolean isPrime(int n) {
    //    // check if n is a multiple of 2
    //    if (n % 2 == 0) return false;
    //    // if not, then just check the odds
    //    for (int i = 3; i * i <= n; i += 2) {
    //      if (n % i == 0) return false;
    //    }
    //    return true;
    if (n <= 1) {
      return false;
    }
    for (int i = 2; i < n; i++) {
      if (n % i == 0) {
        return false;
      }
    }
    return true;
  }
}
