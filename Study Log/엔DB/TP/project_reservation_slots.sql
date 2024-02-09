-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	5.6.20

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
-- Table structure for table `reservation_slots`
--

DROP TABLE IF EXISTS `reservation_slots`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservation_slots` (
  `slot_id` int(11) NOT NULL AUTO_INCREMENT,
  `charging_station_id` int(11) NOT NULL,
  `charger_id` int(11) NOT NULL,
  `user_id` varchar(45) NOT NULL,
  `start_datetime` datetime NOT NULL,
  `end_datetime` datetime NOT NULL,
  `status` varchar(45) NOT NULL,
  PRIMARY KEY (`slot_id`),
  KEY `fk_reservation_slots_user` (`user_id`),
  KEY `fk_reservation_slots_charger` (`charging_station_id`,`charger_id`),
  CONSTRAINT `fk_reservation_slots_charger` FOREIGN KEY (`charging_station_id`, `charger_id`) REFERENCES `charging_station` (`station_id`, `chger_id`),
  CONSTRAINT `fk_reservation_slots_charging_station` FOREIGN KEY (`charging_station_id`) REFERENCES `charging_station` (`station_id`),
  CONSTRAINT `fk_reservation_slots_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation_slots`
--

LOCK TABLES `reservation_slots` WRITE;
/*!40000 ALTER TABLE `reservation_slots` DISABLE KEYS */;
INSERT INTO `reservation_slots` VALUES (13,1,1,'seojiwon','2023-12-05 18:00:00','2023-12-05 18:30:00','cancelled');
/*!40000 ALTER TABLE `reservation_slots` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-06  8:50:13
