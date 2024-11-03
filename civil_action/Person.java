/** civil_action
 * this class models a person in a civil action (protest)
 * social setting
 */

package civil_action;

public class Person {
public int joinedProtest;
public double threshold;

// default constructor
Person() {
joinedProtest = 0;
threshold = 0.50;
}

// parameterized constructor
Person(int joinedProtest, double threshold) {
this.joinedProtest = joinedProtest;
this.threshold = threshold;
}

// agent decision making process
public void decide(double percentProtesting) {
if (percentProtesting >= threshold) {
joinedProtest = 1;
}
}
}
