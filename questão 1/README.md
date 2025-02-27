## 857. Minimum Cost to Hire K Workers

![{F51D24CA-E454-45FF-90FA-4017F9B7B4D4}](https://github.com/user-attachments/assets/3d90b616-bcb8-41ae-949f-f043776f94f7)

[Link para a questão](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/description/)

### Gravação

[Link para a gravação](https://youtu.be/8d-GFH15Mns)

#### Dificuldade: Difícil

### Enunciado

There are n workers. You are given two integer arrays quality and wage where quality[i] is the quality of the ith worker and wage[i] is the minimum wage expectation for the ith worker.

We want to hire exactly k workers to form a paid group. To hire a group of k workers, we must pay them according to the following rules:

Every worker in the paid group must be paid at least their minimum wage expectation.
In the group, each worker's pay must be directly proportional to their quality. This means if a worker’s quality is double that of another worker in the group, then they must be paid twice as much as the other worker.
Given the integer k, return the least amount of money needed to form a paid group satisfying the above conditions. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: quality = [10,20,5], wage = [70,50,30], k = 2
Output: 105.00000
Explanation: We pay 70 to 0th worker and 35 to 2nd worker.
Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
Output: 30.66667
Explanation: We pay 4 to 0th worker, 13.33333 to 2nd and 3rd workers separately.
 

Constraints:

n == quality.length == wage.length
1 <= k <= n <= 104
1 <= quality[i], wage[i] <= 104

### Submissões: 

![{40515E90-5276-41B7-980E-F2CEDA9BD3B1}](https://github.com/user-attachments/assets/9320b6c1-4fae-4bc3-8478-fe8200883dbf)

![{ADA2D50C-BE59-4880-AA41-D5B0B1373769}](https://github.com/user-attachments/assets/47ee7814-c811-4d7e-9bb1-47ac509e6e0d)

