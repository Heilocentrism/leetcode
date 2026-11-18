# 73. Set Matrix Zeroes (Medium)
https://leetcode.com/problems/set-matrix-zeroes/

## 문제 요약
행렬에서 0인 칸이 있으면 그 행과 열 전체를 0으로 바꾸기. 제자리(in-place)에서 수정해야 함.

## 접근
- 첫 행/열을 "이 행/열은 0으로" 표시용으로 사용 -> 추가 공간 O(1)
- 첫 행/열에 원래 0이 있었는지는 미리 변수로 저장
- 첫 행/열은 마지막에 처리 (표시가 덮어씌워지지 않도록)

## 복잡도
- 시간 O(m·n), 공간 O(1)

