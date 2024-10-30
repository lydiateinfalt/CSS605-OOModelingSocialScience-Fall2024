package hello;
import java.util.Scanner;

public class factorial {
	
	/* Accepts an integer as a parameter and returns the factorial */ 
	public static int factorial_calculator(int m) {
		
		if (m == 0 || m == 1) {
			return 1;
		}
		else { 
			return m* factorial_calculator(m-1);

		}
	}
	
	/* Prompts user to enter a number and passes it to factorial_calculator method and returns answer to be printed */ 
	public static void main(String[] args) {
		
		int num;
		Scanner in = new Scanner(System.in);
		
		System.out.println("Factorial Calculator");
		System.out.print("Enter a number ");
		num = in.nextInt();
		System.out.print(num + " factorial = ");
		System.out.print(factorial_calculator(num));
	}

}