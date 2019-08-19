package leetcode;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class No227BasicCalculatorIiTest {

  public No227BasicCalculatorIi testObject = new No227BasicCalculatorIi();

  @Test
  void test1(){
    String input = "1+(1+(14*(-5)-2)/3)*(6+8)";
    int output = -321;
    assertEquals(output, testObject.calculate(input));
  }

  @Test
  void basic(){
    String input = "1 + 1";
    int output = 2;
    assertEquals(output, testObject.calculate(input));
  }

  @Test
  void withBlank(){
    String input = " 2-1 + 2 ";
    int output = 3;
    assertEquals(output, testObject.calculate(input));
  }

  @Test
  void biggerThan10(){
    String input = "1+11-3";
    int output = 9;
    assertEquals(output, testObject.calculate(input));
  }

  @Test
  void negative(){
    String input = "2-(5-6)";
    int output = 3;
    assertEquals(output, testObject.calculate(input));
  }

  @Test
  void negativeStart(){
    String input = "-2-(5-6)";
    int output = -1;
    assertEquals(output, testObject.calculate(input));
  }

  @Test
  void emptyFinalNegative(){
    String input = "-5-(1+(5))";
    int output = -11;
    assertEquals(output, testObject.calculate(input));
  }

  @Test
  void emptyFinal(){
    String input = "(5-(1+(5)))";
    int output = -1;
    assertEquals(output, testObject.calculate(input));
  }

  @Test
  void withParentheses(){
    String input = "(1+(4+5+2)-3)+(6+8)";
    int output = 23;
    assertEquals(output, testObject.calculate(input));
  }

  @Test
  void veryBigInput(){
    String input = "(1+(4+5+2)-3)+(6+8)";
    int output = 23;
    assertEquals(output, testObject.calculate(input));
  }

}
