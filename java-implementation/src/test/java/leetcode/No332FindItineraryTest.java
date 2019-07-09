package leetcode;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class No332FindItineraryTest {

  private No332FindItinerary testObject = new No332FindItinerary();

  private List<List<String>> array2List(String[][] inputArray) {
    List<List<String>> inputList = new ArrayList<>();
    for (String[] input : inputArray) {
      inputList.add(Arrays.asList(input));
    }
    return inputList;
  }

  @Test
  public void example1() {

    String[][] input = {{"MUC", "LHR"}, {"JFK", "MUC"}, {"SFO", "SJC"}, {"LHR", "SFO"}};
    String[] output = {"JFK", "MUC", "LHR", "SFO", "SJC"};
    assertEquals(Arrays.asList(output), testObject.findItinerary(array2List(input)));
  }

  @Test
  public void example2() {

    String[][] input = {{"JFK", "SFO"}, {"JFK", "ATL"}, {"SFO", "ATL"}, {"ATL", "JFK"}, {"ATL", "SFO"}};
    String[] output = {"JFK", "ATL", "JFK", "SFO", "ATL", "SFO"};
    assertEquals(Arrays.asList(output), testObject.findItinerary(array2List(input)));
  }

  @Test
  public void failed1() {

    String[][] input = {{"JFK", "KUL"}, {"JFK", "NRT"}, {"NRT", "JFK"}};
    String[] output = {"JFK", "NRT", "JFK", "KUL"};
    assertEquals(Arrays.asList(output), testObject.findItinerary(array2List(input)));
  }

  @Test
  public void failed3() {

    String[][] input = {{"MUC", "LHR"}, {"JFK", "MUC"}, {"SFO", "SJC"}, {"LHR", "SFO"}};
    String[] output = {"JFK", "MUC", "LHR", "SFO", "SJC"};
    assertEquals(Arrays.asList(output), testObject.findItinerary(array2List(input)));
  }

  @Test
  public void failed2() {

    String[][] input = {{"AXA", "EZE"}, {"EZE", "AUA"}, {"ADL", "JFK"}, {"ADL", "TIA"}, {"AUA", "AXA"}, {"EZE", "TIA"}, {"EZE", "TIA"}, {"AXA", "EZE"}, {"EZE", "ADL"}, {"ANU", "EZE"}, {"TIA", "EZE"}, {"JFK", "ADL"}, {"AUA", "JFK"}, {"JFK", "EZE"}, {"EZE", "ANU"}, {"ADL", "AUA"}, {"ANU", "AXA"}, {"AXA", "ADL"}, {"AUA", "JFK"}, {"EZE", "ADL"}, {"ANU", "TIA"}, {"AUA", "JFK"}, {"TIA", "JFK"}, {"EZE", "AUA"}, {"AXA", "EZE"}, {"AUA", "ANU"}, {"ADL", "AXA"}, {"EZE", "ADL"}, {"AUA", "ANU"}, {"AXA", "EZE"}, {"TIA", "AUA"}, {"AXA", "EZE"}, {"AUA", "SYD"}, {"ADL", "JFK"}, {"EZE", "AUA"}, {"ADL", "ANU"}, {"AUA", "TIA"}, {"ADL", "EZE"}, {"TIA", "JFK"}, {"AXA", "ANU"}, {"JFK", "AXA"}, {"JFK", "ADL"}, {"ADL", "EZE"}, {"AXA", "TIA"}, {"JFK", "AUA"}, {"ADL", "EZE"}, {"JFK", "ADL"}, {"ADL", "AXA"}, {"TIA", "AUA"}, {"AXA", "JFK"}, {"ADL", "AUA"}, {"TIA", "JFK"}, {"JFK", "ADL"}, {"JFK", "ADL"}, {"ANU", "AXA"}, {"TIA", "AXA"}, {"EZE", "JFK"}, {"EZE", "AXA"}, {"ADL", "TIA"}, {"JFK", "AUA"}, {"TIA", "EZE"}, {"EZE", "ADL"}, {"JFK", "ANU"}, {"TIA", "AUA"}, {"EZE", "ADL"}, {"ADL", "JFK"}, {"ANU", "AXA"}, {"AUA", "AXA"}, {"ANU", "EZE"}, {"ADL", "AXA"}, {"ANU", "AXA"}, {"TIA", "ADL"}, {"JFK", "ADL"}, {"JFK", "TIA"}, {"AUA", "ADL"}, {"AUA", "TIA"}, {"TIA", "JFK"}, {"EZE", "JFK"}, {"AUA", "ADL"}, {"ADL", "AUA"}, {"EZE", "ANU"}, {"ADL", "ANU"}, {"AUA", "AXA"}, {"AXA", "TIA"}, {"AXA", "TIA"}, {"ADL", "AXA"}, {"EZE", "AXA"}, {"AXA", "JFK"}, {"JFK", "AUA"}, {"ANU", "ADL"}, {"AXA", "TIA"}, {"ANU", "AUA"}, {"JFK", "EZE"}, {"AXA", "ADL"}, {"TIA", "EZE"}, {"JFK", "AXA"}, {"AXA", "ADL"}, {"EZE", "AUA"}, {"AXA", "ANU"}, {"ADL", "EZE"}, {"AUA", "EZE"}};
    String[] output = {"JFK", "ADL", "ANU", "ADL", "ANU", "AUA", "ADL", "AUA", "ADL", "AUA", "ANU", "AXA", "ADL", "AUA", "ANU", "AXA", "ADL", "AXA", "ADL", "AXA", "ANU", "AXA", "ANU", "AXA", "EZE", "ADL", "AXA", "EZE", "ADL", "AXA", "EZE", "ADL", "EZE", "ADL", "EZE", "ADL", "EZE", "ANU", "EZE", "ANU", "EZE", "AUA", "AXA", "EZE", "AUA", "AXA", "EZE", "AUA", "AXA", "JFK", "ADL", "EZE", "AUA", "EZE", "AXA", "JFK", "ADL", "JFK", "ADL", "JFK", "ADL", "JFK", "ADL", "TIA", "ADL", "TIA", "AUA", "JFK", "ANU", "TIA", "AUA", "JFK", "AUA", "JFK", "AXA", "TIA", "AXA", "TIA", "EZE", "AXA", "TIA", "EZE", "JFK", "AXA", "TIA", "EZE", "JFK", "EZE", "TIA", "JFK", "EZE", "TIA", "JFK", "TIA", "JFK", "AUA", "TIA", "JFK", "AUA", "TIA", "AUA", "SYD"};
    assertEquals(Arrays.asList(output), testObject.findItinerary(array2List(input)));
  }

  @Test
  public void failed4() {
    String[][] input = {{"AXA", "AUA"},{"BNE", "ANU"},{"EZE", "ANU"},{"TIA", "JFK"},{"TIA", "BNE"},{"ANU", "BNE"},{"BNE", "AUA"},{"BNE", "ADL"},{"AXA", "ADL"},{"EZE", "AUA"},{"AUA", "AXA"},{"ADL", "AXA"},{"ADL", "TIA"},{"JFK", "ANU"},{"EZE", "JFK"},{"JFK", "AUA"},{"BNE", "EZE"},{"TIA", "ANU"},{"TIA", "AUA"},{"JFK", "TIA"},{"EZE", "ANU"},{"AXA", "JFK"},{"AUA", "OOL"},{"AUA", "AXA"},{"ANU", "BNE"},{"ANU", "EZE"},{"ANU", "TIA"},{"JFK", "EZE"},{"ADL", "ANU"},{"AXA", "BNE"},{"BNE", "ADL"},{"ANU", "EZE"},{"ANU", "JFK"},{"BNE", "AUA"},{"ANU", "AUA"},{"ANU", "AXA"},{"TIA", "BNE"},{"AUA", "EZE"},{"JFK", "ANU"},{"AXA", "TIA"},{"EZE", "ANU"},{"AUA", "BNE"},{"AUA", "AXA"},{"AUA", "TIA"}};
    String[] output = {"JFK", "ANU", "AUA", "AXA", "ADL", "ANU", "AXA", "AUA", "AXA", "BNE", "ADL", "AXA", "JFK", "ANU", "BNE", "ADL", "TIA", "ANU", "BNE", "ANU", "EZE", "ANU", "EZE", "ANU", "JFK", "AUA", "AXA", "TIA", "AUA", "BNE", "AUA", "EZE", "ANU", "TIA", "BNE", "AUA", "TIA", "BNE", "EZE", "JFK", "TIA", "JFK", "EZE", "AUA", "OOL"};
    assertEquals(Arrays.asList(output), testObject.findItinerary(array2List(input)));
  }

  @Test
  public void failed5() {
    String[][] input = {{"EZE","TIA"},{"EZE","HBA"},{"AXA","TIA"},{"JFK","AXA"},{"ANU","JFK"},{"ADL","ANU"},{"TIA","AUA"},{"ANU","AUA"},{"ADL","EZE"},{"ADL","EZE"},{"EZE","ADL"},{"AXA","EZE"},{"AUA","AXA"},{"JFK","AXA"},{"AXA","AUA"},{"AUA","ADL"},{"ANU","EZE"},{"TIA","ADL"},{"EZE","ANU"},{"AUA","ANU"}};
    String[] output = {"JFK", "AXA", "AUA", "ADL", "ANU", "AUA", "ANU", "EZE", "ADL", "EZE", "ANU", "JFK", "AXA", "EZE", "TIA", "AUA", "AXA", "TIA", "ADL", "EZE", "HBA"};
    assertEquals(Arrays.asList(output), testObject.findItinerary(array2List(input)));
  }
}