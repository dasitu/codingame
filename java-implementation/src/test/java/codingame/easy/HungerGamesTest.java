package codingame.easy;

import org.junit.Test;
import utils.StdInOutTestUtils;

public class HungerGamesTest extends StdInOutTestUtils {
  @Test
  public void test1() {
    String[] input = {
      "2", "Bowser", "Mario", "1", "Mario killed Bowser",
    };
    String[] output = {
      "Name: Bowser",
      "Killed: None",
      "Killer: Mario",
      "",
      "Name: Mario",
      "Killed: Bowser",
      "Killer: Winner",
    };
    testWithInputOutput(input, output);
  }

  @Test
  public void aFewMore() {
    String[] input = {
      "5",
      "Ann",
      "Isaac",
      "Mary",
      "Max",
      "Thomas",
      "4",
      "Max killed Isaac",
      "Isaac killed Mary",
      "Mary killed Max",
      "Thomas killed Ann",
    };
    String[] output = {
      "Name: Ann",
      "Killed: None",
      "Killer: Thomas",
      "",
      "Name: Isaac",
      "Killed: Mary",
      "Killer: Max",
      "",
      "Name: Mary",
      "Killed: Max",
      "Killer: Isaac",
      "",
      "Name: Max",
      "Killed: Isaac",
      "Killer: Mary",
      "",
      "Name: Thomas",
      "Killed: Ann",
      "Killer: Winner",
    };
    testWithInputOutput(input, output);
  }

  @Test
  public void serialKillers() {
    String[] input = {
      "4", "Foo", "Bar", "Foobar", "Sam", "1", "Foo killed Bar, Foobar, Sam",
    };
    String[] output = {
      "Name: Bar",
      "Killed: None",
      "Killer: Foo",
      "",
      "Name: Foo",
      "Killed: Bar, Foobar, Sam",
      "Killer: Winner",
      "",
      "Name: Foobar",
      "Killed: None",
      "Killer: Foo",
      "",
      "Name: Sam",
      "Killed: None",
      "Killer: Foo",
    };
    testWithInputOutput(input, output);
  }

  @Test
  public void lineKillers() {
    String[] input = {
      "4",
      "Dude",
      "Him",
      "Killed",
      "This",
      "3",
      "Dude killed Him",
      "Dude killed Killed",
      "Dude killed This",
    };
    String[] output = {
      "Name: Dude",
      "Killed: Him, Killed, This",
      "Killer: Winner",
      "",
      "Name: Him",
      "Killed: None",
      "Killer: Dude",
      "",
      "Name: Killed",
      "Killed: None",
      "Killer: Dude",
      "",
      "Name: This",
      "Killed: None",
      "Killer: Dude",
    };
    testWithInputOutput(input, output);
  }

  @Test
  public void alphabetizeTributes() {
    String[] input = {
      "4",
      "Zulu",
      "Whiskey",
      "Charlie",
      "Alpha",
      "2",
      "Charlie killed Alpha",
      "Whiskey killed Charlie, Zulu",
    };
    String[] output = {
      "Name: Alpha",
      "Killed: None",
      "Killer: Charlie",
      "",
      "Name: Charlie",
      "Killed: Alpha",
      "Killer: Whiskey",
      "",
      "Name: Whiskey",
      "Killed: Charlie, Zulu",
      "Killer: Winner",
      "",
      "Name: Zulu",
      "Killed: None",
      "Killer: Whiskey",
    };
    testWithInputOutput(input, output);
  }

  @Test
  public void alphabizeVictims() {
    String[] input = {
      "10",
      "Marco",
      "Sophie",
      "Diamond",
      "Lester",
      "Steve",
      "Hawkings",
      "Harry",
      "Potter",
      "Michael",
      "Scott",
      "6",
      "Marco killed Sophie, Diamond",
      "Sophie killed Lester",
      "Sophie killed Scott",
      "Michael killed Harry",
      "Harry killed Potter",
      "Potter killed Hawkings, Steve, Marco",
    };
    String[] output = {
      "Name: Diamond",
      "Killed: None",
      "Killer: Marco",
      "",
      "Name: Harry",
      "Killed: Potter",
      "Killer: Michael",
      "",
      "Name: Hawkings",
      "Killed: None",
      "Killer: Potter",
      "",
      "Name: Lester",
      "Killed: None",
      "Killer: Sophie",
      "",
      "Name: Marco",
      "Killed: Diamond, Sophie",
      "Killer: Potter",
      "",
      "Name: Michael",
      "Killed: Harry",
      "Killer: Winner",
      "",
      "Name: Potter",
      "Killed: Hawkings, Marco, Steve",
      "Killer: Harry",
      "",
      "Name: Scott",
      "Killed: None",
      "Killer: Sophie",
      "",
      "Name: Sophie",
      "Killed: Lester, Scott",
      "Killer: Marco",
      "",
      "Name: Steve",
      "Killed: None",
      "Killer: Potter",
    };
    testWithInputOutput(input, output);
  }
}
