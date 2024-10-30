package hello;
import java.util.Scanner;

public class tempConverter {

	public static void main(String[] args) {
		int F;
		double C;
		double FC = 5.0/9.0;
		final int FZero = 32;
		Scanner in = new Scanner(System.in);
		
		System.out.println("Fahrenheit to Celsius Converter");
		System.out.print("What is the temp in F?");
		F = in.nextInt();
		C = (F-FZero)* (FC);
		System.out.print(F + " Fahrenheit = ");
		System.out.printf("%.2f Celsius", C);
		System.out.println("");

	}

}
