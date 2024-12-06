#include <iostream>
#include <fstream>

using namespace std;

int main()
{
  ifstream in("input.txt");
  string line;
  int score = 0;
  // Part 1
  // while (getline(in, line))
  // {
  //   score += line[2] - 87;
  //   if (line[0] == 'A') // rock
  //   {
  //     if (line[2] == 'X')
  //     {
  //       score += 3;
  //     }
  //     else if (line[2] == 'Y')
  //     {
  //       score += 6;
  //     }
  //     else
  //     {
  //       score += 0;
  //     }
  //   }
  //   else if (line[0] == 'B') // paper
  //   {
  //     if (line[2] == 'X')
  //     {
  //       score += 0;
  //     }
  //     else if (line[2] == 'Y')
  //     {
  //       score += 3;
  //     }
  //     else
  //     {
  //       score += 6;
  //     }
  //   }
  //   else // scrissors
  //   {
  //     if (line[2] == 'X')
  //     {
  //       score += 6;
  //     }
  //     else if (line[2] == 'Y')
  //     {
  //       score += 0;
  //     }
  //     else
  //     {
  //       score += 3;
  //     }
  //   }
  // }
  // Part 2
  while (getline(in, line))
  {
    score += (line[2] - 88) * 3;
    if (line[0] == 'A') // rock
    {
      if (line[2] == 'X')
      {
        score += 3;
      }
      else if (line[2] == 'Y')
      {
        score += 1;
      }
      else
      {
        score += 2;
      }
    }
    else if (line[0] == 'B') // paper
    {
      if (line[2] == 'X')
      {
        score += 1;
      }
      else if (line[2] == 'Y')
      {
        score += 2;
      }
      else
      {
        score += 3;
      }
    }
    else // scrissors
    {
      if (line[2] == 'X')
      {
        score += 2;
      }
      else if (line[2] == 'Y')
      {
        score += 3;
      }
      else
      {
        score += 1;
      }
    }
    cout << score << endl;
  }

  cout << score << endl;
  return 0;
}