package Bed_allocation;
import java.util.ArrayList;
import java.util.List;


public class Repository {
	//creating array list to store bedlist
      public List<Bed_info> BedList = new ArrayList();
    //creating array list to store hospital list
      public List<Hospital> hospList = new ArrayList();
      //creating array list to store patient details
      public List<Admit_patient>   patientList = new ArrayList();
      private static Repository repository;
      private Repository() {
    	  
      }
      public static Repository getRepository() {
    	  if(repository==null) {
    		  repository = new Repository();
    	  }
    	  return repository;
      }
}
