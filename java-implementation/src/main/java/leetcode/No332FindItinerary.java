package leetcode;

import java.util.*;

import static java.util.Map.Entry.comparingByValue;

public class No332FindItinerary {

  public List<String> findItineraryMyIncomplete(List<List<String>> tickets) {
    List<String> answer = new ArrayList<>();
    answer.add("JFK");
    Map<String, Map<Integer, String>> allTickets = new HashMap<>();
    ArrayList<String> uniqueEndList = new ArrayList<>();
    ArrayList<String> endList = new ArrayList<>();

    for (List<String> ticket : tickets) {
      String from = ticket.get(0);
      String to = ticket.get(1);
      Map<Integer, String> destinations = new HashMap<>();

      if (allTickets.containsKey(from)) {
        destinations = allTickets.get(from);
      }
      destinations.put(destinations.size(), to);
      allTickets.put(ticket.get(0), destinations);

      if (!uniqueEndList.contains(to)) {
        uniqueEndList.add(to);
      }
    }

    String from = "JFK";
    while (!allTickets.isEmpty()) {
      System.err.println("allTickets:" + allTickets);
      Map<Integer, String> tos = allTickets.get(from);

      // sort by lexical value
      List<Map.Entry<Integer, String>> toSort = new ArrayList<>(tos.entrySet());
      toSort.sort(comparingByValue());
      Map<Integer, String> sortedTos = new LinkedHashMap<>();
      for (Map.Entry<Integer, String> integerStringEntry : toSort) {
        sortedTos.put(integerStringEntry.getKey(), integerStringEntry.getValue());
      }
      // sort by lexical value

      System.err.println("Check from:" + from + sortedTos);
      String to = "";

      for (Integer i : sortedTos.keySet()) {
        to = sortedTos.get(i);
        System.err.println("handling:" + to);
        if (!allTickets.containsKey(to)) { // still have next stop
          endList.add(0, to);
          allTickets.get(from).remove(i);
        } else { // no next stop, this should equal to final stop
          answer.add(to);
          allTickets.get(from).remove(i);
          break;
        }
      }

      System.err.println("answer:" + answer);
      System.err.println("endList:" + endList);

      if (allTickets.get(from).isEmpty()) {
        allTickets.remove(from);
      }

      // update from for next iteration
      if (!to.isEmpty()) {
        from = to;
      } else {
        break;
      }
    }
    answer.addAll(endList);
    return answer;
  }

  public List<String> findItinerary(List<List<String>> tickets) {
    HashMap<String, List<String>> map = new HashMap<>();
    for (List<String> strings : tickets) {
      if (!map.containsKey(strings.get(0))) {
        map.put(strings.get(0), new ArrayList<>());
      }
      map.get(strings.get(0)).add(strings.get(1));
    }
    return findPathFromS(map, "JFK");
  }

  public List<String> findPathFromS(HashMap<String, List<String>> map, String s) {
    List<String> ret = new ArrayList<>();
    ret.add(s);
    if (map.containsKey(s)) {
      List<String> list = map.get(s);
      Collections.sort(list);
      if (list.size() > 0) {
        for (int i = 0; i < list.size(); i++) {
          String end = list.get(i);
          list.remove(i);
          List<String> tmp = findPathFromS(map, end);
          if (tmp != null) {
            ret.addAll(tmp);
            return ret;
          }
          list.add(i, end);
        }
      }
    }
    for (String key : map.keySet()) {
      if (map.get(key).size() > 0) {
        return null;
      }
    }
    return ret;
  }
}
