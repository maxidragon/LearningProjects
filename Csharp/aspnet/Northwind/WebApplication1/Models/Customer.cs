using WebApplication1.Models;

namespace WebApplication1.Models
{
    public class Customer
    {
        public int CustomerId { get; set; }
        public string CustomerName { get; set; }
        public string ContactName { get; set; }
        public string Adress { get; set; }
        public string City { get; set; }
        public string PostalCode { get; set; }
        public string Country { get; set; }
        public List<Order>? Orders { get; set; }
    }
}
