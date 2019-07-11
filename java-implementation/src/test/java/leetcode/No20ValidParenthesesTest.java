package leetcode;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;


public class No20ValidParenthesesTest {
  private No20ValidParentheses testObject = new No20ValidParentheses();

  @Test
  public void failed1() {
    String input = "]";
    boolean expected = false;
    assertEquals(expected, testObject.isValid(input));
  }

  @Test
  public void example1() {
    String input = "()";
    boolean expected = true;
    assertEquals(expected, testObject.isValid(input));
  }

  @Test
  public void example2() {
    String input = "()[]{}";
    boolean expected = true;
    assertEquals(expected, testObject.isValid(input));
  }

  @Test
  public void example3() {
    String input = "(]";
    boolean expected = false;
    assertEquals(expected, testObject.isValid(input));
  }

  @Test
  public void example4() {
    String input = "([)]";
    boolean expected = false;
    assertEquals(expected, testObject.isValid(input));
  }

  @Test
  public void example5() {
    String input = "{[]}";
    boolean expected = true;
    assertEquals(expected, testObject.isValid(input));
  }
}
