using System.Text;

static void ReadCSV(string path)
{
    try
    {
        using (FileStream fs = new FileStream(path, FileMode.Open))
        {
            using (StreamReader sr = new StreamReader(fs, Encoding.UTF8, false))
            {
                string lines = null;
                string[] keys = null;
                string[] values = null;

                while ((lines = sr.ReadLine()) != null)
                {
                    if (string.IsNullOrEmpty(lines)) 
                        return;

                    values = lines.Split(',');  // 콤마로 분리

                    for (int i = 0; i < values.Length; i++)
                    {
                        Console.Write(values[i]);
                        if (i != values.Length - 1)
                            Console.Write(", ");
                    }

                    Console.WriteLine();
                }
            }
        }
    }
    catch (Exception e)
    {
        Console.WriteLine(e.ToString());
    }
}

string path = "D:\\GItSource\\TOGServer\\Tracking\\Raw.csv";

ReadCSV(path);