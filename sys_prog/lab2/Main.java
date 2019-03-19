import java.io.File;
import java.io.FileNotFoundException;
import java.util.Objects;
import java.util.Scanner;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        try {
            System.out.format("Please enter the name of file with NFA: ");
            String pathname = sc.next();

            NFA nfa = new NFA(pathname);

            Set<Integer> reachableStates = nfa.getReachable();

            System.out.format("Enter w0: ");
            String w0 = sc.next();
            Set<Integer> afterW0 = nfa.processWordFromStates(w0, reachableStates);

            Set<Integer> reachableFromAfterW0 = nfa.getReachableFromStates(afterW0);
            reachableFromAfterW0.retainAll(nfa.finalStates);
            if (!reachableFromAfterW0.isEmpty()) {
                System.out.println("There DOES exist w1, w2 such that w1w0w2 is acceptable.");
            } else {
                System.out.println("There does NOT exist w1, w2 such that w1w0w2 is acceptable.");
            }
        } catch (FileNotFoundException ex) {
            System.out.println("Invalid file pathname");
        }

        sc.close();
    }

    static class CompleteStepNotPossibleException extends Exception {
        private static final long serialVersionUID = 1L;

        CompleteStepNotPossibleException(String message) {
            super(message);
        }
    }

    // private static <T> void printIterableInline(Iterable<T> iterable, String indent, String separator) {
    //     System.out.print(indent);
    //     for (T t : iterable) {
    //         System.out.print(t + separator);
    //     }
    //     System.out.println();
    // }

    static Scanner getScanner(String pathname) throws FileNotFoundException {
        File file = new File(pathname);

        if (!file.exists()) {
            System.out.format("File '%s' does not exist.%n", pathname);
        }

        if (!file.canRead()) {

            System.out.format("Cannot read file '%s'.%n", pathname);
        }

        return new Scanner(file);
    }
}
