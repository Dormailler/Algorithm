import java.util.Scanner;
 
public class Solution {
 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] dy = {1,0,-1,0};
        int[] dx = {0,1,0,-1};
        for(int A = 1; A<= n; A++) {
            int N = sc.nextInt();
            int [][] arr = new int[N][N];
            arr[0][0] = 1;
            int a = 1;
            int x = 0;
            int y = 0;
            System.out.println("#"+A);
            while(a < N*N) {
                for(int j = 0 ; j<4; j++) {
                    while((y + dy[j]>-1)&&(x + dx[j]>-1)&&(x + dx[j]<N)&&(y+dy[j] < N)&&arr[x + dx[j]][y+dy[j]] == 0){
                        x += dx[j];
                        y += dy[j];
                        a += 1;
                        arr[x][y] = a;
                    }
                }
            }
            for (int i = 0; i < arr.length; i++) {
                   for (int j = 0; j < arr[i].length; j++) {
                       System.out.print(arr[i][j] + " ");
                   }
                   System.out.println();
            }
        }
    }
}