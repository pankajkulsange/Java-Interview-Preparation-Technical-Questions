
public class StringManipulation {
	
	// reverse string
	public static void main(String args[]) {
		reverseString();
		reverseStringUsingBuildInMethods();

	}
	public static void reverseString(){
		String str = "hello";
		String rev = "";
		for(int i = str.length()-1; i >= 0; i-- ) {
			rev += str.charAt(i);
		}
		System.out.println("Original String: " + str);
		System.out.println("Reversed String: " + rev);
	}
	public static void reverseStringUsingBuildInMethods(){
		String str = "hello";
		String reversed = new StringBuilder(str).reverse().toString();
		System.out.println(reversed);
	}

}
