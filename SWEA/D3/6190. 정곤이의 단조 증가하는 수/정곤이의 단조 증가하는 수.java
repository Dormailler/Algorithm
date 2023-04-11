import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int t = 1; t <= T; t++) {
			int N = sc.nextInt();
			int[] A = new int[N];
			int max = 0;
			for(int i = 0 ; i < N; i++) {
				A[i] = sc.nextInt();
			}
			for(int i = 0 ; i < N; i++) {
				for(int j = 1 ; i+j < N; j++) {
					String ab = Integer.toString(A[i] * A[i+j]);
					int s= 0;
					for(int k = 0 ; k < ab.length()-1; k++) {
						if((int)(ab.charAt(k)) > (int)ab.charAt(k+1)) s = 1;
					}
					if(s == 0) max = Math.max(max, Integer.parseInt(ab));
				}
			}
			if(max==0) max=-1;
			System.out.println("#" + t + " " + max);			
		}
	}
}