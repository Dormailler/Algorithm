import java.util.Scanner;

public class Solution{

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int i = 1; i <= T; i++) {
			int N = sc.nextInt();
			String[] arr = new String[N];
			String[] ans = new String[N];
			for(int j = 0 ; j < N ; j++) {
				arr[j] = sc.next();
			}
			for(int j = 0 ; j < N ; j+=2) {
				ans[j] = arr[j/2];
			}
			for(int j = 1 ; j < N ; j+=2) {
				ans[j] = arr[j/2+N/2+N%2];
			}
            System.out.print("#" + i + " ");
			for(int j = 0 ; j < N ; j+=1) {
				System.out.print(ans[j] +" ");
			}
			System.out.println();
		}
	}
}