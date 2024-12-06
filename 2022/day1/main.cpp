#include <iostream>
#include <fstream>

using namespace std;

int main()
{
  ifstream in("input.txt");
  string line;
  int sum = 0, max = -1, max2 = -1, max3 = -1;
  while (getline(in, line))
  {
    if (line.empty())
    {
      if (sum > max)
      {
        max3 = max2;
        max2 = max;
        max = sum;
      }
      else if (sum > max2)
      {
        max3 = max2;
        max2 = sum;
      }
      else if (sum > max3)
      {
        max3 = sum;
      }
      cout << sum << endl;
      cout << max << ' ' << max2 << ' ' << max3 << endl;
      sum = 0;
    }
    else
    {
      int num = stoi(line);
      sum += num;
    }
  }
  if (sum > max)
  {
    max3 = max2;
    max2 = max;
    max = sum;
  }
  else if (sum > max2)
  {
    max3 = max2;
    max2 = sum;
  }
  else if (sum > max3)
  {
    max3 = sum;
  }
  cout << max << ' ' << max2 << ' ' << max3 << endl;
  cout << max + max2 + max3 << endl;
  return 0;
}