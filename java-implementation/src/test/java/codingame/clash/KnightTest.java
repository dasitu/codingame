package codingame.clash;

import org.junit.Test;
import utils.StdInOutTestUtils;

public class KnightTest extends StdInOutTestUtils {

    @Test
    public void test1() {
      String[] input = {
          "........8",
          "........7",
          "........6",
          "........5",
          "........4",
          "..N.....3",
          "........2",
          "........1",
          "abcdefgh",
      };
      String[] output = {
              "a2",
              "a4",
              "b1",
              "b5",
              "d1",
              "d5",
              "e2",
              "e4",
      };
      testWithInputOutput(input, output);
    }

  @Test
  public void test2() {
    String[] input = {
            "........8",
            "........7",
            "........6",
            "....N...5",
            "........4",
            "........3",
            "........2",
            "........1",
            "abcdefgh",
    };
    String[] output = {
            "c4",
            "c6",
            "d3",
            "d7",
            "f3",
            "f7",
            "g4",
            "g6",
    };
    testWithInputOutput(input, output);
  }

  @Test
  public void test3() {
    String[] input = {
            "........8",
            "......N.7",
            "........6",
            "........5",
            "........4",
            "........3",
            "........2",
            "........1",
            "abcdefgh",
    };
    String[] output = {
            "e6",
            "e8",
            "f5",
            "h5",
    };
    testWithInputOutput(input, output);
  }

  @Test
  public void test4() {
    String[] input = {
            "........8",
            "........7",
            "........6",
            "........5",
            "........4",
            "........3",
            "........2",
            "N.......1",
            "abcdefgh",
    };
    String[] output = {
            "b3",
            "c2",
    };
    testWithInputOutput(input, output);
  }
}
