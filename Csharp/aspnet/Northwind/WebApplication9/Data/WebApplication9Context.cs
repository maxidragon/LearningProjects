using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using WebApplication9.Models;

namespace WebApplication9.Data
{
    public class WebApplication9Context : DbContext
    {
        public WebApplication9Context (DbContextOptions<WebApplication9Context> options)
            : base(options)
        {
        }

        public DbSet<WebApplication9.Models.Product>? Product { get; set; }

        public DbSet<WebApplication9.Models.Category>? Category { get; set; }

        public DbSet<WebApplication9.Models.Customer>? Customer { get; set; }

        public DbSet<WebApplication9.Models.Employee>? Employee { get; set; }

        public DbSet<WebApplication9.Models.Order>? Order { get; set; }

        public DbSet<WebApplication9.Models.Shipper>? Shipper { get; set; }

        public DbSet<WebApplication9.Models.Supplier>? Supplier { get; set; }
    }
}
