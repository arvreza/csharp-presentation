static void Hello(string name) 
{
    if (name == null) throw new ArgumentNullException(nameof(name));

    Console.WriteLine($"Hello {name}!");
}
