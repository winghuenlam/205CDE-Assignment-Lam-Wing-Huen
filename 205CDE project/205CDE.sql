-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 09, 2019 at 08:27 PM
-- Server version: 5.7.25-0ubuntu0.16.04.2
-- PHP Version: 7.0.33-0ubuntu0.16.04.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `205CDE`
--

-- --------------------------------------------------------

--
-- Table structure for table `ExtraFacility`
--

CREATE TABLE `ExtraFacility` (
  `FacilityID` int(11) NOT NULL,
  `FacilityName` char(30) NOT NULL,
  `Price` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ExtraFacility`
--

INSERT INTO `ExtraFacility` (`FacilityID`, `FacilityName`, `Price`) VALUES
(1, 'Cookery Kitchen', 150),
(2, 'Professional Photo Taking', 200),
(3, '6-7 Person Menu Set', 750),
(4, '10-12 Person Menu Set', 1300),
(5, '18-22 Person Menu Set', 2300);

-- --------------------------------------------------------

--
-- Table structure for table `Feedback`
--

CREATE TABLE `Feedback` (
  `FeedbackID` int(11) NOT NULL,
  `Name` char(11) DEFAULT NULL,
  `Room` char(10) NOT NULL,
  `RoomRating` int(1) NOT NULL,
  `ServiceRating` int(1) NOT NULL,
  `Comment` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Feedback`
--

INSERT INTO `Feedback` (`FeedbackID`, `Name`, `Room`, `RoomRating`, `ServiceRating`, `Comment`) VALUES
(1, 'test', 'Room A', 5, 4, 'wow'),
(2, NULL, 'Room A', 1, 3, 'test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test !!@#$%$%1234564655gjjgfds'),
(3, 'john', 'Room A', 4, 5, 'Good'),
(4, 'try try', 'Room C', 4, 5, 'great'),
(5, 'Hohoho', 'Room C', 5, 5, 'higher score'),
(6, 'Mario Mar', 'Room B', 4, 4, 'trying not to break 1500 word count so tricky');

-- --------------------------------------------------------

--
-- Table structure for table `Member`
--

CREATE TABLE `Member` (
  `MemberID` int(11) NOT NULL,
  `FirstName` char(50) NOT NULL,
  `LastName` char(30) DEFAULT NULL,
  `Username` char(20) DEFAULT NULL,
  `Email` char(50) DEFAULT NULL,
  `Password` char(16) DEFAULT NULL,
  `ContactNumber` char(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Member`
--

INSERT INTO `Member` (`MemberID`, `FirstName`, `LastName`, `Username`, `Email`, `Password`, `ContactNumber`) VALUES
(1, 'Mishy', 'Le', 'ML1234', 'change125@abc.com', '1111qqqq', '2343-7650'),
(2, 'Charles', 'Cheung', 'CCeung', 'ccfdg@gmail.com', '12345qqq', '4536-6655'),
(3, 'Hayton', 'Ip', 'siuhay', 'siuhay@asdf.com', 'qqqwww11', '4354-7666'),
(4, 'Dai', 'Ko', 'daikoo', 'daikoo@deeds.com', 'daikoo123', '8787-9898'),
(5, 'Bailey', 'Chan', 'Bailey111', 'Bailey111@hjkl.com', '1234567qaq', '5675-8645'),
(6, 'Nio', 'Si', 'NS765', 'ns345@gmail.com', '6565656a', '7663-6789'),
(7, 'James', 'Ki', 'JK0987', 'xzj@dx.com', '55555aaa', '2357-7777'),
(8, 'Tyler', 'Ho', 'THO567', 'tylerho@tgyuh.com', '12345qwe', '5786-8577'),
(9, 'Dani', 'Rui', 'Danru', 'daniru123@gmail.com', '12345qwe', '4567-0000'),
(10, 'Charles', 'Wu', 'Charlie_Lau', 'charleswu@gmail.com', 'charlie123', '1212-7989');

-- --------------------------------------------------------

--
-- Table structure for table `MenuSetA_6To7`
--

CREATE TABLE `MenuSetA_6To7` (
  `ItemID` int(11) NOT NULL,
  `FoodItem` char(50) NOT NULL,
  `Quantity` float NOT NULL,
  `Unit` char(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `MenuSetA_6To7`
--

INSERT INTO `MenuSetA_6To7` (`ItemID`, `FoodItem`, `Quantity`, `Unit`) VALUES
(1, 'German Potato Salad', 1, 'lb'),
(2, 'Chicken Wings (Honey Sauce)', 12, 'pcs'),
(3, 'Enoki Mushroom and Beef Roll', 12, 'pcs'),
(4, 'Croissant with Cheese, Ham (Mustard Sauce)', 10, 'pcs'),
(5, 'Italian Meat Ball (Tomato Sauce)', 20, 'pcs'),
(6, 'Spaghetti Bolognese', 2, 'lb'),
(7, 'Yeung Chow Fried Rice', 1.5, 'lb'),
(10, 'Orange Juice', 2, 'liter');

-- --------------------------------------------------------

--
-- Table structure for table `MenuSetB_10To12`
--

CREATE TABLE `MenuSetB_10To12` (
  `ItemID` int(11) NOT NULL,
  `FoodItem` char(50) NOT NULL,
  `Quantity` float NOT NULL,
  `Unit` char(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `MenuSetB_10To12`
--

INSERT INTO `MenuSetB_10To12` (`ItemID`, `FoodItem`, `Quantity`, `Unit`) VALUES
(1, 'German Potato Salad', 1.2, 'lb'),
(2, 'Chicken Wings (Honey Sauce)', 18, 'pcs'),
(3, 'Enoki Mushroom and Beef Roll', 18, 'pcs'),
(4, 'Croissant with Cheese, Ham (Mustard Sauce)', 15, 'pcs'),
(5, 'Italian Meat Ball (Tomato Sauce)', 30, 'pcs'),
(6, 'Bake Potato with Sour Cream and Bacon', 1, 'lb'),
(7, 'Pan Fried Prawns', 12, 'pcs'),
(8, 'Roasted Lamb Rack with Herbs', 12, 'pcs'),
(9, 'Spaghetti Bolognese', 2, 'lb'),
(10, 'Yeung Chow Fried Rice', 1.5, 'lb'),
(11, 'Baked Spaghetti in Seafood (Cream Sauce)', 2, 'lb'),
(12, 'Orange Juice', 1.5, 'Liter'),
(15, 'Coca Cola', 1.5, 'liter');

-- --------------------------------------------------------

--
-- Table structure for table `MenuSetC_18To22`
--

CREATE TABLE `MenuSetC_18To22` (
  `ItemID` int(11) NOT NULL,
  `FoodItem` char(50) NOT NULL,
  `Quantity` float NOT NULL,
  `Unit` char(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `MenuSetC_18To22`
--

INSERT INTO `MenuSetC_18To22` (`ItemID`, `FoodItem`, `Quantity`, `Unit`) VALUES
(1, 'German Potato Salad', 1.2, 'lb'),
(2, 'Caesar Salad', 1.2, 'lb'),
(3, 'Chicken Wings (Honey Sauce)', 24, 'pcs'),
(4, 'Enoki Mushroom and Beef Roll', 30, 'pcs'),
(5, 'Croissant with Cheese, Ham (Mustard Sauce)', 25, 'pcs'),
(6, 'Italian Meat Ball (Tomato Sauce)', 50, 'pcs'),
(7, 'Mini Escargot Tart with Herb', 25, 'pcs'),
(8, 'Bake Potato with Sour Cream and Bacon', 1.5, 'lb'),
(9, 'Pan Fried Prawns', 22, 'pcs'),
(10, 'Roasted Lamb Rack with Herbs', 22, 'pcs'),
(11, 'Shrimp with Pinapple (Sweet and Sour Sauce)', 2, 'lb'),
(12, 'Bolognese', 2.5, 'lb'),
(13, 'Yeung Chow Fried Rice', 2.5, 'lb'),
(14, 'Baked Spaghetti in Seafood (Cream Sauce)', 2.5, 'lb'),
(15, 'Baked Rice with Pork Chop (Tomato Sauce)', 2.5, 'lb'),
(16, 'Orange Juice', 3, 'liter'),
(17, 'Coca Cola', 3, 'liter');

-- --------------------------------------------------------

--
-- Table structure for table `Reservation`
--

CREATE TABLE `Reservation` (
  `BookingID` int(11) NOT NULL,
  `Name` char(50) NOT NULL,
  `MemberID` int(11) DEFAULT NULL,
  `ContactNumber` char(9) NOT NULL,
  `Participant` int(2) NOT NULL,
  `BookingDate` date NOT NULL,
  `StartTime` time NOT NULL,
  `EndTime` time NOT NULL,
  `Room` char(10) DEFAULT NULL,
  `CookeryKitchen` enum('YES','NO') DEFAULT NULL,
  `PhotoTaking` enum('YES','NO') DEFAULT NULL,
  `MenuAAmt` int(2) DEFAULT NULL,
  `MenuBAmt` int(2) DEFAULT NULL,
  `MenuCAmt` int(2) DEFAULT NULL,
  `TotalPrice` int(5) DEFAULT NULL,
  `CardType` enum('MASTER','VISA') DEFAULT NULL,
  `CardNumber` char(19) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Reservation`
--

INSERT INTO `Reservation` (`BookingID`, `Name`, `MemberID`, `ContactNumber`, `Participant`, `BookingDate`, `StartTime`, `EndTime`, `Room`, `CookeryKitchen`, `PhotoTaking`, `MenuAAmt`, `MenuBAmt`, `MenuCAmt`, `TotalPrice`, `CardType`, `CardNumber`) VALUES
(1, 'Hoho Fo', NULL, '2345-6789', 8, '2019-04-05', '09:00:00', '12:00:00', 'Room B', 'NO', 'YES', 0, 1, 0, NULL, NULL, NULL),
(2, 'Ma Jo', NULL, '6748-2678', 12, '2019-04-02', '09:00:00', '14:00:00', 'Room B', 'YES', 'YES', 1, 1, 0, NULL, NULL, NULL),
(3, 'Tai Man', NULL, '5467-3333', 12, '2019-04-17', '08:00:00', '13:00:00', 'Room A', 'YES', 'YES', 0, 0, 0, NULL, NULL, NULL),
(4, 'Martha Chow', NULL, '5215-1414', 20, '2019-04-30', '09:00:00', '17:00:00', 'Room C', 'YES', 'YES', 1, 2, 0, 12700, NULL, NULL),
(5, 'So Ma', NULL, '2548-4755', 10, '2019-04-06', '11:00:00', '16:00:00', 'Room B', 'YES', 'YES', 2, 0, 0, 4150, NULL, NULL),
(6, 'Fin Lau', NULL, '4262-2533', 9, '2019-04-01', '08:00:00', '12:00:00', 'Room C', 'YES', 'NO', 1, 0, 0, 3150, 'MASTER', '-11110'),
(7, 'May Fo', NULL, '4565-2525', 15, '2019-04-02', '00:00:00', '15:00:00', 'Room A', 'YES', 'NO', 1, 1, 0, 9100, 'VISA', '-8462'),
(8, 'Siu Ming', NULL, '1522-1111', 13, '2019-04-05', '13:00:00', '16:00:00', 'Room A', 'NO', 'YES', 0, 0, 1, 3800, 'MASTER', '2222-4444-1111-5252'),
(9, 'Ray Wai', NULL, '4747-5855', 23, '2019-04-14', '09:00:00', '14:00:00', 'Room C', 'NO', 'NO', 1, 0, 1, 9950, 'VISA', '4152-4141-4747-7485'),
(10, 'plz work', NULL, '1111-7777', 17, '2019-04-17', '12:00:00', '19:00:00', 'Room C', 'YES', 'YES', 3, 2, 1, 14300, 'MASTER', '2345-4567-8585-9898'),
(11, 'Bobby Li', NULL, '5675-8777', 15, '2019-04-12', '11:00:00', '14:00:00', 'Room A', 'YES', 'NO', 0, 1, 0, 2950, 'VISA', '7675-9764-4679-8549'),
(12, 'Lolipop Wo', NULL, '5678-8753', 8, '2019-04-06', '16:00:00', '19:00:00', 'Room B', 'NO', 'NO', 0, 1, 0, 2500, 'MASTER', '4567-9865-9876-6565'),
(13, 'Sarah Wong', NULL, '4444-8989', 18, '2019-04-16', '13:00:00', '17:00:00', 'Room B', 'NO', 'YES', 0, 0, 1, 5920, 'MASTER', '5674-9878-9897-9333'),
(14, 'Wai Wai Wong', NULL, '6575-8786', 12, '2019-04-06', '13:00:00', '18:00:00', 'Room A', 'YES', 'NO', 0, 0, 0, 2070, 'VISA', '7373-4443-8784-8784'),
(15, 'Mike M', NULL, '5676-5456', 34, '2019-04-17', '14:00:00', '18:00:00', 'Room B', 'YES', 'NO', 0, 1, 1, 10210, 'MASTER', '7678-8444-9999-0009'),
(16, 'Sofia Ma', NULL, '6543-8697', 36, '2019-04-23', '10:00:00', '15:00:00', 'Room C', 'YES', 'NO', 2, 0, 0, 12450, 'VISA', '5656-8700-8642-6479'),
(17, 'Mishy Le', 1, '2343-7654', 7, '2019-04-18', '08:00:00', '12:00:00', 'Room A', 'YES', 'NO', 0, 0, 0, 1060, 'MASTER', '3454-8787-9898-0000'),
(18, 'Dani Rui', 9, '4567-0000', 14, '2019-04-09', '13:00:00', '18:00:00', 'Room C', 'NO', 'NO', 0, 1, 0, 5500, 'VISA', '5454-9758-9876-8543'),
(19, 'Gigi Lo', NULL, '6445-8657', 20, '2019-04-08', '11:00:00', '17:00:00', 'Room B', 'NO', 'YES', 0, 0, 0, 5600, 'MASTER', '3456-8765-2580-0876'),
(20, 'Mishy Le', 1, '2343-7654', 15, '2019-05-01', '13:00:00', '17:00:00', 'Room B', 'NO', 'NO', 0, 1, 0, 4150, 'MASTER', '4567-4567-8753-7645'),
(21, 'Tyler Ho', 8, '5786-8577', 25, '2019-04-29', '09:00:00', '17:00:00', 'Room C', 'YES', 'YES', 1, 1, 1, 15950, 'MASTER', '6347-4764-8976-8975'),
(22, 'Mario Ma', NULL, '6344-3837', 17, '2019-04-27', '13:00:00', '17:00:00', 'Room A', 'YES', 'YES', 0, 0, 1, 4860, 'MASTER', '5456-8757-8759-4578'),
(23, 'Kiiki', NULL, '2347-4375', 28, '2019-05-07', '09:00:00', '12:00:00', 'Room C', 'YES', 'NO', 0, 0, 0, 5750, 'MASTER', '5656-5454-7485-2594'),
(24, 'Rachel Chow', NULL, '6957-5460', 5, '2019-08-04', '08:00:00', '12:00:00', 'Room A', 'YES', 'YES', 1, 0, 0, 1750, 'VISA', '1313-1212-1313-1313'),
(25, 'Charlie Lau', 10, '1212-7989', 19, '2019-04-28', '10:00:00', '17:00:00', 'Room C', 'YES', 'NO', 1, 0, 1, 10800, 'VISA', '1515-4545-7545-1526'),
(26, 'Charles Wu', 10, '1212-7989', 10, '2019-05-08', '11:00:00', '16:00:00', 'Room A', 'YES', 'YES', 1, 0, 0, 2700, 'MASTER', '4545-4141-4545-4141'),
(27, 'Charles Wu', 10, '1212-7989', 10, '2019-05-09', '11:00:00', '16:00:00', 'Room A', 'YES', 'YES', 1, 0, 0, 2083, 'MASTER', '4545-4545-2635-1212');

-- --------------------------------------------------------

--
-- Table structure for table `Room`
--

CREATE TABLE `Room` (
  `RoomID` int(11) NOT NULL,
  `RoomName` char(10) NOT NULL,
  `Area` int(4) NOT NULL,
  `Capacity` int(3) NOT NULL,
  `Theme` char(30) NOT NULL,
  `ThreeHrPrice` int(3) NOT NULL,
  `ExtraHrPrice` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Room`
--

INSERT INTO `Room` (`RoomID`, `RoomName`, `Area`, `Capacity`, `Theme`, `ThreeHrPrice`, `ExtraHrPrice`) VALUES
(1, 'Room A', 1000, 30, 'Family', 100, 30),
(2, 'Room B', 1500, 45, 'Disco Ball Room', 150, 40),
(3, 'Room C', 2000, 60, 'Industrial Loft', 200, 50);

-- --------------------------------------------------------

--
-- Table structure for table `Staff`
--

CREATE TABLE `Staff` (
  `StaffID` int(11) NOT NULL,
  `Username` char(30) NOT NULL,
  `Password` char(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Staff`
--

INSERT INTO `Staff` (`StaffID`, `Username`, `Password`) VALUES
(1, 'staff', 'staff123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ExtraFacility`
--
ALTER TABLE `ExtraFacility`
  ADD PRIMARY KEY (`FacilityID`);

--
-- Indexes for table `Feedback`
--
ALTER TABLE `Feedback`
  ADD PRIMARY KEY (`FeedbackID`);

--
-- Indexes for table `Member`
--
ALTER TABLE `Member`
  ADD PRIMARY KEY (`MemberID`),
  ADD UNIQUE KEY `Username` (`Username`),
  ADD KEY `ContactNumber` (`ContactNumber`);

--
-- Indexes for table `MenuSetA_6To7`
--
ALTER TABLE `MenuSetA_6To7`
  ADD PRIMARY KEY (`ItemID`);

--
-- Indexes for table `MenuSetB_10To12`
--
ALTER TABLE `MenuSetB_10To12`
  ADD PRIMARY KEY (`ItemID`);

--
-- Indexes for table `MenuSetC_18To22`
--
ALTER TABLE `MenuSetC_18To22`
  ADD PRIMARY KEY (`ItemID`);

--
-- Indexes for table `Reservation`
--
ALTER TABLE `Reservation`
  ADD PRIMARY KEY (`BookingID`),
  ADD KEY `MemberID` (`MemberID`),
  ADD KEY `Room` (`Room`),
  ADD KEY `ContactNumber` (`ContactNumber`);

--
-- Indexes for table `Room`
--
ALTER TABLE `Room`
  ADD PRIMARY KEY (`RoomID`),
  ADD UNIQUE KEY `RoomName` (`RoomName`);

--
-- Indexes for table `Staff`
--
ALTER TABLE `Staff`
  ADD PRIMARY KEY (`StaffID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `ExtraFacility`
--
ALTER TABLE `ExtraFacility`
  MODIFY `FacilityID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `Feedback`
--
ALTER TABLE `Feedback`
  MODIFY `FeedbackID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `Member`
--
ALTER TABLE `Member`
  MODIFY `MemberID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `MenuSetA_6To7`
--
ALTER TABLE `MenuSetA_6To7`
  MODIFY `ItemID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `MenuSetB_10To12`
--
ALTER TABLE `MenuSetB_10To12`
  MODIFY `ItemID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
--
-- AUTO_INCREMENT for table `MenuSetC_18To22`
--
ALTER TABLE `MenuSetC_18To22`
  MODIFY `ItemID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
--
-- AUTO_INCREMENT for table `Reservation`
--
ALTER TABLE `Reservation`
  MODIFY `BookingID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
--
-- AUTO_INCREMENT for table `Room`
--
ALTER TABLE `Room`
  MODIFY `RoomID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `Staff`
--
ALTER TABLE `Staff`
  MODIFY `StaffID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `Reservation`
--
ALTER TABLE `Reservation`
  ADD CONSTRAINT `Reservation_ibfk_1` FOREIGN KEY (`MemberID`) REFERENCES `Member` (`MemberID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Reservation_ibfk_2` FOREIGN KEY (`Room`) REFERENCES `Room` (`RoomName`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
