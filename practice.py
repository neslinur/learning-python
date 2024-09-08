import java.util.Scanner;

{
 

 Scanner scan = new Scanner(System.in);
    System.out.println("enter seconds");
   
    int a = scan.nextInt();
    int b = a/60;
      int c = b/60;
   
     
    System.out.println("minutes "+b);
    System.out.println("hours "+c);
        System.out.println("seconds "+a);

