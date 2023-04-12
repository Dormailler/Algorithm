import java.util.LinkedList;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		
		LinkedList<Integer> list = new LinkedList<>();
		for(int i = 1; i <= N; i++) {
			list.add(i);
		}
		
		StringBuilder sb = new StringBuilder();
        sb.append("<");
        
        int rear = 0;
        while (list.size() > 1) {
            rear = (rear + K - 1) % list.size();
            sb.append(list.remove(rear)+", ");
        }
        sb.append(list.remove()+">");
        System.out.println(sb.toString());
	}

}