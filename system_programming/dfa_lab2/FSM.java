import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Set;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Queue;
import java.util.LinkedList;


public class FSM {
    Set<Character> alphabet;
    Set<Integer> states;
    Integer initial;
    Set<Integer> finals;
    Map<Integer, Map<Character, Set<Integer>>> transitions;

    FSM()
    {
        alphabet = new HashSet<>();
        states = new HashSet<>();
        initial = 0;
        finals = new HashSet<>();
        transitions = new HashMap<>();
    }

    FSM(File file)
    {
        try
        {
            Scanner sc = new Scanner(file);
            String[] alphs = sc.nextLine().split("\\s");
            alphabet = new HashSet<>();
            for (int i = 0; i < alphs.length; i++){
                alphabet.add(Character.valueOf(alphs[i].charAt(0)));
            }

            int numberOfStates = sc.nextInt();
            states = new HashSet<>(numberOfStates);
            for (int i = 0; i < numberOfStates; i++){
                states.add(i);
            }

            initial = sc.nextInt();


            int amount_fin_states = sc.nextInt();
            finals = new HashSet<>(amount_fin_states);
            for (int i = 0; i < amount_fin_states; i++) {
                finals.add(sc.nextInt());
            }

            transitions = new HashMap<>(numberOfStates);
            for (Integer state : states) {
                transitions.put(state, new HashMap<>());
            }
            int j = 0;
            while (sc.hasNext()) {
                Integer fromState = sc.nextInt();
                Character viaLetter = sc.next().charAt(0);
                Integer toState = sc.nextInt();
                if (!transitions.get(fromState).keySet().contains(viaLetter)){
                    transitions.get(fromState).put(viaLetter, new HashSet<>());
                }
                transitions.get(fromState).get(viaLetter).add(toState);
            }
        }
        catch (FileNotFoundException ex) {
            System.out.println("Invalid file");
        }
    }
    
    private Map<Integer, Boolean> bfsFromStates(Set<Integer> fromStates) {
        Map<Integer, Boolean> used = new HashMap<>();
        for (Integer state : states) {
            used.put(state, false);
        }

        Queue<Integer> statesq = new LinkedList<>(fromStates);
        while (!statesq.isEmpty()) {
            Integer fromState_ = statesq.peek();
            used.put(fromState_, true);

            for (Character viaLetter : transitions.get(fromState_).keySet()) {
                for (Integer toState : transitions.get(fromState_).get(viaLetter)) {
                    if (!used.get(toState)) {
                        statesq.add(toState);
                    }
                }
            }

            statesq.poll();
        }
        return used;
    }
    
    Set<Integer> getReachableFromStates(Set<Integer> fromStates) {
        Map<Integer, Boolean> used = bfsFromStates(fromStates);
        Set<Integer> visited = new HashSet<>();
        for (Integer state : used.keySet()) {
            if (used.get(state)) {
                visited.add(state);
            }
        }
        return visited;
    }

    private Set<Integer> getReachableFromState(Integer fromState) {
        Set<Integer> fromStates = new HashSet<>();
        fromStates.add(fromState);
        return getReachableFromStates(fromStates);
    }

    Set<Integer> getReachable() {
        return getReachableFromState(initial);
    }

    Set<Integer> processWordFromStates(String word, Set<Integer> fromStates) {
        Set<Integer> states_ = new HashSet<>(fromStates);
        for (Character viaLetter : word.toCharArray()) {
            System.out.println("viaLetter: " + viaLetter);
            Set<Integer> nextStates = new HashSet<>();
            for (Integer lett: states_) {
                System.out.println("Cur states: " + lett);
            }
            for (Integer fromState_ : states_) {
                if (transitions.get(fromState_).containsKey(viaLetter)){
                    nextStates.addAll(transitions.get(fromState_).get(viaLetter));
                }
            }
            states_ = new HashSet<>(nextStates);

        }
        return states_;
    }

}
