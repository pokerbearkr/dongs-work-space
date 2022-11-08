import java.util.Scanner;
public class array {
    public static void main(String[] args){
        int intarray[]= new int[5];
        int sum=0;

        Scanner scanner = new Scanner(System.in);
        System.out.print(intarray.length+"개의 정수를 입력하세요>>");
        for(int i=0;i<intarray.length;i++)
            intarray[i]= scanner.nextInt();

            for(int i=0;i<intarray.length;i++)
                sum+=intarray[i];

                System.out.print("평균은"+(double)sum/intarray.length);
                scanner.close();

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    }

 }
