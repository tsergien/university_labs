import java.io.File;
import java.util.Scanner;
import javax.lang.model.util.ElementScanner6;
import java.io.FileNotFoundException;
import java.util.Set;

public class Main{

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        // System.out.format("Please enter the name of file with FSM: ");
        // String pathname = sc.next();

        String pathname = "automat1";
        File file = new File(pathname);
        FSM fsm = new FSM(file);

        Set<Integer> reachableStates = fsm.getReachable();
        System.out.println("Reachable states: ");
        for (Integer st: reachableStates){
            System.out.println(st);
        }
        
        System.out.format("Enter w0: ");
        String w0 = sc.next();
        Set<Integer> afterW0 = fsm.processWordFromStates(w0, reachableStates);
        System.out.println("After w0");
        for (Integer st: afterW0){
            System.out.println(st);
        }
        Set<Integer> reachableFromAfterW0 = fsm.getReachableFromStates(afterW0);
        System.out.println("Reachable after fromw0");
        for (Integer st: reachableFromAfterW0){
            System.out.println(st);
        }
        reachableFromAfterW0.retainAll(fsm.finals);
        if (reachableFromAfterW0.isEmpty()) {
            System.out.println("-----> There does NOT exist w1, w2 such that w1w0w2 is acceptable.");
        } else {
            System.out.println("-----> There DOES exist w1, w2 such that w1w0w2 is acceptable.");
        }
        sc.close();      

        
    }
}