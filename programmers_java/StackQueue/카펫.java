package programmers.StackQueue;

import java.util.ArrayList;
import java.util.List;

public class 카펫 {

	public static void main(String[] args) {
		int brown = 24;
		int yellow = 24;
		System.out.println(solution(brown, yellow));
		
	}
	
    public static int[] solution(int brown, int yellow) {
        int[] answer = {0,0};
        
        int now = brown+yellow;
        List<Integer> list = new ArrayList<Integer>();
        for(int i=1; i<=now; i++) {
        	if(now%i==0) {
        		list.add(i);
        	}
        }
        if(list.size()%2 == 0) {
        	answer[0] = list.get(list.size()/2);
        	answer[1] = list.get(list.size()/2-1);
        } else {
        	answer[0] = list.get(list.size()/2);
        	answer[1] = list.get(list.size()/2);
        }
        
        return answer;
    }
    
    public static int getGCD(int a, int b) {
    	if (b>a) {
    		int temp;
    		temp = a;
    		a = b;
    		b = temp;
    	}
    	
    	int r=1;
    	while(r>0) {
    		r = a%b;
    		a=b;
    		b=r;
    	}
    	
    	return a;
    }

}
