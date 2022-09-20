#include <iostream>
#include <vector>
#include <limits>


int main()
{
  const int M = 5;
  const std::vector<int> A = {1, 2, 3, 4, 5};
  const std::vector<int> B = {6, 7, 8, 9, 10};
  const size_t K = B.size();
  
  int min = std::numeric_limits<int>::max();
 
  for (int k = 1; k <= M; k++)
  {
    long long int mult = 1;
    for (int i = 1; i <= k; i++)
    {
      auto res = 1 / A[i-1] - B[i-1];

      std::cout
        << "k: " << k
        << " i: " << i
        << " res: " << res
      << std::endl;

      mult *= res;
    }

    std::cout << "mult: " << mult << std::endl;
  }
  
  std::cout << "\nMin: " << min << std::endl;

  return 0;
}

