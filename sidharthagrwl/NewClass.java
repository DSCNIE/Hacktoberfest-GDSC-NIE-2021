package sidharthagrwl;
import java.util.*;

public class NewClass {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
		
		int randNum = (int)(Math.random()*100);
		System.out.println("random number generated is "+randNum);
		int mynum = 0;
        
		while(mynum>=0) {
			mynum = sc.nextInt();
			if(mynum>randNum) {
				System.out.println("too high");
			}
			else if(mynum<randNum) {
				System.out.println("too low");
			}
			else if(mynum==randNum) {
				System.out.println("correct guess");
				break;
			}
			}
            sc.close();
    }
}
