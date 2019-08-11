package codingame.clash;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class CountChars {
  public static void main(String[] args) {
      Scanner in = new Scanner(System.in);
      String inputString = in.nextLine();
      List<Character> f = new ArrayList<>();
      inputString.chars().distinct().forEach(c -> f.add((char)c));
      Collections.sort(f);
      for (char c: f){
        int count = 0;
        for (char ic: inputString.toCharArray()){
          if (c == ic){
            count++;
          }
        }
        System.out.print(c);
        System.out.println(count);
      }
  }
}