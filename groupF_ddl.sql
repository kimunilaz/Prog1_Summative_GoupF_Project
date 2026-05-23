DROP DATABASE IF EXISTS groupF_shop;
CREATE DATABASE groupF_shop
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE groupF_shop;

CREATE TABLE Products (
    product_id      VARCHAR(10)     NOT NULL,
    name            VARCHAR(100)    NOT NULL,
    category        VARCHAR(50)     NOT NULL DEFAULT 'General',
    unit            VARCHAR(20)     NOT NULL DEFAULT 'unit',

    CONSTRAINT pk_products          PRIMARY KEY (product_id),
    CONSTRAINT uq_products_name     UNIQUE (name),
    CONSTRAINT ck_products_id       CHECK (product_id REGEXP '^P[0-9]{3}$')
);

CREATE TABLE Batches (
    product_id      VARCHAR(10)     NOT NULL,
    batch_number    VARCHAR(10)     NOT NULL,
    price           DECIMAL(10,2)   NOT NULL,
    quantity        INT             NOT NULL DEFAULT 0,
    expiry_date     DATE            NOT NULL,

    CONSTRAINT pk_batches           PRIMARY KEY (product_id, batch_number),
    CONSTRAINT fk_batches_product   FOREIGN KEY (product_id)
                                    REFERENCES Products(product_id)
                                    ON DELETE RESTRICT
                                    ON UPDATE CASCADE,
    CONSTRAINT ck_batches_price     CHECK (price > 0),
    CONSTRAINT ck_batches_qty       CHECK (quantity >= 0),
    CONSTRAINT ck_batch_number      CHECK (batch_number REGEXP '^B[0-9]{3}$')
);

CREATE TABLE Sales (
    sale_id         VARCHAR(10)     NOT NULL,
    product_id      VARCHAR(10)     NOT NULL,
    batch_number    VARCHAR(10)     NOT NULL,
    quantity_sold   INT             NOT NULL,
    price           DECIMAL(10,2)   NOT NULL,
    date_of_sale    DATE            NOT NULL,

    CONSTRAINT pk_sales             PRIMARY KEY (sale_id),
    CONSTRAINT fk_sales_batch       FOREIGN KEY (product_id, batch_number)
                                    REFERENCES Batches(product_id, batch_number)
                                    ON DELETE RESTRICT
                                    ON UPDATE CASCADE,
    CONSTRAINT ck_sales_qty         CHECK (quantity_sold > 0),
    CONSTRAINT ck_sales_price       CHECK (price > 0),
    CONSTRAINT ck_sales_id          CHECK (sale_id REGEXP '^S[0-9]{3}$')
);

CREATE TABLE RemovedProducts (
    removal_id      INT             NOT NULL AUTO_INCREMENT,
    product_id      VARCHAR(10),
    batch_number    VARCHAR(10),
    removal_reason  VARCHAR(50)     NOT NULL DEFAULT 'Expired',
    removal_date    DATE            NOT NULL,

    CONSTRAINT pk_removed           PRIMARY KEY (removal_id),
    CONSTRAINT fk_removed_batch     FOREIGN KEY (product_id, batch_number)
                                    REFERENCES Batches(product_id, batch_number)
                                    ON DELETE SET NULL
                                    ON UPDATE CASCADE,
    CONSTRAINT ck_removed_reason    CHECK (removal_reason IN
                                    ('Expired', 'Damaged', 'Recalled', 'Other'))
);
