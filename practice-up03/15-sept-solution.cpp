#include <iostream>
#include <vector>
#include <limits>

#define NDEBUG

void print_vec(const std::vector<int> &vec);

int main()
{
  const int M = 5;
  const std::vector<int> A = {1, 2, 3, 4, 5};
  const std::vector<int> B = {6, 7, 8, 9, 10};
  const size_t K = B.size();

  int min_product = std::numeric_limits<int>::max();
 
  std::cout << "Vector A: "; print_vec(A);
  std::cout << "Vector B: "; print_vec(B);
  std::cout << '\n';


  // calculate the product for each k
  for (int k = 1; k <= M; k++)
  {
    long long int product = 1;

    // calculate the product
    for (int i = 1; i <= k; i++)
    {
      auto res = 1 / A[i-1] - B[i-1];

      #ifndef NDEBUG
      // info for debug
      std::cout
        << "k: " << k
        << " i: " << i
        << " res: " << res
      << std::endl;
      #endif

      product *= res;
    }

    std::cout << "product for k = " << k << ": " << product << std::endl;

    // search min product
    if (product < min_product)
      min_product = product;
  }
  
  std::cout << '\n';
  std::cout << "Min product: " << min_product << std::endl;

  return 0;
}

void print_vec(const std::vector<int> &vec)
{
  std::cout << "[";

  // we can also use this syntax: std::vector<int>::const_iterator iter = vec.cbegin()
  for(auto iter = vec.cbegin(); iter != vec.cend(); iter++)
    std::cout << *iter << (iter == vec.cend()-1 ? "" : ", ");

  std::cout << "]" << '\n';
}

