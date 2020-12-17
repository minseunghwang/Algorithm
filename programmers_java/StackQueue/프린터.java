package programmers.StackQueue;

import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;

public class 프린터 {

	public static void main(String[] args) {

//		int[] priorities = {2,1,3,2};
		int[] priorities = {1, 1, 9, 1, 1, 1};
		int location = 0;
		
		System.out.println(solution(priorities, location));
		

	}
	
    public static int solution(int[] priorities, int location) {
        int answer = 1;
        
        Queue<Integer> q = new LinkedList<Integer>();
        for (int i:priorities) {
        	q.add(i);
        }
        int max_ = Collections.max(q);
        
        while(!q.isEmpty()) {
        	System.out.println(q.toString() + " , " + location);
        	int now = q.poll();
        	if(now == max_) {
        		if(location == 0) {
        			return answer;
        		}
        		location--;
        		answer++;
        		max_ = Collections.max(q);
        	} else {
        		q.add(now);
        		location--;
        		if(location < 0) {
        			location = q.size()-1;
        		}
        	}
        }
        
        return answer;
    }
}
