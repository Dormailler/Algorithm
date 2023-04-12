import java.util.LinkedList;
import java.util.Scanner;

public class Main{

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		LinkedList<Integer> list = new LinkedList<>();
		for(int i = N; i >= 1; i--) {
			list.add(i);
		}
        while (list.size() > 1) {
            list.removeLast();
            if(list.size() == 1) break;
            list.addFirst(list.removeLast());
        }
        System.out.println(list.get(0));
	}
}