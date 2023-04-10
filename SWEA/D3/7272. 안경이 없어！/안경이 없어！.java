import java.util.Arrays;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int t = 1; t <= T; t++) {
			String arr1 = sc.next();
			String arr2 = sc.next();
			String zero = "CEFGHIJKLMNSTUVWXYZ";
			String one = "ADOPQR";
			String ans = "DIFF";
			if(arr1.length() == arr2.length()) {
				for(int i = 0 ; i < arr1.length(); i++) {
					if(zero.contains(Character.toString(arr1.charAt(i)))) arr1 = arr1.replaceAll(Character.toString(arr1.charAt(i)),"0");
					if(one.contains(Character.toString(arr1.charAt(i)))) arr1 = arr1.replaceAll(Character.toString(arr1.charAt(i)),"1");
					if(zero.contains(Character.toString(arr2.charAt(i)))) arr2 = arr2.replaceAll(Character.toString(arr2.charAt(i)),"0");
					if(one.contains(Character.toString(arr2.charAt(i)))) arr2 = arr2.replaceAll(Character.toString(arr2.charAt(i)),"1");
				}
			}
			if(arr1.equals(arr2)) ans = "SAME";
			System.out.println("#" + t + " " + ans);		
		}
	}
}