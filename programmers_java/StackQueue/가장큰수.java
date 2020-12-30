package programmers.StackQueue;

import java.util.Arrays;
import java.util.Comparator;

public class 가장큰수 {

	public static void main(String[] args) {
//		int[] numbers = {6, 10, 2};
		int[] numbers = {0, 0};
//		int[] numbers = {3, 30, 34, 5, 9, 31, 33 , 7};
		System.out.println(solution(numbers));
	}
	
	public static String solution(int[] numbers) {
		String answer = "";
		String[] nums = new String[numbers.length];
		
		for(int i=0; i<numbers.length; i++)
			nums[i] = numbers[i] + "";
		
		Arrays.sort(nums, new Comparator<String>() {
			@Override
			public int compare(String o1, String o2) {
				return (o2+o1).compareTo(o1+o2);
			}
		});
		for(String i:nums)
			answer += i;
        if(answer.charAt(0) == '0')
        	return "0";
        return answer;
        
    }

}
