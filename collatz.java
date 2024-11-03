package hello;

public class collatz {
	public static int col (int n) {
		while (n != 1) {
			System.out.print(n);
			System.out.print(" ");
			if ((n % 2) == 0) { // n is even
				n = n / 2;
			} else {
				n = (n * 3) + 1;
			}
		}
		System.out.print(n);
		System.out.println("");
		System.out.println("");
		return n;
	}

	public static void main(String[] args) {
		
		int counter = 10;
		
		while (counter > 0) {
			System.out.print("Collatz ");
			System.out.println(counter);
			col(counter);
			counter = counter - 1;
		}
	}
}

