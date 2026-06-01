CREATE DATABASE  IF NOT EXISTS `groupf_shop` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `groupf_shop`;
-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: groupf_shop
-- ------------------------------------------------------
-- Server version	8.0.45

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `batches`
--

DROP TABLE IF EXISTS `batches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `batches` (
  `product_id` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `batch_number` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `quantity` int NOT NULL DEFAULT '0',
  `expiry_date` date NOT NULL,
  PRIMARY KEY (`product_id`,`batch_number`),
  CONSTRAINT `fk_batches_product` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `ck_batch_number` CHECK (regexp_like(`batch_number`,_utf8mb4'^B[0-9]{3}$')),
  CONSTRAINT `ck_batches_price` CHECK ((`price` > 0)),
  CONSTRAINT `ck_batches_qty` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `batches`
--

LOCK TABLES `batches` WRITE;
/*!40000 ALTER TABLE `batches` DISABLE KEYS */;
/*!40000 ALTER TABLE `batches` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `product_id` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `category` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'General',
  `unit` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'unit',
  PRIMARY KEY (`product_id`),
  UNIQUE KEY `uq_products_name` (`name`),
  CONSTRAINT `ck_products_id` CHECK (regexp_like(`product_id`,_utf8mb4'^P[0-9]{3}$'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `removedproducts`
--

DROP TABLE IF EXISTS `removedproducts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `removedproducts` (
  `removal_id` int NOT NULL AUTO_INCREMENT,
  `product_id` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `batch_number` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `removal_reason` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'Expired',
  `removal_date` date NOT NULL,
  PRIMARY KEY (`removal_id`),
  KEY `fk_removed_batch` (`product_id`,`batch_number`),
  CONSTRAINT `fk_removed_batch` FOREIGN KEY (`product_id`, `batch_number`) REFERENCES `batches` (`product_id`, `batch_number`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `ck_removed_reason` CHECK ((`removal_reason` in (_utf8mb4'Expired',_utf8mb4'Damaged',_utf8mb4'Recalled',_utf8mb4'Other')))
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `removedproducts`
--

LOCK TABLES `removedproducts` WRITE;
/*!40000 ALTER TABLE `removedproducts` DISABLE KEYS */;
/*!40000 ALTER TABLE `removedproducts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales`
--

DROP TABLE IF EXISTS `sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales` (
  `sale_id` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `product_id` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `batch_number` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `quantity_sold` int NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `total_amount` decimal(12,2) NOT NULL,
  `date_of_sale` date NOT NULL,
  PRIMARY KEY (`sale_id`),
  KEY `fk_sales_batch` (`product_id`,`batch_number`),
  CONSTRAINT `fk_sales_batch` FOREIGN KEY (`product_id`, `batch_number`) REFERENCES `batches` (`product_id`, `batch_number`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `ck_sales_id` CHECK (regexp_like(`sale_id`,_utf8mb4'^S[0-9]{3}$')),
  CONSTRAINT `ck_sales_price` CHECK ((`price` > 0)),
  CONSTRAINT `ck_sales_qty` CHECK ((`quantity_sold` > 0)),
  CONSTRAINT `ck_sales_total` CHECK ((`total_amount` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales`
--

LOCK TABLES `sales` WRITE;
/*!40000 ALTER TABLE `sales` DISABLE KEYS */;
/*!40000 ALTER TABLE `sales` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-06-02  0:13:09
