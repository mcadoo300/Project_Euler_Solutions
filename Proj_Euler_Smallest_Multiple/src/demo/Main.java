package demo;

public class Main {
	public static void main(String args[]) {
		
		boolean flag = true;
		
		int i=1;
		while (flag) {
			for(int j=1;j<21;j++) {
				if(i%j!=0)
					j=21;
				if(j==20)
					flag=false;
			}
			if(flag)
				i++;
		}
		System.out.print(i);
	}
}
