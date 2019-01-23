import java.io.*; 
import java.util.*;
import java.util.regex.Pattern;
class Wordprocessing
{

	public static void read()
	{ 
		Scanner sc = new Scanner("stepik_algo.cpp"); //throw exception 
		sc.useDelimiter("\\s|\\.|\\_"); 
		while (sc.hasNext())
			System.out.println(sc.next()); 
		sc.close();
	}
	public static void main(String[] args) 
	{ 
		read();
	} 
} 
