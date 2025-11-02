import java.lang.reflect.Array;
import java.util.Scanner;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num[] = new int[28];

		for (int i = 0; i < 28; i++) {
			num[i] = sc.nextInt(); // 입력 값을 int로 읽어서 배열에 저장
		}
		sc.close(); // 스캐너는 사용 끝나면 항상 닫아주기
		Arrays.sort(num); // 오름차순으로 정렬

		// 1 ~ 30 중에 누가 안냈는지 확인하기
		for (int i = 1; i <= 30; i++) {
			boolean check = false;
			for (int j = 0; j < 28; j++) {
				if (num[j] == i) {
					check = true;
					break;
				}
			}
			// 만약 check가 false 라면 print
			if (!check) {
				System.out.println(i);
			}
		}
	}
}
