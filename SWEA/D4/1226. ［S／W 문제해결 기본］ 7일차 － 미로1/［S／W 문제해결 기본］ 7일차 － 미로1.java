import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Solution {
	
	static int[] dr = {-1,0,1,0};
	static int[] dc = {0,1,0,-1};
	
	static class Loc{
		int r;
		int c;
		public Loc(int r, int c) {
			this.r = r;
			this.c = c;
		}
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		for(int tc = 1; tc <= 10; tc ++) {
			int t = sc.nextInt();
			char[][] map = new char[16][16];
			boolean[][] visited = new boolean[16][16];
			for(int i = 0 ; i <16; i++) {
				map[i] = sc.next().toCharArray();
			}
			
			Queue<Loc> queue = new LinkedList<>();
			int answer = 0;
			queue.add(new Loc(1,1)); // 시작좌표
			outer : while(!queue.isEmpty()) {
				Loc now = queue.poll();
				for(int i = 0 ; i < 4; i++) {
					int nr = now.r + dr[i];
					int nc = now.c + dc[i];
					if(nr >= 0 && nr < 16 && nc >= 0 && nc < 16) {
						if(map[nr][nc] != '1' && !visited[nr][nc]) {
							queue.add(new Loc(nr,nc));
							visited[nr][nc] = true;
							
							if(map[nr][nc] == '3') {
								answer = 1;
								break outer;
							}
						}
					}
				}
			}
			System.out.println("#" + tc + " " + answer);
		}		
	}
}