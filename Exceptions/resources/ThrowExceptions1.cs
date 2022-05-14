static void Hello(string name) 
{
    ArgumentNullException.ThrowIfNull (name);

    Console.WriteLine($"Hello {name}!");
}
