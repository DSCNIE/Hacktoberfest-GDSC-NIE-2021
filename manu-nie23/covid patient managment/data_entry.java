package Bed_allocation;
import java.io.IOException;

import java.util.List;
import java.util.List;
import java.util.Scanner;
import java.util.Set;
//concept of importing packages as been included
import Hospitalmanagment.Hospital;

public class dataEntry extends login_info {
	//Access control
      private Scanner input = new Scanner(System.in);
      private Repository repo = Repository.getRepository();
      ReportService reportservice = new ReportService();
      public dataEntry() {
    	  prepareSampleData();
      }
      
      private int choice;
      int i;
      public String[] HospName = new String[20];
      public  String[] PatientName= new String[20];
   
      
      public void displayMenu() {
    	  while(true) {
    		    printMenu();
    		    switch(choice) {
    		  
    		    case 1:
    		         hospitallist();
    		         pressAnyKeyToContinue();
   		             break;
    		  
    		    case 2:
    		          bedavailabilitylist();
    		          pressAnyKeyToContinue();
    		          break;
    		    case 3:
    		         admitpatient();
    		     
    		         pressAnyKeyToContinue();
   		          break;
    		   
    		    case 4:
    		         exit();
    		         break;
    		    
    		    }
    		   	  
    	  }
      }
      public void printMenu() {
    	  System.out.println("Menu");
    	  System.out.println("1.Hospital list");
    	  System.out.println("2.Bed Availability List");
    	  System.out.println("3.Admit Patient");
    	  System.out.println("4.Exit");
    	  System.out.println("Enter Your Choice");
    	  choice = input.nextInt();
      }
      public void pressAnyKeyToContinue()
      {
        System.out.println("Press any key to continue");
        //Exception handling
        try {
        	System.in.read();
        }catch (IOException e) {
        	e.printStackTrace();
        }
      }
      //Interface concept included 
      interface hospital
      {
    	  void addHospital();
      }
      class addHospital implements hospital
      {
      public void addHospital() {
    	  input.nextLine();
    	  System.out.print("Enter Hospital Name ");
    	  String hospName = input.nextLine();
    	  Hospital hosp = new Hospital(hospName);
    	  repo.hospList.add(hosp);
    	  System.out.println("\nHospital Added:\n" + hospName);
      }
      }
      public void  hospitallist() {
    	  System.out.println("Hospital Names List");
    	  List<Hospital>hlist = repo.hospList;
    	  for(int i =0; i<hlist.size();i++) {
    		  Hospital h = hlist.get(i);
    		  System.out.println((i+1) +"," +  h.getName()+","+ h.gethospitalID());
    	  }
      }
      
   
     public void bedavailabilitylist() {
    	  System.out.println("Bed Availablity");
    	  List<Bed_info> BedList = repo.BedList;
    	 List<Hospital>hlist = repo.hospList;
    	for(int i =0;i<BedList.size();i++) {
    		
    		  Bed_info bed = BedList.get(i);
    	//Hospital name accessed by using hospital id
			String hospName = reportservice.getHospitalNameByID(bed.gethospitalID());
    		  System.out.println((i+1) +","+ hospName+ "," + bed.gettotalBed());
    	}
    		}
    	  
      
      public void admitpatient() {
    	  List<Bed_info> BedList = repo.BedList;
	         Bed_info bed = BedList.get(i);
	    
 		  for(int i =0;i<BedList.size();i++) {
 			  System.out.println("Allocate Bed for covid patient");
 	     	  System.out.println("Display List of hospitals");
 	     	  hospitallist();
 	     	  //Selecting hospital in which patient has to be admitted
 	    	  System.out.println("Select the hospital");
 	    	  int hospChoice = input.nextInt();
 	    	 Hospital selectedhosp = repo.hospList.get(hospChoice -1);
 	    	 
 	    	  System.out.println("Selected hospital:" +selectedhosp.getName());
 	    	  System.out.println("Enter patient details");
 	    	  System.out.println("Enter patient Name And hospital in which he as to get admiited");
 	    	
 	    	  String patientName = input.next();
 	    	  String  HospName =input.next();
 	    	 
 			  System.out.println((i+1)+"," +HospName + ","+ patientName);
 			  System.out.println("Patient Added");
 			  System.out.println("Would do you like do add another patient?If so enter 1\n");
 			  int x = input.nextInt();
 			  if(x!=1) {
 				  i = 101;
 			  }
 			  

	    		
 		  }
 		 
 		  
 		
      }
      //exit and stop the program
      public void exit() {
    	  System.out.println("System Exiting");
    	  System.exit(0); 
      }
      // preparing sample data 
     
     public void  prepareSampleData() {
    	 Hospital hospSapthagiri = new Hospital("Sapthagiri");
    	 delay();
    	 Hospital hospAppolo = new Hospital("Appolo");
    	 delay();
    	 Hospital hospJSS = new Hospital("JSS");
    	 delay();
    	 Hospital hospPrasad = new Hospital("prasad");
    	 delay();
    	 Hospital hospKC = new Hospital("KC");
    	 delay();
    	 Hospital hospFortis = new Hospital("Fortis");
    	 delay();
    	 Hospital hospBowring = new Hospital("Bowring");
    	 delay();
    	 Hospital hospvikram = new Hospital("Vikram");
    	 delay();
    	 Hospital hospvanivillas = new Hospital("vanivillas");
    	 delay();
    	 //repo function used to create list
    	 repo.hospList.add(hospSapthagiri);
    	 repo.hospList.add(hospAppolo);
    	 repo.hospList.add(hospJSS);
    	 repo.hospList.add(hospPrasad);
    	 repo.hospList.add(hospKC);
    	 repo.hospList.add(hospFortis);
    	 repo.hospList.add(hospBowring);
    	 repo.hospList.add(hospvikram);
    	 repo.hospList.add(hospvanivillas );
    	 
    	 Bed_info b1 = new Bed_info(hospSapthagiri.gethospitalID(), 60);
    	 Bed_info b2 = new Bed_info(hospAppolo.gethospitalID(), 25);
    	 Bed_info b3 = new Bed_info(hospJSS.gethospitalID(), 18);
    	 Bed_info b4 = new Bed_info(hospPrasad.gethospitalID(), 15);
    	 Bed_info b5 = new Bed_info(hospKC.gethospitalID(), 130);
    	 Bed_info b6 = new Bed_info(hospFortis.gethospitalID(), 75);
    	 Bed_info b7 = new Bed_info(hospBowring.gethospitalID(), 28);
    	 Bed_info b8 = new Bed_info(hospvikram.gethospitalID(), 23);
    	 Bed_info b9 = new Bed_info(hospvanivillas .gethospitalID(), 15); 
    	 
    	 repo.BedList.add(b1);
    	 repo.BedList.add(b2);
    	 repo.BedList.add(b3);
    	 repo.BedList.add(b4);
    	 repo.BedList.add(b5);
    	 repo.BedList.add(b6);
    	 repo.BedList.add(b7);
    	 repo.BedList.add(b8);
    	 repo.BedList.add(b9);
     }
     //Thread created 
     private void delay() {
    	 try {
    		 Thread.sleep(10);
    		 
    	 }catch (InterruptedException e) {
    		  e.printStackTrace();
    	 }
     }
     
}
