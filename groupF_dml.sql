USE groupF_shop;

INSERT INTO Products (product_id, name, category, unit) VALUES
    ('P001', 'Sugar',       'Dry Goods',  'kg'),
    ('P002', 'Milk',        'Dairy',      'litre'),
    ('P003', 'Bread',       'Bakery',     'loaf'),
    ('P004', 'Butter',      'Dairy',      'pack'),
    ('P005', 'Oats',        'Dry Goods',  'kg'),
    ('P006', 'Orange Juice','Beverages',  'litre');


INSERT INTO Batches (product_id, batch_number, price, quantity, expiry_date) VALUES
    ('P001', 'B001', 2500.00,  10, '2026-12-31'),
    ('P002', 'B001', 1500.00,  20, '2026-03-15'),
    ('P002', 'B002', 1550.00,  15, '2026-05-20'),
    ('P003', 'B001', 1200.00,   5, '2026-01-10'),
    ('P004', 'B001', 3500.00,   5, '2026-03-05'),
    ('P005', 'B001',  230.00,  32, '2029-02-02'),
    ('P005', 'B002',  245.00,  18, '2030-01-01'),
    ('P006', 'B001',  850.00,  25, '2026-08-30');

INSERT INTO Sales (sale_id, product_id, batch_number, quantity_sold, price_per_unit, total_amount, date_of_sale) VALUES
    ('S001', 'P001', 'B001', 2, 2500.00,  5000.00, '2026-01-05'),
    ('S002', 'P002', 'B001', 1, 1500.00,  1500.00, '2026-01-06'),
    ('S003', 'P003', 'B001', 5, 1200.00,  6000.00, '2026-01-07'),
    ('S004', 'P004', 'B001', 2, 3500.00,  7000.00, '2026-01-08'),
    ('S005', 'P005', 'B001', 4,  230.00,   920.00, '2026-01-09'),
    ('S006', 'P006', 'B001', 3,  850.00,  2550.00, '2026-01-10'),
    ('S007', 'P001', 'B001', 1, 2500.00,  2500.00, '2026-01-11');

INSERT INTO RemovedProducts (product_id, batch_number, product_name, price_at_removal, quantity_removed, expiry_date, removal_reason, removal_date) VALUES
    ('P003', 'B001', 'Bread',        1200.00, 15, '2026-01-10', 'Expired',  '2026-01-14'),
    ('P002', 'B001', 'Milk',         1500.00,  3, '2026-03-15', 'Damaged',  '2026-02-01'),
    ('P004', 'B001', 'Butter',       3500.00,  2, '2026-03-05', 'Expired',  '2026-03-06'),
    ('P005', 'B001', 'Oats',          230.00,  5, '2029-02-02', 'Recalled', '2026-04-01'),
    ('P006', 'B001', 'Orange Juice',  850.00,  1, '2026-08-30', 'Damaged',  '2026-05-01');

-- Uncomment the line below to test the FK violation:
-- INSERT INTO Sales (sale_id, product_id, batch_number, quantity_sold, price_per_unit, total_amount, date_of_sale)
--  VALUES ('S999', 'P999', 'B999', 1, 100.00, 100.00, '2026-01-15');

