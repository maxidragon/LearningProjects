using System;
using System.Threading;

namespace Hangman
{
    class Program
    {
        public static string[] kategorie = { "brak", "fruits", "vegetables" };
        public static string[] fruits = { "apple", "pineapple", "strawberry"};
        public static string[] vegetables = { "carrot"};
        public static char[] used = new char[32];
        public static string generatedWord = "";
        public static int choosedCategory = 0;
        public static string display = "";
        public static int hangman = 0;
        public static int[] occuringLetters = new int[20];
        public static Random rnd = new Random();
        static void Main(string[] args)
        {
            Hello();
        }
        public static void Hello()
        {
            generatedWord = "";
            display = "";
            choosedCategory = 0;
            hangman = 0;
            for (int i = 0; i < occuringLetters.Length; i++)
            {
                occuringLetters[i] = 0;
            }
            for (int i = 0; i < used.Length; i++)
            {
                used[i] = ' ';
            }
            Console.Clear();
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine("Hello w Wisielcu");
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("Wybierz kategorię (wpisz liczbę)");
            Console.WriteLine("1. Fruits");
            Console.WriteLine("2. Vegetables");
            Console.ForegroundColor = ConsoleColor.White;
            char category = Console.ReadKey(true).KeyChar;
            switch (category)
            {
                case '1':
                    StartGame(fruits, 1);
                    break;
                case '2':
                    StartGame(vegetables, 2);
                    break;
                default:
                    break;
            }


        }
        public static void StartGame(string[] possibleWords, int category)
        {
            Console.Clear();

            int which = rnd.Next(0, hasla.Length);
            generatedWord = possibleWords[word];
            choosedCategory = category;
            for (int i = 0; i < generatedWord.Length; i++)
            {
                display = display + "_";
            }
            for (int i = 0; i < used.Length; i++)
            {
                used[i] = '8';
            }
            Play();
        }
        public static void Play()
        {
            if (display == generatedWord)
            {
                Win();
            }
            else
            {
                string display2 = display.Replace("_", "_ ");
                Console.Clear();
                Console.WriteLine("category: " + kategorie[choosedCategory]);
                DisplayUsedLetters();
                Console.WriteLine(display2);
                DrawHangman();
                Console.ForegroundColor = ConsoleColor.Yellow;
                Console.WriteLine("Give a letter");
                Console.ForegroundColor = ConsoleColor.White;
                char letter = Console.ReadKey(true).KeyChar;
                string letters = letter.ToString().ToLower();
                letter = char.Parse(letters);
                CheckLetter(letter);
            }

        }
        public static void CheckLetter(char letter)
        {


            int nieoccuringLetters = 0;
            bool isUsed = false;
            for (int i = 0; i< occuringLetters.Length; i++)
            {
                occuringLetters[i] = 0;
            }
            for (int i = 0; i < used.Length; i++)
            {
                if (used[i] == letter)
                {
                    isUsed = true;
                }
            }
            if (isUsed == false)
            {
                for (int i = 0; i < used.Length; i++)
                {
                    if (used[i] == '8')
                    {
                        used[i] = letter;
                        break;
                    }
                }                
            }
            for (int i = 0; i < generatedWord.Length; i++)
            {
                if (generatedWord[i] == letter)
                {
                    occuringLetters[i] = 1;
                }
                else
                {
                    nieoccuringLetters++;
                }
            }
            if (nieoccuringLetters == generatedWord.Length)
            {
                if (hangman < 10)
                {
                    if (isUsed == false)
                    {
                        hangman = hangman + 1;
                    }
                    Play();
                }
                else
                {
                    Lose();
                }
            }
            else if (isUsed == true)
            {
                Console.Clear();
                Console.WriteLine("Letter have been used before!");
                Thread.Sleep(1000);
                Play();
            }
            else
            {
                char[] displayC = display.ToCharArray();
                display = "";
                for (int i = 0; i < displayC.Length; i++)
                {
                    if (occuringLetters[i] == 1 && displayC[i] == '_')
                    {
                        displayC[i] = letter;
                    }
                }
                for (int i = 0; i < displayC.Length; i++)
                {
                    display = display + displayC[i].ToString();
                    //displayC[i] = '8';
                }
                Play();
            }


        }
        public static void DisplayUsedLetters()
        {
            string used2 = "";
            for (int i = 0; i < used.Length; i++)
            {
                if (used[i] != '8')
                {
                    used2 = used2 + used[i].ToString() + ", ";
                }

            }
            Console.WriteLine("used letters: " + used2);
        }
        public static void DrawHangman()
        {
            Console.ForegroundColor = ConsoleColor.Red;
            switch (hangman)
            {
                case 1:
                    Console.WriteLine("");
                    Console.WriteLine("");
                    Console.WriteLine("");
                    Console.WriteLine("");
                    Console.WriteLine("");
                    Console.WriteLine("");
                    Console.WriteLine("  \\");
                    break;
                case 2:
                    Console.WriteLine("");
                    Console.WriteLine("");
                    Console.WriteLine("");
                    Console.WriteLine("");
                    Console.WriteLine("");
                    Console.WriteLine("");
                    Console.WriteLine("/|\\");
                    break;
                case 3:
                    Console.WriteLine("");
                    Console.WriteLine("");
                    Console.WriteLine("");
                    Console.WriteLine(" |");
                    Console.WriteLine(" |");
                    Console.WriteLine(" |");
                    Console.WriteLine("/|\\");
                    break;
                case 4:
                    Console.WriteLine(" |");
                    Console.WriteLine(" |");
                    Console.WriteLine(" |");
                    Console.WriteLine(" |");
                    Console.WriteLine(" |");
                    Console.WriteLine(" |");
                    Console.WriteLine("/|\\");
                    break;
                case 5:
                    Console.WriteLine(" |----");
                    Console.WriteLine(" |");
                    Console.WriteLine(" |");
                    Console.WriteLine(" |");
                    Console.WriteLine(" |");
                    Console.WriteLine(" |");
                    Console.WriteLine("/|\\");
                    break;
                case 6:
                    Console.WriteLine(" |----");
                    Console.WriteLine(" |   |");
                    Console.WriteLine(" |");
                    Console.WriteLine(" |");
                    Console.WriteLine(" |");
                    Console.WriteLine(" |");
                    Console.WriteLine("/|\\");
                    break;
                case 7:
                    Console.WriteLine(" |----");
                    Console.WriteLine(" |   |");
                    Console.WriteLine(" |   O");
                    Console.WriteLine(" |");
                    Console.WriteLine(" |");
                    Console.WriteLine(" |");
                    Console.WriteLine("/|\\");
                    break;
                case 8:
                    Console.WriteLine(" |----");
                    Console.WriteLine(" |   |");
                    Console.WriteLine(" |   O");
                    Console.WriteLine(" |  /|\\");
                    Console.WriteLine(" |");
                    Console.WriteLine(" |");
                    Console.WriteLine("/|\\");
                    break;
                case 9:
                    Console.WriteLine(" |----");
                    Console.WriteLine(" |   |");
                    Console.WriteLine(" |   O");
                    Console.WriteLine(" |  /|\\");
                    Console.WriteLine(" |   |");
                    Console.WriteLine(" |");
                    Console.WriteLine("/|\\");
                    break;
                case 10:
                    Console.WriteLine(" |----");
                    Console.WriteLine(" |   |");
                    Console.WriteLine(" |   O");
                    Console.WriteLine(" |  /|\\");
                    Console.WriteLine(" |   |");
                    Console.WriteLine(" |  /|\\");
                    Console.WriteLine("/|\\");
                    break;
                default:
                    Console.WriteLine("There is no hangman yet ;)");
                    break;
            }
        }
        static public void Lose()
        {
            RysujWisielca();
            Console.ForegroundColor = ConsoleColor.DarkRed;
            Console.WriteLine("You lost :<");
            Console.ForegroundColor = ConsoleColor.White;
            Console.WriteLine();
            Console.WriteLine("Word: " + generatedWord);
            Console.ForegroundColor = ConsoleColor.White;
            Wyswietlused();
            Console.WriteLine();
            DoYouWantToPlayAgain();
        }
        static public void DoYouWantToPlayAgain()
        {
            Console.ForegroundColor = ConsoleColor.Magenta;
            Console.WriteLine("If you want to play again press 2");
            Console.ForegroundColor = ConsoleColor.White;
            if (Console.ReadKey(true).KeyChar == 50)
            {
                Hello();
            }
        }
        public static void Win()
        {
            Console.Clear();
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("You win!");
            Console.ForegroundColor = ConsoleColor.DarkCyan;
            Console.WriteLine("To see a hangman and word press 1.");
            Console.ForegroundColor = ConsoleColor.Magenta;
            Console.WriteLine("If you want to play again press 2");
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Press something else to end.");
            Console.ForegroundColor = ConsoleColor.White;
            if (Console.ReadKey(true).KeyChar == 49)
            {
                DrawHangman();
                Console.WriteLine();
                Console.WriteLine("Word: " + generatedWord);
                Console.ForegroundColor = ConsoleColor.White;
                DisplayUsedLetters();
                Console.WriteLine();
                DoYouWantToPlayAgain();
            }
            else if (Console.ReadKey(true).KeyChar == 50)
            {
                Hello();
            }
        }
    }
}
