package demo;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


public class Main {
	public static void main(String args[]) throws FileNotFoundException {
		File myObj= new File("C:\\Users\\Mcado\\eclipse-workspace\\Project_Euler_product_series\\src\\demo\\thousand_digit_num.txt");
		Scanner myReader = new Scanner(myObj);
		int[] intArray = new int[1000];
		String nextChar=null;
		int i=0;
		//populate array of integers
		while(myReader.hasNext()) {
			nextChar=myReader.next();
			for(int j=0;j<nextChar.length();j++) {
				intArray[i]=Character.getNumericValue(nextChar.charAt(j));
				i++;
			}
						
		}
//		int printcount=0;
//		for (int l=0;l<1000;l++)
//		{
//			int f9=49;
//			System.out.print(intArray[l]);
//			if(l==((f9)+50*printcount)) {
//				System.out.print('\n');
//				printcount++;
//				
//			}
//				
//		}
//		System.out.print('\n');

		//brute force all possible products of adjecent integer values
		//output largest product
		long largestProduct=0;
		long prodOfInt=0;//holds values of 13th products
		for(int n=0;n<987;n++) {
			prodOfInt=intArray[n]*intArray[n+1];
			for(int k=n+2;k<(n+13);k++)
				prodOfInt=prodOfInt*intArray[k];
				
			if(prodOfInt>largestProduct) {
				largestProduct=prodOfInt;
				System.out.println(largestProduct);
			}
				
			
		}
			System.out.print("final" + largestProduct);
		
	}

}
