import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Set;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class FSM {
    Set<Character> alphabet;
    Set<Integer> states;
    Character initial;
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
            for (int i = 0; i < alphs.length; i++){
                alphabet.add(Character.valueOf(alphs[i].charAt(0)));
            }

            String[] states_line = sc.nextLine().split("\\s");
            for (int i = 0; i < alphs.length; i++){
                states.add(Integer.valueOf(alphs[i]));
            }

            String in = sc.nextLine();
            initial = Character.valueOf(in.charAt(0));
            int amount_fin_states = sc.nextInt();
            for (int i = 0; i < amount_fin_states; i++) {
                finals.add(sc.nextInt());
            }

            int j = 0;
            while (sc.hasNext()) {
                transitions
            }

            
        }
        catch (FileNotFoundException ex) {
            System.out.println("Invalid file pathname");
        }
    }
}