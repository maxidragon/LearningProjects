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
    public class ProductsController : Controller
    {
        private readonly WebApplication1Context _context;

        public ProductsController(WebApplication1Context context)
        {
            _context = context;
        }

        // GET: Products
        public async Task<IActionResult> Index()
        {
            var webApplication1Context = _context.Product.Include(p => p.Category).Include(p => p.Supplier);
            return View(await webApplication1Context.ToListAsync());
        }
        [HttpPost]
        public async Task<IActionResult> Index(string PriceFromS, string PriceToS)
        {
            decimal PriceFrom;
            decimal PriceTo;
            decimal.TryParse(PriceFromS, out PriceFrom);
            decimal.TryParse(PriceToS, out PriceTo);
            if (PriceTo != 0)
            {
                var webApplication1Context = _context.Product.Include(p => p.Category).Include(p => p.Supplier)
                    .Where(p => p.Price > PriceFrom).Where(p => p.Price < PriceTo);
                return View(await webApplication1Context.ToListAsync());
            }
            else
            {
                var webApplication1Context = _context.Product.Include(p => p.Category).Include(p => p.Supplier)
    .Where(p => p.Price > PriceFrom);
                return View(await webApplication1Context.ToListAsync());
            }
        }

        public async Task<IActionResult> ShowProductsFromCategory(int? id)
        {
            //var products = from p in _context.Product
            //               where p.CategoryId == id
            //               select p;
            var products = _context.Product
                .Include(p => p.Category)
                .Include(p => p.Supplier)
                .Where(p => p.CategoryId == id);
            return View(await products.ToListAsync());
        }    
        public async Task<IActionResult> ShowProductsWithPriceGreaterThan(int? price)
        {
            //var products = from p in _context.Product
            //               where p.CategoryId == id
            //               select p;
            var products = _context.Product
                .Include(p => p.Category)
                .Include(p => p.Supplier)
                .Where(p => p.Price > price);
            return View(await products.ToListAsync());
        }

        // GET: Products/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null || _context.Product == null)
            {
                return NotFound();
            }

            var product = await _context.Product
                .Include(p => p.Category)
                .Include(p => p.Supplier)
                .FirstOrDefaultAsync(m => m.ProductId == id);
            if (product == null)
            {
                return NotFound();
            }

            return View(product);
        }

        // GET: Products/Create
        public IActionResult Create()
        {
            ViewData["CategoryId"] = new SelectList(_context.Category, "CategoryId", "CategoryName");
            ViewData["SupplierId"] = new SelectList(_context.Set<Supplier>(), "SupplierId", "SupplierName");
            return View();
        }

        // POST: Products/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("ProductId,ProductName,Unit,Price,CategoryId,SupplierId")] Product product)
        {
            if (ModelState.IsValid)
            {
                _context.Add(product);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            ViewData["CategoryId"] = new SelectList(_context.Category, "CategoryId", "CategoryName", product.CategoryId);
            ViewData["SupplierId"] = new SelectList(_context.Set<Supplier>(), "SupplierId", "SupplierName", product.SupplierId);
            return View(product);
        }

        // GET: Products/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null || _context.Product == null)
            {
                return NotFound();
            }

            var product = await _context.Product.FindAsync(id);
            if (product == null)
            {
                return NotFound();
            }
            ViewData["CategoryId"] = new SelectList(_context.Category, "CategoryId", "CategoryId", product.CategoryId);
            ViewData["SupplierId"] = new SelectList(_context.Set<Supplier>(), "SupplierId", "SupplierId", product.SupplierId);
            return View(product);
        }

        // POST: Products/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("ProductId,ProductName,Unit,Price,CategoryId,SupplierId")] Product product)
        {
            if (id != product.ProductId)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(product);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!ProductExists(product.ProductId))
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
            ViewData["CategoryId"] = new SelectList(_context.Category, "CategoryId", "CategoryId", product.CategoryId);
            ViewData["SupplierId"] = new SelectList(_context.Set<Supplier>(), "SupplierId", "SupplierId", product.SupplierId);
            return View(product);
        }

        // GET: Products/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null || _context.Product == null)
            {
                return NotFound();
            }

            var product = await _context.Product
                .Include(p => p.Category)
                .Include(p => p.Supplier)
                .FirstOrDefaultAsync(m => m.ProductId == id);
            if (product == null)
            {
                return NotFound();
            }

            return View(product);
        }

        // POST: Products/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            if (_context.Product == null)
            {
                return Problem("Entity set 'WebApplication1Context.Product'  is null.");
            }
            var product = await _context.Product.FindAsync(id);
            if (product != null)
            {
                _context.Product.Remove(product);
            }
            
            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool ProductExists(int id)
        {
          return _context.Product.Any(e => e.ProductId == id);
        }
    }
}
