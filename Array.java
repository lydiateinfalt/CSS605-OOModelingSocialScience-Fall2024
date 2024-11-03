package hello;

import java.util.Arrays;

public class Array {

	// Sum array using for loop
	public static int arraySumFor(int[] a) {
		int sum = 0;

		for (int i = 0; i < a.length; i++) {
			sum = sum + a[i];
		}
		return sum;
	}
	
	// Sum array using while loop
	public static int arraySumWhile (int[] a) {
		int sum = 0;
		int i = 0;
		
		while (i < a.length) {
			sum = sum + a[i];
			i = i+1;	
		}
		return sum;
	}
	
	// Sum array using do while loop
	public static int arraySumDoWhile (int[] a) {
		int sum = 0;
		int i = 0;
		
		do {
			sum = sum + a[i];
			i = i+1;	
		} 
		while (i < a.length);
		return sum;
	}
	public static void main(String[] args) {
		int[] sequence;
		sequence = new int[100];

		for (int k = 0; k < 100; k++) {
			sequence[k] = k+1;
		}
		System.out.println("Array = " + Arrays.toString(sequence));
		System.out.println("Sum of the array using FOR loop = " + arraySumFor(sequence));
		System.out.println("Sum of the array using WHILE loop = " + arraySumWhile(sequence));
		System.out.println("Sum of the array using DO WHILE loop = " + arraySumDoWhile(sequence));

	}

}
