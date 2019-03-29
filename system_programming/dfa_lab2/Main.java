import java.io.File;
import java.util.Scanner;

import javax.lang.model.util.ElementScanner6;

import java.io.FileNotFoundException;

public class Main{

    public static void main(String[] args)
    {
        if (args.length != 0)
            RtFiniteStateMachine fsm = FSMBuilder::build(args[0]);
        else
            System.out.println("Please, enter filename with finite state machine");
        

        

        
    }
}