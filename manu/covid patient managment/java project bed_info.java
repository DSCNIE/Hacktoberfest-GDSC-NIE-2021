package Bed_allocation;

public class Bed_info {
	private long hospitalID;
	private int totalBed;
	public Bed_info(long hospitalID,int totalBed) {
		this.hospitalID = hospitalID;
		this.totalBed = totalBed;
	}
	public  Bed_info() {
		
	}
	public long gethospitalID() {
		return hospitalID;
	}
	//set total bed
	public void settotalbed(int totalBed) {
		this.totalBed = totalBed;
	}
	public int gettotalBed() {
		return totalBed;
	}
	//set hospital id
	public void setHospitalId(long hospitalID) {
		this.hospitalID = hospitalID;
	}
	

}
