package demo;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws FileNotFoundException {
		File myObj= new File("C:\\Users\\Mcado\\eclipse-workspace\\Proj_Euler_Largest_grid_product\\src\\demo\\grid.txt");
		Scanner myReader = new Scanner(myObj);
		String intVal=null;
		int[][] grid1 = new int[20][20];
		for(int i=0;i<20;i++)
		{
			for(int j=0;j<20;j++) 
			{
				grid1[i][j]=myReader.nextInt();
			}
		}
		
		long largestProd=0;
		long prodOfInt=0;
		//check horizontal
		for(int row=0;row<20;row++) {
			for(int colStart=0;colStart<16;colStart++) {
				prodOfInt=grid1[row][colStart]*grid1[row][colStart+1];
				for(int adjNum=(colStart+2);adjNum<(colStart+4);adjNum++){
					prodOfInt=prodOfInt*grid1[row][adjNum];
					
				}
				if(prodOfInt>largestProd)
					largestProd=prodOfInt;
			}//end of row search
		}//end of horizontal search
		
		
		//check vertically
		for(int row=0;row<16;row++) {
			for(int colStart=0;colStart<20;colStart++) {
				prodOfInt=grid1[row][colStart]*grid1[row+1][colStart];
				for(int adjNum=(row+2);adjNum<(row+4);adjNum++){
					prodOfInt=prodOfInt*grid1[adjNum][colStart];
					
				}
				if(prodOfInt>largestProd)
					largestProd=prodOfInt;
			}//end of col search
		}//end of verticle search
		
		
		//check right diagonal
		for(int row=0;row<16;row++) {
			for(int colStart=0;colStart<16;colStart++) {
				prodOfInt=grid1[row][colStart]*grid1[row+1][colStart+1];
				for(int adjNum=2;adjNum<4;adjNum++){
					prodOfInt=prodOfInt*grid1[row+adjNum][colStart+adjNum];
				}
				if(prodOfInt>largestProd)
					largestProd=prodOfInt;
			}//end of row search
		}//end of diagonal search
		
		//check left diagonal
		for(int row=0;row<16;row++) {
			for(int colStart=19;colStart>3;colStart--) {
				prodOfInt=grid1[row][colStart]*grid1[row+1][colStart-1];
				for(int adjNum=2;adjNum<4;adjNum++){
					prodOfInt=prodOfInt*grid1[row+adjNum][colStart-adjNum];
				}
				if(prodOfInt>largestProd)
					largestProd=prodOfInt;
			}//end of left search
		}//end of diagonal search
		
		System.out.print(largestProd);
		
	}

}
