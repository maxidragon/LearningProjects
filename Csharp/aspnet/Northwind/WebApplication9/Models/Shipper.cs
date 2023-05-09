namespace WebApplication9.Models
{
    public class Shipper
    {
        public int ShipperId { get; set; }
        public string ShipperName { get; set; }
        public string Phone { get; set; }  
        public List<Order>? Orders { get; set; }

    }
}
