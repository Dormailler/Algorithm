import java.util.Scanner;

public class Solution{

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		for(int i = 1; i<=N; i++) {
			String si = Integer.toString(i);
			char[] ca = si.toCharArray();
			int is = 0;
			for(char c : ca) {
				if(c == '3' || c == '6' || c == '9') {
					System.out.print("-");
					is = 1;
				}
			}
			if(is == 0) System.out.print(i);
			System.out.print(" ");
		}
	}
}