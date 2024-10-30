package civil_action;

import java.util.Random;

public class Protest {
	public int numCitizens;
	public int numProtesters;
	public double currentProtesting;
	public double initialProtesting;

	public Person[] persons;
	public Random random;

//model the population deciding what to do
	public void act() {
		for (int i = 0; i < numCitizens; i++) {
			Person person = persons[i];
			person.decide(currentProtesting);
		}

	}

//count up the number of protesters
	public void tabulate() {

//count number of protesters
		numProtesters = 0;
		for (int i = 0; i < numCitizens; i++) {
			Person person = persons[i];
			if (person.joinedProtest == 1) {
				numProtesters += 1;
			}
		}

		// update percent protesting
		currentProtesting = (1.0 * numProtesters) / (1.0 * numCitizens);
	}

	Protest() {
		numCitizens = 10000;
		numProtesters = 0;
		currentProtesting = 0.0;
		initialProtesting = 0.035;

		persons = new Person[numCitizens];
		random = new Random();

		for (int i = 0; i < numCitizens; i++) {
			int hasJoined = 0;
			double chance = random.nextDouble();
			double threshold = 0.0;
			if (chance < this.initialProtesting) {
				threshold = 0.0;
				hasJoined = 1;
			} else {
				threshold = random.nextDouble();
				hasJoined = 0;
			}
			Person person = new Person(hasJoined, threshold);
			persons[i] = person;
		}

// update counts
		tabulate();
	}

	//
	// main
	//
	public static void main(String[] args) {

		Protest protest = new Protest();
		//int n = 10;
		for (int j = 10; j <= 100; j += 10) {
			for (int i = 0; i < j; i++) {
				protest.act();
				protest.tabulate();
			}
			System.out.printf("t=%4d num protesters = %4d, percent = %8.2f\n", j, protest.numProtesters,
					protest.currentProtesting);
		}
	}
}
