//package Bed_allocation;
import java.util.*;

public class login_info {
 Scanner input = new Scanner(System.in);
 // Set login id
 public int setLoginid (int loginId)
 {
	 this.loginId = loginId;//use of this keyword
	 return loginId;
 }
 //get login id
 public int getLoginId() {
	 return loginId;
 }
 //set pin number
 public int setPinNumber(int pinNumber) {
	 this.pinNumber = pinNumber;
	 return pinNumber;
 }
 //Get pin number
 public int getPinNumber() {
	 return pinNumber;
 }
 //Access control mechanism
 public int loginId;
 private int pinNumber;
}
