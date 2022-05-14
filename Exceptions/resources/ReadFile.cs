void ReadFile(string fileName)
{
  StreamReader reader = null;    
  try
  {
    reader = File.OpenText (fileName); 
    if (reader.EndOfStream) return;
    Console.WriteLine (reader.ReadToEnd());
  }
  finally
  {
    if (reader != null) reader.Dispose();
  }
}