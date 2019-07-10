package codingame.easy;

import org.junit.Test;
import utils.StdInOutTestUtils;

public class TriforceStdInOutTest extends StdInOutTestUtils {

  @Test
  public void test1(){
    String[] input = {"1"};
    String[] output = {
            ".*",
            "* *"};
    testWithInputOutput(input, output);
  }

  @Test
  public void test3(){
    String[] input = {"3"};
    String[] output = {
            ".    *",
            "    ***",
            "   *****",
            "  *     *",
            " ***   ***",
            "***** *****"};
    testWithInputOutput(input, output);
  }

  @Test
  public void test5(){
    String[] input = {"5"};
    String[] output = {
            ".        *",
            "        ***",
            "       *****",
            "      *******",
            "     *********",
            "    *         *",
            "   ***       ***",
            "  *****     *****",
            " *******   *******",
            "********* *********"
    };
    testWithInputOutput(input, output);
  }

  @Test
  public void test10(){
    String[] input = {"10"};
    String[] output = {
            ".                  *",
            "                  ***",
            "                 *****",
            "                *******",
            "               *********",
            "              ***********",
            "             *************",
            "            ***************",
            "           *****************",
            "          *******************",
            "         *                   *",
            "        ***                 ***",
            "       *****               *****",
            "      *******             *******",
            "     *********           *********",
            "    ***********         ***********",
            "   *************       *************",
            "  ***************     ***************",
            " *****************   *****************",
            "******************* *******************"
    };
    testWithInputOutput(input, output);
  }

}
