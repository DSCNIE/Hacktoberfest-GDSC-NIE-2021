package com.siddharth;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

    Generate_otp obj1 = new Generate_otp();
    Generate_lowerpassword obj2 = new Generate_lowerpassword();
    Generate_upperpassword obj3 = new Generate_upperpassword();

    int otp_length = 6;
    int password_length = 3;

        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();

        System.out.println("enter login method: ");
        System.out.print("enter 1 for OTP and 2 for Password: ");

        if(a==1) {
            System.out.println("your OTP is: "+ obj1.get_otp(otp_length));
        }else if(a==2) {
            System.out.println("your Password is: " + obj2.get_lowerpassword(password_length) + obj3.get_upperpassword(password_length));
        }else {
            System.out.println("invalid login attempt");
        }
    }
}
class Generate_otp {
    String str;
    int str_length;
    String otp = "";

    public Generate_otp() {
        this.str = "0123456789";
        this.str_length = str.length();
    }

    String get_otp(int len) {
        try {
            for (int i = 0; i < len; i++) {
                otp = otp + (str.charAt((int)((Math.random()*10)%str_length)));
            }
        }
        catch(StringIndexOutOfBoundsException e) {
            System.out.println(e.getMessage());
        }
        finally {
            System.out.println("exception caught!");
        }
        return otp;
    }
}
class Generate_lowerpassword extends Generate_otp implements Lower_password {
    String lower_password = "";

    public Generate_lowerpassword() {
        this.str = "abcdefghijklmnopqrstuvwxyz";
        this.str_length = str.length();
    }

    public String get_lowerpassword(int len) {

        for (int i = 0; i < len; i++) {
            lower_password += (str.charAt((int)((Math.random()*10)%str.length())));
        }
        return lower_password;
    }
}
class Generate_upperpassword extends Generate_otp implements Upper_password {
    String upper_password = "";

    public Generate_upperpassword() {
        this.str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        this.str_length = str.length();
    }

    public String get_upperpassword(int len) {
        for (int i = 0; i < len; i++) {
            upper_password += (str.charAt((int)((Math.random()*10)%str.length())));
        }
        return upper_password;
    }
}
interface Lower_password {
    public String get_lowerpassword(int len);
}
interface Upper_password {
    public String get_upperpassword(int len);
}