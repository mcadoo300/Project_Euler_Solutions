package demo;

public class Main {
	public static void main(String args[]) {
		int upperBound=999*999;
		
		int largestProduct=0;
		while(largestProduct==0) {
			String prodString= String.valueOf(upperBound);
			char[] palCheck=new char[prodString.length()];
			
			//create reverse array of characters
			for(int k=0;k<prodString.length();k++) {
				palCheck[k]=prodString.charAt(prodString.length()-1-k);
			}
			//check if palindrome
			for(int k=0;k<prodString.length();k++) {
				if(palCheck[k]!=prodString.charAt(k))
					k=palCheck.length;
				if(k==(prodString.length()-1)) {//if upperBound is a palindrome check for 3 digit factor
					for(int i=999;i>99;i--) {
						if(upperBound%i==0) {
							int x=upperBound/i;
							String digitCheck= String.valueOf(x);
							if(digitCheck.length()==3)
								largestProduct=upperBound;
						}
					}
				}	
		}
		upperBound--;
	}
		System.out.print(largestProduct);


}
}
//String prodString= String.valueOf(product);
//char[] palCheck=new char[prodString.length()];
//
//for(int k=0;k<prodString.length();k++) {
//	palCheck[k]=prodString.charAt(prodString.length()-1-k);
//}
//for(int k=0;k<prodString.length();k++) {
//	if(palCheck[k]!=prodString.charAt(k))
//		k=palCheck.length;
//	if(k==(prodString.length()-1)) {
//		largestProduct=product;
//		j=1;
//		i=1;
//	}