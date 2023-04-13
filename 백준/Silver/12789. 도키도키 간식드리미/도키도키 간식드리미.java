import java.util.Arrays;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.Stack;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		Stack<Integer> list1 = new Stack<>();
		String ans = "Sad";
		for(int x = 0 ; x < N; x++) {
			list1.push(sc.nextInt());
		}
		Stack<Integer> list2 = new Stack<>();
		int k = 1;
		while(k != N+1) {
			if(!list1.empty() && list1.elementAt(0) == k) {
				list1.remove(0);
				k += 1;
			}
			else if(!list2.empty() && list2.peek() == k) {
				list2.pop();
				k += 1;
			}
			else if(!list1.empty() && list1.elementAt(0) != k) {
				list2.push(list1.elementAt(0));
				list1.remove(0);
			}
			else break;	
		}
		if(list1.empty() && list2.empty()) ans = "Nice";
		System.out.println(ans);
		
	}
}