package Bed_allocation;

public class Admit_patient {
	private long hospitalID;
	private int totalBed;
	private int patientID;
	private String patientName;
	public Admit_patient (long hospitalID,int totalBed,int patientID,String patientName) {
		this.hospitalID = hospitalID;
		this.totalBed = totalBed;
		this.patientID = patientID;
		this.patientName = patientName;
	}
	public Admit_patient(String patientName) {
		this.patientName = patientName;
	}
	public Admit_patient (int patientId){
		this.patientID = patientId;	
	}
	public Admit_patient() {
		
	}
	public long gethospitalID() {
		return hospitalID;
	}
	public int gettotalBed() {
		return totalBed;
	}
    public void setpatientID(int patientID) {
    	this.patientID = patientID;
    }
    public int getpatientID(){
    	return patientID;
    }
    public void setpatientName(String patientName) {
    	this.patientName = patientName;
    }
    public String getpatientName() {
    	return patientName;
    }
    public void setHospitalId(long hospitalID) {
		this.hospitalID = hospitalID;
	}
}
