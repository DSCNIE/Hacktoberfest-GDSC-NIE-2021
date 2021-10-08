package Bed_allocation;
import java.io.IOException;

import java.util.*;//Importing of packages available in java

//inheritance used to get login details
public class login extends login_info {
	 int Id = 0;
	
	public void login_info() {
		//Method overloading
	}
	//method overriding
	public void login_info(int loginId) {
		super.loginId = Id; //use of super keyword

	}
	
	Scanner menuInput = new Scanner(System.in);
	//Verify user
	HashMap<Integer,Integer>data = new HashMap<Integer,Integer>();
	//Exception Handling in java
	public void getLogin()throws IOException {
		int x =1;
		do {
			try {
				data.put(123456, 1837);
				data.put(654231,3553);
				data.put(255559,4309);
				data.put(255851,4567);
				System.out.println("The programe written By manu K usn :4ni19is046");
				System.out.println("Welcome to covid Bed allocation portal");
				System.out.print("Enter your Hospital Login id :");
			    setLoginid(menuInput.nextInt());
			    System.out.println("Enter your password");
			    setPinNumber(menuInput.nextInt());    
			}catch (Exception e)
			{
				System.out.println("\n"+"Invalid Character(s).only numbers."+"\n");
				x =2;
			}
			for(java.util.Map.Entry<Integer ,Integer>entry : data.entrySet())
			{
				//Checking for correct login details
				if(entry.getKey() == getLoginId()&& entry.getValue() == getPinNumber() ) {
					System.out.println("You have been successfully login to the covid portal ");
		//after successful login user can access other parts of program
					dataEntry data = new dataEntry();
					data.displayMenu();
					
				}
			}
			System.out.println("wrong login id or password");
		}while (x == 1);
	}
	
	
}