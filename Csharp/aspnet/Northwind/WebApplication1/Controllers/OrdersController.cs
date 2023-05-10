using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using WebApplication1.Data;
using WebApplication1.Models;
using WebApplication1.Models.ViewModels;

namespace WebApplication1.Controllers
{
    public class OrdersController : Controller
    {
        private readonly WebApplication1Context _context;

        public OrdersController(WebApplication1Context context)
        {
            _context = context;
        }

        // GET: Orders
        public async Task<IActionResult> Index()
        {
            var webApplication1Context = _context.Order.Include(o => o.Customer).Include(o => o.Employee).Include(o => o.Shipper);
            return View(await webApplication1Context.ToListAsync());
        }

        // GET: Orders/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null || _context.Order == null)
            {
                return NotFound();
            }

            var order = await _context.Order
                .Include(o => o.Customer)
                .Include(o => o.Employee)
                .Include(o => o.Shipper)
                .FirstOrDefaultAsync(m => m.OrderId == id);
            if (order == null)
            {
                return NotFound();
            }

            return View(order);
        }

        // GET: Orders/Create
        public IActionResult Create()
        {
            ViewData["CustomerId"] = new SelectList(_context.Customer, "CustomerId", "CustomerName");
            ViewData["EmployeeID"] = new SelectList(_context.Employee, "EmployeeId", "LastName");
            ViewData["ShipperId"] = new SelectList(_context.Shipper, "ShipperId", "ShipperName");
            return View();
        }
        public IActionResult CreateOrderWithDetails()
        {
            ViewData["CustomerId"] = new SelectList(_context.Customer, "CustomerId", "CustomerName");
            ViewData["EmployeeID"] = new SelectList(_context.Employee, "EmployeeId", "LastName");
            ViewData["ShipperId"] = new SelectList(_context.Shipper, "ShipperId", "ShipperName");
            ViewData["ProductId"] = new SelectList(_context.Product, "ProductId", "ProductName");
            return View();
        }
        [HttpPost]
        public async Task<IActionResult> CreateOrderWithDetails(OrderViewModel order)
            {
            Order order1 = new Order 
            {
                OrderDate = order.OrderDate,
                EmployeeID = order.EmployeeID,
                CustomerId = order.CustomerId,
                ShipperId = order.ShipperId
            };
            _context.Order.Add(order1);
            await _context.SaveChangesAsync();
            foreach (var detail in order.OrderDetailsList)
            {
                OrderDetails detail2 = new OrderDetails
                {
                    OrderId = order1.OrderId,
                    ProductId = detail.ProductId,
                    Quantity = detail.Quantity
                };
                _context.OrderDetails.Add(detail2);
            }
            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
            ViewData["CustomerId"] = new SelectList(_context.Customer, "CustomerId", "CustomerName");
            ViewData["EmployeeID"] = new SelectList(_context.Employee, "EmployeeId", "LastName");
            ViewData["ShipperId"] = new SelectList(_context.Shipper, "ShipperId", "ShipperName");
            ViewData["ProductId"] = new SelectList(_context.Product, "ProductId", "ProductName");
            return View();
        }
        // POST: Orders/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("OrderId,OrderDate,CustomerId,EmployeeID,ShipperId")] Order order)
        {
            if (ModelState.IsValid)
            {
                _context.Add(order);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            ViewData["CustomerId"] = new SelectList(_context.Customer, "CustomerId", "CustomerId", order.CustomerId);
            ViewData["EmployeeID"] = new SelectList(_context.Employee, "EmployeeId", "EmployeeId", order.EmployeeID);
            ViewData["ShipperId"] = new SelectList(_context.Shipper, "ShipperId", "ShipperId", order.ShipperId);
            return View(order);
        }

        // GET: Orders/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null || _context.Order == null)
            {
                return NotFound();
            }

            var order = await _context.Order.FindAsync(id);
            if (order == null)
            {
                return NotFound();
            }
            ViewData["CustomerId"] = new SelectList(_context.Customer, "CustomerId", "CustomerId", order.CustomerId);
            ViewData["EmployeeID"] = new SelectList(_context.Employee, "EmployeeId", "EmployeeId", order.EmployeeID);
            ViewData["ShipperId"] = new SelectList(_context.Shipper, "ShipperId", "ShipperId", order.ShipperId);
            return View(order);
        }

        // POST: Orders/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("OrderId,OrderDate,CustomerId,EmployeeID,ShipperId")] Order order)
        {
            if (id != order.OrderId)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(order);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!OrderExists(order.OrderId))
                    {
                        return NotFound();
                    }
                    else
                    {
                        throw;
                    }
                }
                return RedirectToAction(nameof(Index));
            }
            ViewData["CustomerId"] = new SelectList(_context.Customer, "CustomerId", "CustomerId", order.CustomerId);
            ViewData["EmployeeID"] = new SelectList(_context.Employee, "EmployeeId", "EmployeeId", order.EmployeeID);
            ViewData["ShipperId"] = new SelectList(_context.Shipper, "ShipperId", "ShipperId", order.ShipperId);
            return View(order);
        }

        // GET: Orders/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null || _context.Order == null)
            {
                return NotFound();
            }

            var order = await _context.Order
                .Include(o => o.Customer)
                .Include(o => o.Employee)
                .Include(o => o.Shipper)
                .FirstOrDefaultAsync(m => m.OrderId == id);
            if (order == null)
            {
                return NotFound();
            }

            return View(order);
        }

        // POST: Orders/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            if (_context.Order == null)
            {
                return Problem("Entity set 'WebApplication1Context.Order'  is null.");
            }
            var order = await _context.Order.FindAsync(id);
            if (order != null)
            {
                _context.Order.Remove(order);
            }
            
            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool OrderExists(int id)
        {
          return _context.Order.Any(e => e.OrderId == id);
        }
    }
}
