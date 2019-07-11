package leetcode;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class No344ReverseStringTest {

  private No344ReverseString testObject = new No344ReverseString();

  @Test
  public void example1(){
    char[] input = {'h','e','l','l','o'};
    char[] output = {'o','l','l','e','h'};
    testObject.reverseString(input);
    assertEquals(String.valueOf(output), String.valueOf(input));
  }

  @Test
  public void example2(){
    char[] input = {'H','a','n','n','a','h'};
    char[] output = {'h','a','n','n','a','H'};
    testObject.reverseString(input);
    assertEquals(String.valueOf(output), String.valueOf(input));
  }
}
