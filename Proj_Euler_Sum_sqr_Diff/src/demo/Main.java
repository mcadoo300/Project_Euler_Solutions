package demo;

public class Main {
	public static void main(String args[]) {
		int sqrSum=0; //square of sum
		int sumOfSqr=0; //sum of square
		
		for(int i=0;i<11;i++) {
			sqrSum=i+sqrSum;
			sumOfSqr=(i*i)+sumOfSqr;
		}
		System.out.print((sqrSum*sqrSum)-sumOfSqr);
	}

}
