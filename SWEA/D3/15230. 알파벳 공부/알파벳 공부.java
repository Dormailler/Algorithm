import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int t = 1; t <= T; t++) {
			String A = sc.next();
			int ans = 0;
			char c = 'a';
			for(int i = 0 ; i < A.length(); i++) {
				if(A.charAt(i) == c) {
					ans++;
					c++;
				}
				else{
					break;
				}
			}
			System.out.println("#" + t + " " + ans);			
		}
	}
}