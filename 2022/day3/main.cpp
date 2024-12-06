#include <iostream>
#include <fstream>
#include <map>
using namespace std;

int main()
{
  ifstream in("input.txt");
  string line;
  int sum = 0, count = 0;
  int check[127][3];
  while (getline(in, line))
  {
    // string first_half = line.substr(0, line.length() / 2);
    // string second_half = line.substr(line.length() / 2);
    // for (int i = 0; i < first_half.length(); ++i)
    // {
    //   check.insert(pair<char, int>(first_half[i], 1));
    // }

    // for (int i = 0; i < second_half.length(); ++i)
    // {
    //   if (check[second_half[i]] == 1)
    //   {
    //     cout << second_half[i] << endl;
    //     if (second_half[i] > 96)
    //       sum += second_half[i] - 96;
    //     else
    //       sum += second_half[i] - 38;
    //     cout << sum << endl;
    //     break;
    //   }
    // }
    if (count == 2)
    {
      for (int i = 0; i < 127; ++i)
      {
        if (check[i][0] == 1)
        {
          for (int j = 0; j < 3; ++j)
          {
            cout << check[i][j] << ' ';
          }
          cout << endl;
        }
      }
      count = 0;
    }
    for (int i = 0; i < line.length(); ++i)
    {
      check[line[i]][count] = 1;
    }
    count++;
  }
  cout << sum << endl;
  return 0;
}