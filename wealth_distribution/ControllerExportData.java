package wealth_distribution;

public class ControllerExportData extends Controller{

    public ControllerExportData(int numAgents) {
        super(numAgents);
    }
    

	public static void main(String[] args) {
		
	        int numAgents = 100;
			int numTradingDays = 250;
	        ControllerExportData controller = new ControllerExportData(numAgents);
			
			// set up number of time cycles to run
			int maxYears = 50;
			
			// set up the model
			controller.init();
			
			// run for numLoops time cycles
			for (int yr = 0; yr < maxYears; yr++) {
				
				// do the run for the year
				controller.run(numTradingDays);
				controller.calcStats();
				System.out.println(yr + "," + controller.sdVal);	
			}
			
	}

}
