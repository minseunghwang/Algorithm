package programmers.StackQueue;

import java.util.ArrayList;
import java.util.List;

public class 체육복 {

	public static void main(String[] args) {

		int n = 5;
		int[] lost = {2,4};
		int[] reverse = {5};
		System.out.println(solution(n,lost,reverse));
	}
	
	public static int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        answer = n;

        int[] all = new int[n];
        for(int i:reserve) {
        	all[i-1]++;
        }
        for(int i:lost) {
        	all[i-1]--;
        }
        for(int i=0;i<all.length;i++) {
        	if (all[i] == -1) {
        		if(i != 0 && all[i-1] == 1) {
        			all[i-1]--;
        			all[i]++;
        		} else if(i != all.length-1 && all[i+1]==1) {
        			all[i+1]--;
        			all[i]++;
        		}
        	}
        }
        for(int i:all) {
        	if(i==-1) {
        		answer--;
        	}
        }
        
        
        
        return answer;
    }

}
