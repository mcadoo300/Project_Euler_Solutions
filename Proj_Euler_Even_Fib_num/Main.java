package demo;

public class Main {
	public static void main(String args[])
    {  
		int sum=0;
		//initalize first and"second" fib number to be 1
		int fibNum=1;
		int fibNew=1;
		int fibPrev=1;
		
		while(fibNum<4000000) {
			
			fibNew=fibPrev+fibNum;
			fibPrev=fibNum;
			fibNum=fibNew;
			
			if(fibNum%2==0)
				sum=fibNum+sum;
		}
		System.out.print(sum);
		
    }
}
