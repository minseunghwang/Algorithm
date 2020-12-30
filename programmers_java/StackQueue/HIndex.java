package programmers.StackQueue;

import java.util.Arrays;

public class HIndex {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int[] citations = {3, 0, 6, 1, 5};
		System.out.println(solution(citations));

		
	}
	
    public static int solution(int[] citations) {
    	int answer = 0;
        Arrays.sort(citations);
        int h = citations.length;
        while(true) {
        	if(citations[h-1] == h) {
        		answer = h;
        		break;
        	}
        	h--;
        	System.out.println(0);
        }
        return answer;
    }

}

