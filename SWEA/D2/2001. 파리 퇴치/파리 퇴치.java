import java.util.Arrays;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int k = 1; k <= T; k++) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			int[][] arr = new int[N][N];
			int max = 0;
			for(int i = 0 ; i < N ; i++) {
				for(int j = 0 ; j < N ; j++) {
					arr[i][j] = sc.nextInt();
				}
			}
			for(int y = 0 ; y < N-M+1; y++) {
				for(int x = 0 ; x < N-M+1; x++){
					int sum = 0;
					for(int i = y ; i < M+y ; i++) {
						for(int j = x ; j < M+x ; j++) {
							sum += arr[i][j];
						}
					}
					max = Math.max(max, sum);
				}
			}
			System.out.println("#" + k + " " + max);
		}
	}
}