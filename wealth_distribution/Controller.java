package wealth_distribution;

import java.util.Random;

public class Controller {
	// class variables
	final int MAX_AGENTS = 100;
	int numAgents;
	Agent[] agentSet;
	Random random;
	
	//booking variables
	double meanVal;
	double sdVal;
	
	// constructor -- default
	Controller(){
		numAgents = MAX_AGENTS;
		agentSet = new Agent[this.numAgents];
		random = new Random();
		meanVal = 0.0;
		sdVal = 0.0;
	}
	
	Controller(int numAgents){
		this.numAgents = numAgents;
		agentSet = new Agent[this.numAgents];
		random = new Random();
		meanVal = 0.0;
		sdVal = 0.0;
	}	
	
	//init()
	//
	//initializes the agent population
	public void init() {
		for (int i = 0; i < numAgents; i++) {
			Agent agent = new Agent();
			agentSet[i]= agent;
		}
	}
	
	public void run(int numTicks) {
		for (int t = 0; t < numTicks; t++) {
			
			for (int j = 0; j < numAgents; j++) {
				
				// pick donor agent
				int src = j;
				
				//pick recipient agent, other than ourself
				int tgt = Math.abs(random.nextInt()) % numAgents;
				while (src == tgt) {
					tgt = Math.abs(random.nextInt()) % numAgents;
				}
				
				if (agentSet[src].canGive() == true) {
					// ask src to donate
					agentSet[src].give();
					// ask tgt to receive
					agentSet[tgt].receive();
				} //if
			} // for j
			
		} // for t
	} // run
	
	public void calcStats() {
		int totalWealth =0;
		//compute total wealth
		for (int i = 0; i < numAgents; i++) {
			totalWealth = totalWealth + agentSet[i].wealth;
		}
		
		//compute mean
		double meanWealth = totalWealth/(1.0*numAgents);
		meanVal = meanWealth;
		
		// compute sd
		double sd = 0.0;
		double sumSquare = 0.0;
		for (int i = 0; i<numAgents; i++) {
			double tmp = Math.pow(agentSet[i].wealth - meanWealth, 2.0);
			sumSquare = sumSquare + tmp;
		} // for i
		sd = Math.pow(sumSquare, 0.5);
		sdVal = sd;
	} // calStats
	
	
	public static void main(String[] args) {
		// set up the Controller
		int numAgents = 100;
		Controller controller = new Controller(numAgents);
		
		// set up number of time cycles to run
		int maxYears = 50;
		int numTradingDays = 250;
		
		// set up the model
		controller.init();
		
		// run for numLoops time cycles
		for (int yr = 0; yr < maxYears; yr++) {
			
			// do the run for the year
			controller.run(numTradingDays);
			controller.calcStats();
			System.out.printf("at end of year = %4d, weath sd = %8.2f\n", yr, controller.sdVal);	
		}
		

	}

}
