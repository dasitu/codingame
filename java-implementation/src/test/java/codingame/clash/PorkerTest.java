package codingame.clash;

import org.junit.Test;
import utils.StdInOutTestUtils;

public class PorkerTest extends StdInOutTestUtils {

  @Test
  public void testPair1(){
    String[] input = {
            "2",
            "Phil 4 4 6",
            "Melinda 3 3 5",
    };
    String[] output = {
            "Phil"
    };
    testWithInputOutput(input, output);
  }

  @Test
  public void testPair2(){
    String[] input = {
            "2",
            "Phil 4 4 6",
            "Melinda 4 4 9",
    };
    String[] output = {
            "Melinda"
    };
    testWithInputOutput(input, output);
  }

  @Test
  public void testPair3(){
    String[] input = {
            "2",
            "Phil 4 4 6",
            "Melinda 4 4 6",
    };
    String[] output = {
            "Phil Melinda"
    };
    testWithInputOutput(input, output);
  }

  @Test
  public void testTriple1(){
    String[] input = {
            "2",
            "Phil 4 4 4",
            "Melinda 3 3 3",
    };
    String[] output = {
            "Phil"
    };
    testWithInputOutput(input, output);
  }

  @Test
  public void testTriple2(){
    String[] input = {
            "2",
            "Phil 4 4 4",
            "Melinda 1 2 3",
    };
    String[] output = {
            "Phil"
    };
    testWithInputOutput(input, output);
  }

  @Test
  public void testStraight1(){
    String[] input = {
            "2",
            "Phil 4 4 1",
            "Melinda 1 2 3",
    };
    String[] output = {
            "Melinda"
    };
    testWithInputOutput(input, output);
  }

  @Test
  public void testStraight2(){
    String[] input = {
            "2",
            "Phil 4 5 6",
            "Melinda 1 2 3",
    };
    String[] output = {
            "Phil"
    };
    testWithInputOutput(input, output);
  }

  @Test
  public void testStraight3(){
    String[] input = {
            "2",
            "Phil 1 2 3",
            "Melinda 1 2 3",
    };
    String[] output = {
            "Phil Melinda"
    };
    testWithInputOutput(input, output);
  }

  @Test
  public void testHighCard1(){
    String[] input = {
            "2",
            "Phil 1 2 3",
            "Melinda 5 4 1",
    };
    String[] output = {
            "Phil"
    };
    testWithInputOutput(input, output);
  }

  @Test
  public void testHighCard2(){
    String[] input = {
            "2",
            "Phil 1 4 3",
            "Melinda 5 4 1",
    };
    String[] output = {
            "Melinda"
    };
    testWithInputOutput(input, output);
  }

  @Test
  public void testHighCard3(){
    String[] input = {
            "2",
            "Phil 1 4 3",
            "Melinda 3 4 1",
    };
    String[] output = {
            "Phil Melinda"
    };
    testWithInputOutput(input, output);
  }
}
