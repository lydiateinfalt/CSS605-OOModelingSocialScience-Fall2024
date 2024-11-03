package wealth_distribution;

public class Agent {
	final int MAX_WEALTH = 500;
	int wealth;

	Agent() {
		this.wealth = this.MAX_WEALTH;
	}

	Agent(int wealth) {
		this.wealth = wealth;
	}

	public boolean canGive() {
		boolean value;
		if (this.wealth > 0) {
			value = true;
		} else {
			value = false;
		}
		return (value);
	}
	
	public void give() {
		if(this.wealth > 0) {
			this.wealth = this.wealth -1;
		}
	}
	
	public void receive() {
		this.wealth = this.wealth +1;
	}
}
