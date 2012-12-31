Title: A little JAVA; Overloaded Method
Date: 2010-09-21
Author: Michael


Overloaded methods are handy for situations when you want to pass
parameters in varying ways. I'm sure this is really simple stuff for
veteran Java Jedi's, but it may come in handy for a beginner like
myself. Notice that the name of the method is the same for all three.
The Java complier/runtime is actually smart enough to determine which
one to use. Keep the variable names different unless you plan to use a
"this" reference.... and watch your data types as you may run into an
Ambiguous compile time error.

The first method passes in three parameters:


	:::java
	public void computeNetPay(double hrs, double rtePay, double taxRate) {
	//var to hold tax amount
	double Withholding;

	//assign vars
	Hours = hrs;
	ratePay = rtePay;
	rateTaxes = taxRate;</code>

	//calc gross
	gross = Hours * ratePay;

	//calc amount to withhold from taxes
	Withholding = gross * rateTaxes;

	//Find Net Pay
	net = gross - Withholding;
	System.out.println("This method recieved three parameters and net pay is " + net);
	}




The second passes in two parameters and the third passes in one parameter as you can see from the rest of the code here:




	:::java
	public class Pay {
	private double Hours;
	private double ratePay;
	private double rateTaxes;
	private double gross;
	private double net;

	<code>public void computeNetPay(double hrs, double rtePay, double taxRate)
	{
	//var to hold tax amount
	double Withholding;

	<code>//assign vars
	Hours = hrs;
	ratePay = rtePay;
	rateTaxes = taxRate;

	//calc gross
	gross = Hours * ratePay;
	//calc amount to withhold from taxes
	Withholding = gross * rateTaxes;
	//Find Net Pay
	net = gross - Withholding;
	System.out.println("This method recieved three parameters and net pay is " + net);
	}
	public void computeNetPay(double hrs, double rtePay){
	double Withholding;
	//assign tax rate
	rateTaxes = 0.15;
	Hours = hrs;
	ratePay = rtePay;
	gross = Hours * ratePay;
	Withholding = gross * rateTaxes;
	net = gross - Withholding;
	System.out.println("This method recieved two parameters and net pay is " + net);
	}
	public void computeNetPay(double hrs){
	double Withholding;
	Hours = hrs;
	rateTaxes = 0.15;
	//assign Pay rate
	ratePay = 5.85;
	gross = Hours * ratePay;
	Withholding = gross * rateTaxes;
	net = gross - Withholding;
	System.out.println("This method recieved one parameters and net pay is " + net);
	}



