package programmers.StackQueue;

import java.util.PriorityQueue;

public class 더맵게 {
	public static void main(String[] args) {
//		int[] scoville = {1, 2, 3, 9, 10, 12};
		int[] scoville = {1, 2, 3};

		int K = 1;

		System.out.println(solution2(scoville, K));
	}

	public static int solution2(int[] scoville, int K) {
		int answer = 0;
        
		PriorityQueue<Integer> q = new PriorityQueue();
        for(int i : scoville){
            q.offer(i);
        }
        int a;
        int b;
        
        
        while(true){
            a = q.poll();
            if (a>=K){
                return answer;
            }
            b = q.poll();
            q.offer(a+(2*b));
            answer++;
            if(q.size() == 1){
                int f = q.poll();
                if(f >= K){
                    return answer;
                }
                return -1;
            }
        }
	}
}

