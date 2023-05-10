using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using WebApplication1.Data;
using WebApplication1.Models;

namespace WebApplication1.Controllers
{
    public class CustomersController : Controller
    {
        private readonly WebApplication1Context _context;

        public CustomersController(WebApplication1Context context)
        {
            _context = context;
        }

        // GET: Customers
        //public async Task<IActionResult> Index()
        //{
        //      return View(await _context.Customer.ToListAsync());
        //}
        public async Task<IActionResult> Index(string sortOrder, string currentFilter, string searchString, int? pageNumber)
        {
            ViewData["NameSortParm"] = String.IsNullOrEmpty(sortOrder) ? "name_desc" : "name";
            ViewData["AdressSortParam"] = sortOrder == "adress" ? "adress_desc" : "adress";
            ViewData["CitySortParam"] = sortOrder == "city" ? "city_desc" : "city";
            ViewData["PostalCodeSortParam"] = sortOrder == "PostalCode" ? "postalcode_desc" : "PostalCode";
            if (searchString != null)
            {
                pageNumber = 1;
            }
            else
            {
                searchString = currentFilter;
                
            }
            ViewData["CurrentFilter"] = searchString;
            ViewData["CurrentSort"] = sortOrder;
            var customers = from s in _context.Customer
                           select s;
            if (!String.IsNullOrEmpty(searchString))
            {
                customers = customers.Where(s => s.CustomerName.Contains(searchString)
                                       || s.ContactName.Contains(searchString)
                                       || s.Adress.Contains(searchString)
                                       || s.City.Contains(searchString)
                                       || s.PostalCode.Contains(searchString)
                                       || s.Country.Contains(searchString));
            }
            switch (sortOrder)
            {
                case "name":
                    customers = customers.OrderBy(s => s.CustomerName);
                    break;
                case "name_desc":
                    customers = customers.OrderByDescending(s => s.CustomerName);
                    break;
                case "adress_desc":
                    customers = customers.OrderByDescending(s => s.Adress);
                    break;
                case "adress":
                    customers = customers.OrderBy(s => s.Adress);
                    break;             
                case "city_desc":
                    customers = customers.OrderByDescending(s => s.City);
                    break;
                case "city":
                    customers = customers.OrderBy(s => s.City);
                    break;   
                case "postalcode_desc":
                    customers = customers.OrderByDescending(s => s.PostalCode);
                    break;
                case "PostalCode":
                    customers = customers.OrderBy(s => s.PostalCode);
                    break;
                default:
                    customers = customers.OrderBy(s => s.CustomerId);
                    break;
            }
            int pageSize = 5;
            return View(await PaginatedList<Customer>.CreateAsync(customers.AsNoTracking(),pageNumber ?? 1,pageSize));
        }

        // GET: Customers/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null || _context.Customer == null)
            {
                return NotFound();
            }

            var customer = await _context.Customer
                .FirstOrDefaultAsync(m => m.CustomerId == id);
            if (customer == null)
            {
                return NotFound();
            }

            return View(customer);
        }

        // GET: Customers/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: Customers/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("CustomerId,CustomerName,ContactName,Adress,City,PostalCode,Country")] Customer customer)
        {
            if (ModelState.IsValid)
            {
                _context.Add(customer);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            return View(customer);
        }

        // GET: Customers/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null || _context.Customer == null)
            {
                return NotFound();
            }

            var customer = await _context.Customer.FindAsync(id);
            if (customer == null)
            {
                return NotFound();
            }
            return View(customer);
        }

        // POST: Customers/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("CustomerId,CustomerName,ContactName,Adress,City,PostalCode,Country")] Customer customer)
        {
            if (id != customer.CustomerId)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(customer);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!CustomerExists(customer.CustomerId))
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
            return View(customer);
        }

        // GET: Customers/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null || _context.Customer == null)
            {
                return NotFound();
            }

            var customer = await _context.Customer
                .FirstOrDefaultAsync(m => m.CustomerId == id);
            if (customer == null)
            {
                return NotFound();
            }

            return View(customer);
        }

        // POST: Customers/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            if (_context.Customer == null)
            {
                return Problem("Entity set 'WebApplication1Context.Customer'  is null.");
            }
            var customer = await _context.Customer.FindAsync(id);
            if (customer != null)
            {
                _context.Customer.Remove(customer);
            }
            
            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool CustomerExists(int id)
        {
          return _context.Customer.Any(e => e.CustomerId == id);
        }
    }
}
