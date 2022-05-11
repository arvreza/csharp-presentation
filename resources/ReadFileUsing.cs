void ReadFile(string fileName)
{
  using (StreamReader reader = File.OpenText (fileName))
  {
    if (reader.EndOfStream) return;
    Console.WriteLine (reader.ReadToEnd());
  }
}