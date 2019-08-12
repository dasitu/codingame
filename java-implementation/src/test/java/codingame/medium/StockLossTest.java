package codingame.medium;

import org.junit.Test;
import utils.StdInOutTestUtils;

public class StockLossTest extends StdInOutTestUtils {

  @Test
  public void test1(){
    String[] input = {"6", "3 2 4 2 1 5"};
    String[] output = {"-3"};
    testWithInputOutput(input, output);
  }

  @Test
  public void test2(){
    String[] input = {"6", "5 3 4 2 3 1"};
    String[] output = {"-4"};
    testWithInputOutput(input, output);
  }

  @Test
  public void test3(){
    String[] input = {"5", "1 2 4 4 5"};
    String[] output = {"0"};
    testWithInputOutput(input, output);
  }

  @Test
  public void test4(){
    String[] input = {"5", "3 4 7 9 10"};
    String[] output = {"0"};
    testWithInputOutput(input, output);
  }

  @Test
  public void test6(){
    String[] input = {"6", "3 2 10 7 15 14"};
    String[] output = {"-3"};
    testWithInputOutput(input, output);
  }
}
