package backjoon.array;

import java.util.Scanner;
import java.util.Arrays;

// 2025-11-2 코테 스터디 1주차 백준 5597  배열 문제 과제
//
// X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
// 교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.
// 입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다. 출석번호에 중복은 없다.
// 출력은 2줄이다. 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 2번째 줄에선 그 다음 출석번호를 출력한다.
//
// 그럼 입력을 받을때 뭔가 자동으로 정렬이 되는 것으로 받아야한다.
public class array5597 {
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
