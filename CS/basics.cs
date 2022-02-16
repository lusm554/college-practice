using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


public class Program
{

    static string ASK(string question)
    {
      string answer;
      Console.WriteLine(question);
      answer = Console.ReadLine();
      return answer;
    }

    static void Main(string[] args)
    {
      string[] questions = new string[] {"How old are you?", "What your gender?", "How are you?", "What's your name?", "Do you have job?"};
      List<string> list = new List<string>();
      foreach (string question in questions)
      {
        string answer;
        answer = Program.ASK(question);
        list.Add(answer);
      }

      Console.WriteLine("\nYour answers:\n");

      for (int i = 0; i < list.Count; i++) 
      {
        Console.WriteLine(questions[i] + " " + list[i]);
      }
    }
}

