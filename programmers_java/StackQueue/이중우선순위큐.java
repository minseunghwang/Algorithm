package programmers.StackQueue;

import java.util.ArrayList;
import java.util.List;

public class 이중우선순위큐 {

	public static void main(String[] args) {
		String[] operations = {"I 16","D 1", "D -1"};
//		String[] operations = {"I 7","I 5","I -5","D -1"};	
		System.out.println(solution(operations));
	}
	
    public static int[] solution(String[] operations) {
        int[] answer = {};
        
        List<Integer> list = new ArrayList<Integer>();
        String[] tmp;
        for(String i:operations) {
        	tmp = i.split(" ");
        	if("I".equals(tmp[0])) {
        		list.add(Integer.parseInt(tmp[1]));
        		list.sort(null);
        	} else if("D".equals(tmp[0]) && list.size() > 0){
        		if("1".equals(tmp[1])) {
        			list.remove(list.size()-1);
        		} else {
        			list.remove(0);
        		}
        	} else {
        		break;
        	}
        }
        System.out.println(list);
        if(list.size() == 0) {
        	answer = new int[] {0,0};
        } else {
        	answer = new int[] {list.get(list.size()-1), list.get(0)};
        }
        
        return answer;
    }
}
