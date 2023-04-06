import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int t = 1; t<= T; t++) {
			int num = 0;
			int is = 0;
			String s = sc.next();
			char[] charArray = s.toCharArray();
			for(char c : charArray){
			    if(c == '1' && is==0) {
			    	num++;
			    	is = 1;
			    }
			    if(c=='0' && is == 1) {
			    	num++;
			    	is = 0;
			    }
			}
			System.out.println("#" + t + " " + num);
		}
	}
}