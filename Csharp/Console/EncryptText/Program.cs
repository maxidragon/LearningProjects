using System;
using System.Collections.Generic;

namespace Kodowanie
{
    class Program
    {
        public static List<Letter> letters = new List<Letter>();
        public static void Main(string[] args)
        {
            Console.WriteLine("Press ESC to end program");
            char key = ' ';
            string key2 = "";
            while (key != 27)
            {
                Console.ForegroundColor = ConsoleColor.Yellow;
                Console.WriteLine("Give symbol: ");
                key = Console.ReadKey(true).KeyChar;

                if (key == 27)
                {
                    break;
                }
                else
                {
                    Console.WriteLine(key.ToString());
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine("Give code: ");
                    key2 = Console.ReadLine(); ;
                    letters.Add(new Letter() { symbol = key, code = key2 });
                }
            }
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine("Give Text: ");
            Console.ForegroundColor = ConsoleColor.White;
            string text = Console.ReadLine();
            char[] textC = text.ToCharArray();
            string result = "";
            Console.WriteLine("What do you want to do? ");
            Console.WriteLine("1. Encrypt");
            Console.WriteLine("2. Decrypt");
            char wybor = Console.ReadKey(true).KeyChar;
            if (wybor == 49)
            {
                for (int i = 0; i < textC.Length; i++)
                {
                    foreach (Letter item in letters)
                    {
                        if (item.symbol == textC[i])
                        {
                            result = result + item.code;
                        }
                    }
                }
                Console.WriteLine("Encrypted text: " + result);
            }
            else if (wybor == 50)
            {
                for (int i = textC.Length - 1; i >= 0; i = i - 4)
                {
                    if (i >= 3)
                    {
                        foreach (Letter item in letters)
                        {

                            string temp = textC[i].ToString() + textC[i - 1].ToString() + textC[i - 2].ToString() + textC[i - 3].ToString();
                            if (item.code == temp)
                            {
                                result = item.symbol + result;
                                break;
                            }
                        }
                    }

                }
                Console.WriteLine("Decrypted text: " + result);
            }
            else
            {
                Console.WriteLine("Bad choice!");
            }

        }
    }
    class Letter
    {
        public char symbol;
        public string code;
    }
}
