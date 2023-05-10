using WebApplication1.Models;

namespace WebApplication1.Models
{
    public class Order
    {
        public int OrderId { get; set; }
        public DateTime OrderDate { get; set; }
        public int CustomerId { get; set; }
        public Customer? Customer { get; set; }
        public int EmployeeID { get; set; }
        public Employee? Employee { get; set; }
        public int ShipperId { get; set; }
        public Shipper? Shipper { get; set; }
        public List<OrderDetails>? OrderDetails { get; set; }
    }
}
