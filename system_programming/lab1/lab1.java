//variant: 9
//Знайти ті слова які мають найбільшу кількість різних літер, 
//тобто літери, що повторюються у слові, не враховувати.

import java.io.*; 
import java.util.*;
import java.util.regex.Pattern;
import java.math.*;

class Wordprocessing
{
	public static int different_letters(String word)
	{
		int word_len = word.length();
		Map<Character, Integer> dif_chars = new HashMap<Character, Integer>();
		for (int i = 0; i < word_len; ++i)
			dif_chars.put(word.charAt(i), 0);
		return dif_chars.size();
	}

	public static void print_words()
	{ 
		File file = new File("file1.txt");
    	try
		{
        	Scanner sc = new Scanner(file);
			sc.useDelimiter("\\s|\\.|\\_|\\+|\\-|\\!|\\@|\\#|\\?|\\$|\\,|\\<|\\>|\\^|\\&|\\*|\\(|\\)|\\[|\\]|'|\\\"|\\~|\\|"); 
			ArrayList<String> longest_words = new ArrayList<String>();
			int max_letters = 1;
			while (sc.hasNext())
			{
				String word = sc.next();
				ArrayList<String> words = new ArrayList<String>();
				words.add(word.substring(0, Math.min(30, word.length())));
				while (word.length() > 30)
				{
					words.add(word.substring(30, Math.min(30, word.length())));
					word = word.substring(30);
				}
				for (int j = 0; j < words.size(); j++)
				{
					int cur_letters =  different_letters(words.get(j));
					if (cur_letters > max_letters)
					{
						max_letters = cur_letters;
						longest_words.clear();
						longest_words.add(words.get(j));
					}
					else if (cur_letters == max_letters)
						longest_words.add(words.get(j));
				}
			}
			System.out.println("Max number of different letters: " + max_letters);
			int size = longest_words.size();
			for (int i = 0; i < size; i++)
				System.out.println(longest_words.get(i));
			sc.close();
		}
		catch (FileNotFoundException e) {
        	e.printStackTrace();
    	}
	}

	public static void main(String[] args) 
	{ 
		print_words();
	} 
} 

