import java.util.Arrays;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int t = 1; t <= T; t++) {
			int[] arr = new int[10];
			int[] arr1 = {0,1,2,3,4,5,6,7,8,9};
			Arrays.fill(arr, -1);
			int ans = 0;
			int N = sc.nextInt();
			int k = N;
			while(!Arrays.equals(arr, arr1)) {
				int M = N;
				while(M>0) {
					arr[M%10] = M%10;
					M /= 10;
				}
				ans++;
				N += k; 
			}
			System.out.println("#" + t + " " + ans * k);		
		}
	}
}