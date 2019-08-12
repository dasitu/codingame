package codingame.medium;

import org.junit.Test;
import utils.StdInOutTestUtils;

public class SudokuSolverTest extends StdInOutTestUtils {

  @Test
  public void veryEasy() {
    String[] input = {
            "120070560",
            "507932080",
            "000001000",
            "010240050",
            "308000402",
            "070085010",
            "000700000",
            "080423701",
            "034010028",
    };
    String[] output = {
            "123874569",
            "567932184",
            "849651237",
            "916247853",
            "358196472",
            "472385916",
            "291768345",
            "685423791",
            "734519628",
    };
    testWithInputOutput(input, output);
  }

  @Test
  public void easy() {
    String[] input = {
            "000700040",
            "020801900",
            "000000173",
            "102006097",
            "600090001",
            "970100405",
            "354000000",
            "008604030",
            "010003000",
    };
    String[] output = {
            "531769248",
            "427831956",
            "869425173",
            "182546397",
            "645397821",
            "973182465",
            "354278619",
            "798614532",
            "216953784",
    };
    testWithInputOutput(input, output);
  }

  @Test
  public void intermediate() {
    String[] input = {
            "006000050",
            "003700000",
            "700035008",
            "000070012",
            "000942000",
            "620080000",
            "900120003",
            "000003600",
            "050000700",
    };
    String[] output = {
            "816294357",
            "543718269",
            "792635148",
            "438576912",
            "175942836",
            "629381475",
            "964127583",
            "287453691",
            "351869724",
    };
    testWithInputOutput(input, output);
  }

  @Test
  public void worldsHardest() {
    String[] input = {
            "800000000",
            "003600000",
            "070090200",
            "050007000",
            "000045700",
            "000100030",
            "001000068",
            "008500010",
            "090000400",
    };
    String[] output = {
            "812753649",
            "943682175",
            "675491283",
            "154237896",
            "369845721",
            "287169534",
            "521974368",
            "438526917",
            "796318452",
    };
    testWithInputOutput(input, output);
  }

}