class Solution {
	
	public static int CountBinarySubStrings(String s) {
		String str1 = "";
		String str2 = "";
		int count = 0;
		int sLength = s.length();
		for(int i=1; i<= sLength/2; i++){
			str1 = "0" + str1 + "1";
			str2 = "1" + str2 + "0";
			int index1 = 0;
			int index2 = 0;
			while(s.indexOf(str1, index1) != -1){
				count ++;
				index1 = s.indexOf(str1, index1) + 1;
			}
			
			while(s.indexOf(str2, index2) != -1){
				count ++;
				index2 = s.indexOf(str2, index2) + 1;
			}
		}
		return count;
	}
	
	public static void main(String[] args){
		int result = CountBinarySubStrings("00110011");
		System.out.println(result);
	}
}