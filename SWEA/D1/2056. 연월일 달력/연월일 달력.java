import java.util.Map;
import java.util.Scanner;
 
public class Solution {
 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
                 
        for(int i = 1; i<= num; i++) {
            String a = sc.next();
            String year = a.substring(0,4);
            String month = a.substring(4,6);
            String day = a.substring(6,8);
            int i_month = Integer.parseInt(month);
            int i_day = Integer.parseInt(day);
            if(0< i_month && i_month <= 12) {
                switch(i_month) {
                case 1:
                case 3:
                case 5:
                case 7:
                case 8:
                case 10:
                case 12:
                    if(0<i_day && i_day <= 31) {
                        System.out.println("#" + i + " " + year + "/" + month + "/" + day);
                    }
                    else System.out.println("#" + i + " " + "-1");
                    break;
                case 2:
                    if(0<i_day && i_day <= 28) {
                        System.out.println("#" + i + " " + year + "/" + month + "/" + day);
                    }
                    else System.out.println("#" + i + " " + "-1");
                    break;
                default:
                    if(0<i_day && i_day <= 30) {
                        System.out.println("#" + i + " " + year + "/" + month + "/" + day);
                    }
                    else System.out.println("#" + i + " " + "-1");
                }
                continue;
            }
            System.out.println("#" + i + " " + "-1");
        }
    }
}