namespace WebApplication1.Models.ViewModels
{
    public class OrderViewModel
    {
        public int OrderId { get; set; }
        public DateTime OrderDate { get; set; }
        public int CustomerId { get; set; }
        public Customer? Customer { get; set; }
        public int EmployeeID { get; set; }
        public Employee? Employee { get; set; }
        public int ShipperId { get; set; }
        public Shipper? Shipper { get; set; }
        public List<OrderDetails> OrderDetailsList { get; set; }
    }
}
