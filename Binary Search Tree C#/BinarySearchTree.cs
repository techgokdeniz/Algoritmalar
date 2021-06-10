using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BinarySearch
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] sayilar = { 1, 2, 3, 4, 5, 6 };
            /* Binary Search Arama Algoritması'nı kullanabilmek için elimizde sıralı bir dizi olması gerekmektedir.
             * eğer kullanacağım dizi sıralı değil ise sıralama algoritmaları ile sıralamak gerekemtektedir.*/

            int kucuk = 0, orta, buyuk=sayilar.Length-1, Aranan = 4;
            while(kucuk<=buyuk)
            {
                orta = (kucuk + buyuk) / 2;
                if (Aranan == sayilar[orta]) { Console.WriteLine("Aranan Sayı Dizinin {0}.elemanı", orta); break; }
                else if (Aranan < sayilar[orta]) { buyuk = orta - 1; }
                else { kucuk = orta + 1; }
            }
            Console.ReadKey();
        }
    }
}
