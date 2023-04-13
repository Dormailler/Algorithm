import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Main{

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		List<Integer> arr = new LinkedList<>();
		for(int i = 1 ; i <= N ; i ++ ) {
			arr.add(i);
		}
		List<Integer> arr2 = new LinkedList<>();
		for(int x = 1 ; x <= N; x++) {
			arr2.add(sc.nextInt());
		}
		int k = 0;
		while(!arr.isEmpty()) {
			k %= arr.size();
			while(k<0) {
				k += arr.size();
			}
			System.out.print(arr.remove(k) + " ");
			int p_k = arr2.remove(k);
			if(p_k > 0) k += p_k - 1;
			else k += p_k;
			
		}
	}

}