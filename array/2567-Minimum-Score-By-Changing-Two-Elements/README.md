# 2567. Minimum Score By Changing Two Elements
https://leetcode.com/problems/minimum-score-by-changing-two-elements/

태그: Array, Greedy, Sorting

## 문제 요약
- low = 어떤 두 원소의 차이 중 가장 작은 값
- high = 어떤 두 원소의 차이 중 가장 큰 값
- score = low + high
- 원소 2개를 원하는 값으로 바꿀 수 있을 때, score의 최솟값 구하기

## 접근
바꿀 원소 2개를 남은 원소들 중 하나와 같은 값으로 바꾸면 low = 0이 되고 high값도 바뀌지 않는다.  
따라서 high를 최소로 만들면 된다. high = (최댓값 - 최솟값)인데 이 값을 줄이려면 배열에서 가장 큰 값들이나  
가장 작은 값들을 바꿔주면 된다.

경우는 3가지  
1. 가장 작은 값 2개를 변경 -> `nums[-1] - nums[2]`
2. 가장 큰 값 2개를 변경 -> `nums[-3] - nums[0]`
3. 가장 작은 값 1개, 가장 큰 값 1개 변경 -> `nums[-2] - nums[1]`

세 값 중 최솟값이 정답.

## 복잡도
- 시간 O(nlogn): 배열 정렬
- 공간 O(n): 파이썬 sort(Timsort)의 보조 공간