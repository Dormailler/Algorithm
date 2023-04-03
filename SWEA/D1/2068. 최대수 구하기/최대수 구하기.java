import java.util.Map;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
				
		for(int i = 0; i< num; i++) {
			int answer = 0;
			for(int j = 0; j<10; j++) {
				int a = sc.nextInt();
				if(a > answer) {
					answer = a;
				}
			}
			System.out.println("#" + (i+1) + " " +  answer);
			
		}
	}
}