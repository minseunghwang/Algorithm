package programmers.StackQueue;

import java.util.ArrayList;
import java.util.List;

public class 기능개발 {
	public static void main(String[] args) {
		Solution sol = new Solution();
//		int[] progresses = {93, 30, 55};
		int[] progresses = {95, 90, 99, 99, 80, 99};
//		int[] speeds = {1, 30, 5};
		int[] speeds = {1, 1, 1, 1, 1, 1};
		
		System.out.println(sol.solution(progresses, speeds));
	}
}

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
    	int[] answer;
    	List<Integer> list = new ArrayList<>();
        int n = 0;
        while(n<progresses.length){
        	int ans = 0;
        	while(progresses[n] < 100) {
	        	for(int i=0; i<progresses.length; i++) {
	        		progresses[i] += speeds[i];
	        	}
        	}
        	for(int i:progresses) {
        	}
        	for(int i=n; i<progresses.length; i++) {
        		if(progresses[i] < 100) {
        			break;
        		}
        		ans++;
        	}
            list.add(ans);
            n += ans;
        }
        
        answer = new int[list.size()];
        
        for(int i=0; i<list.size(); i++) {
        	answer[i] = list.get(i);
        }
        return answer;
    }
}
