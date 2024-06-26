# Algorithm

## 시뮬레이션

- 작은 의미로는 문제가 제시한 규칙에 따라 개체를 이동시키는 알고리즘을 말하며, 큰 의미로는 문제가 요구하는 대로 시행되도록 코드를 구현하는 알고리즘

![제목 없음](https://github.com/hjgel/Algorithm/assets/143315340/6da270e9-e87c-4413-af95-d7b42d017f6d)

### 종류

- 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
- 실수 연산을 다루고 특정 소수점 자리까지 출력해야 하는 문제
- 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
- 적절한 라이브러리를 찾아서 사용해야 하는 문제

### 특징

- 2차원배열이 많다.
- 그래프 탐색과 결합해서 나오는 경우가 많다.
- 이차원 공간에서의 방향 벡터가 자주 나온다.

### 차이

- 완전 탐색(Brute Force) : 모든 경우의 수를 주저 없이 다 계산하는 방법
- 시뮬레이션 : 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행하여 해결하는 방법

### 시간 복잡도

- 보통의 시뮬레이션은 이중 for문, 또는 삼중 for문을 작성하기 떄문에 기본적으로
- **O(N^2)** 이상이라고 생각하면 된다.
- 그럼에도 시뮬레이션을 사용하는 이유는 어차피 길어질 코드에, 잘 짜서 코드가 빨라진다고 하더라도, 속도 측면에서 그리 차이가 나지 않기에 가독성이 좋은 시뮬레이션을 주로 사용한다.
