import java.util.ArrayList;
import java.util.*;
import javax.xml.transform.*;

class Solution {
	
	public static int CountBinarySubStrings(String s) {
		// step1.convert the String to charArray
		s = s + "2";
		char[] charArray = s.toCharArray();
		//System.out.println(charArray);
		// step2.convert the charArray to countArray
		ArrayList<Integer> countChar = new ArrayList<Integer>();
		int sameNum = 1;
		int result = 0;
		for(int i=1; i<charArray.length; i++){
			if(charArray[i-1] == charArray[i]){
				sameNum++;
			}else{
				countChar.add(sameNum);
				sameNum = 1;
			}
		}
		
		// test the whether the countChar is right
		Iterator<Integer> it1 = countChar.iterator();
		while (it1.hasNext()) {
			System.out.println(it1.next());
		}
		// step3.count the final result through the countArray
		for(int i=0; i<countChar.size()-1; i++){
			result += Math.min(countChar.get(i), countChar.get(i+1));
		}
		return result;
		
	}
	
	public static void main(String[] args){
		int result = CountBinarySubStrings("00110011");
		System.out.println(result);
	}
}