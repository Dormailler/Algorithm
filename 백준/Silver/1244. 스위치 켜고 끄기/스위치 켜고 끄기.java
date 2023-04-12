import java.util.LinkedList;
import java.util.Scanner;

public class Main{

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int arr[] = new int[N];
		for(int t = 0 ; t < N ; t++) {
			arr[t] = sc.nextInt();
		}
		int student_num = sc.nextInt();
		for(int i = 0; i < student_num; i++) {
			int sex = sc.nextInt();
			int switch_num = sc.nextInt();
			if(sex == 1) {
				for(int j = 0; j< N; j++) {
					if((j+1)%switch_num == 0) {
						if(arr[j] == 0) arr[j] = 1;
						else arr[j] = 0;
					}
				}
			}
			else {
				int index = 1;
				while(true) {
					if(switch_num + index  > N || switch_num - index <= 0 ) break;
					if(arr[switch_num-1+index] == arr[switch_num - 1 - index]) index += 1;
					else break;
				}
				for(int j = switch_num-index ; j <= switch_num + index-2 ; j++ ) {
					if(arr[j] == 0 ) arr[j] = 1;
					else arr[j] = 0;
				}
			}
		}
		for(int x = 0; x< N; x++) {
			if(x != 0 && x %20 == 0) System.out.println();
			System.out.print(arr[x] + " ");
		}
	}
}
