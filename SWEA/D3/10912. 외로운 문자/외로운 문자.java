import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
 
public class Solution {
 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for(int t = 1; t <= T; t++) {
            String A = sc.next();
            String B = "";
            Map<Character, Integer> dic = new HashMap<>();
            for(int i = 0 ; i < A.length(); i++) {
                if(dic.containsKey(A.charAt(i))) {
                    dic.put(A.charAt(i), dic.get(A.charAt(i)) +1);
                }
                else dic.put(A.charAt(i), 1);
            }
            for(Character i : dic.keySet()) {
                if(dic.get(i) %2 == 1) {
                    B += i;
                }
            }
            char[] B_arr = B.toCharArray();
            Arrays.sort(B_arr);
            B = new String(B_arr);
            if(B.equals("")) B = "Good";
            System.out.println("#" + t + " " + B);          
        }
    }
}