import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int i = 1; i <= T; i++) {
			int N = sc.nextInt();
			int[][] arr = new int[N][N];
			int sum = 0;
			for(int j = 0; j < N; j++) {
				String s = sc.next();
				for(int k = 0 ; k < N ; k++) {
					arr[j][k] = (int)s.charAt(k) - '0';
				}
			}
			for(int j = 0; j < N; j++) {
				if(j > N/2) {
					for(int k = N/2 - (N-j-1); k <= N/2 + (N-j-1) ; k++) {
						sum += arr[j][k];
					}
				}
				else {
					for(int k = N/2 - j; k <= N/2 + j ; k++) {
						sum += arr[j][k];
					}
				}
			}
			System.out.println("#" + i + " " + sum);
		}
	}
}
