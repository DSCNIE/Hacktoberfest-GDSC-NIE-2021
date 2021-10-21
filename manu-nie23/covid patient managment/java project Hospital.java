package Bed_allocation;

public class Hospital {
	private long hospitalID =System.currentTimeMillis() ;
	//set constant random hospital id using current Time millisecond
         private String name;
         //constructors
         public Hospital(int hospitalID,String name ) {
        	 this.name = name;
        	 this.hospitalID = hospitalID; 
         }
         
         public Hospital(String name) {
        	 this.name = name;
         }
         public Hospital() {
        	 
         }
         public long gethospitalID() {
        	 return hospitalID;
         }
         //get hospital name
         public String getName() {
        	 return name;
         }
         public void setHospitalId(int hospitalID) {
        	 this.hospitalID = hospitalID;
         }
         public void setName(String name) {
        	 this.name = name;
         }
}
