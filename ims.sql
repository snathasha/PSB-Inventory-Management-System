-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Sep 26, 2021 at 03:17 PM
-- Server version: 8.0.26-0ubuntu0.20.04.2
-- PHP Version: 7.4.23

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ims`
--

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--

CREATE TABLE `admins` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `admins`
--

INSERT INTO `admins` (`id`, `name`, `username`, `password`) VALUES
(1, 'Admin', 'admin', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `employee_no` varchar(100) NOT NULL,
  `registered_at` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `employees`
--

INSERT INTO `employees` (`id`, `name`, `employee_no`, `registered_at`) VALUES
(1, 'Karen R. Schmidt', 'KS2021', '2021-09-22'),
(2, 'Norman M. Millan', 'NM2021', '2021-09-22'),
(3, 'Sheri M. Boutte', 'SM2021', '2021-09-22'),
(4, 'Test', '42424', '2021-09-21'),
(5, 'gihan', '444', '2021-08-21'),
(6, 'test1', 'eqeqe', '2021-08-21'),
(7, ';k', '5353', '2021-08-21'),
(9, 'fsfsfs', '5353fafa', '2021-08-21'),
(10, 'ggdg', 'gdgd', '2021-08-21'),
(12, 'fafafaf', 'fafaf', '2021-08-21'),
(13, 'fafafa', 'fafafaf', '2021-08-21'),
(14, 'fafafafafa', 'fafafaffaf', '2021-08-26');

-- --------------------------------------------------------

--
-- Table structure for table `employee_items`
--

CREATE TABLE `employee_items` (
  `employee_id` int NOT NULL,
  `item_id` int NOT NULL,
  `qty` int NOT NULL,
  `assigned_at` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `employee_items`
--

INSERT INTO `employee_items` (`employee_id`, `item_id`, `qty`, `assigned_at`) VALUES
(6, 2, 3, '2021-09-21'),
(6, 11, 5, '2021-09-09'),
(5, 5, 5, '2021-09-09'),
(4, 2, 5, '2019-09-07');

-- --------------------------------------------------------

--
-- Table structure for table `items`
--

CREATE TABLE `items` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `category` varchar(50) NOT NULL,
  `qty` int NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `items`
--

INSERT INTO `items` (`id`, `name`, `category`, `qty`, `price`, `date`) VALUES
(1, 'pen', 'stationery', 1, '10.00', '2021-09-21'),
(2, 'ruler', 'stationery', 5, '15.00', '2021-09-21'),
(5, 'test A', 'test cate A', 67, '68.00', '2020-04-01'),
(6, 'marker', 'Stationary', 23, '25.00', '2021-09-21'),
(7, 'key', 'test', 10, '30.00', '2021-09-22'),
(9, 'testee', 'rewe', 33, '2.00', '2021-09-21'),
(11, 'printer', 'electric', 3, '5000.00', '2021-09-21'),
(12, 'item 1 ', 'Stationary', 1, '45.00', '2020-04-01'),
(13, 'eraser', 'Stationary', 10, '35.00', '2021-09-22'),
(14, 'laptop', 'Electric', 10, '30.00', '2021-09-22');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `employees`
--
ALTER TABLE `employees`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `employee_no` (`employee_no`);

--
-- Indexes for table `employee_items`
--
ALTER TABLE `employee_items`
  ADD KEY `employee_id` (`employee_id`),
  ADD KEY `item_id` (`item_id`);

--
-- Indexes for table `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admins`
--
ALTER TABLE `admins`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `employees`
--
ALTER TABLE `employees`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `items`
--
ALTER TABLE `items`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `employee_items`
--
ALTER TABLE `employee_items`
  ADD CONSTRAINT `employee_items_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `employee_items_ibfk_2` FOREIGN KEY (`item_id`) REFERENCES `items` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
