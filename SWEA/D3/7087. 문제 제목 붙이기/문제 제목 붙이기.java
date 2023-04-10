import java.util.Map;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for(int t = 1; t<= T; t++) {
			int N = sc.nextInt();
			String[] arr = new String[N];
			int ans = 0;
			for(int i = 0 ; i < N ; i++) {
				arr[i] = sc.next();
			}
			char c = 'A';
			int x = 0;
			while(x == 0) {
				x = 1;
				for(int i = 0 ; i < N ; i++) {
					if(arr[i].charAt(0) == c) {
						ans++;
						c++;
						x = 0;
					}
				}
			}
			System.out.println("#" + t + " " + ans);
		}
	}
}