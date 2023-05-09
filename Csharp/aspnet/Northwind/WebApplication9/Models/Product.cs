namespace WebApplication9.Models
{
    public class Product
    {
        public int ProductId { get; set; }
        public string ProductName { get; set; }
        public string Unit { get; set; }
        public decimal Price { get; set; }
        public int CategoryId { get; set; }
        public Category? Category { get; set; }
        public int SupplierId { get; set; }
        public Supplier? Supplier { get; set; }
    }
}
