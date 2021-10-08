package Bed_allocation;

public class ReportService {
	
	Repository repo = Repository.getRepository();
	//To access hospital name using hospital id 
	public String getHospitalNameByID(long hospitalID) {
		for(Hospital h : repo.hospList) {
			if(h.gethospitalID() == (hospitalID)) {
				return h.getName();
			}
		}
		return null;
	}
}

