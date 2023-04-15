import java.util.Map;
import java.util.Scanner;
 
public class Solution {
 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
                 
        for(int i = 1; i<= num; i++) {
            String answer = "";
            int a = sc.nextInt();
            int b = sc.nextInt();
            if(a > b) answer = ">";
            else if(a == b) answer = "=";
            else answer = "<";
            System.out.println("#" + i + " " +  answer);
             
        }
    }
}