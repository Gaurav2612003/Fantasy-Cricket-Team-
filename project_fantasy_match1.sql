-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: project_fantasy
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `match1`
--

DROP TABLE IF EXISTS `match1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `match1` (
  `player` varchar(49) DEFAULT NULL,
  `scored` int DEFAULT NULL,
  `faced'` int DEFAULT NULL,
  `fours` int DEFAULT NULL,
  `sixes` int DEFAULT NULL,
  `bowled` int DEFAULT NULL,
  `maiden` int DEFAULT NULL,
  `given` int DEFAULT NULL,
  `wickets` int DEFAULT NULL,
  `Catches` int DEFAULT NULL,
  `Stumping` int DEFAULT NULL,
  `runout` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `match1`
--

LOCK TABLES `match1` WRITE;
/*!40000 ALTER TABLE `match1` DISABLE KEYS */;
INSERT INTO `match1` VALUES ('kohli',105,91,9,7,0,0,0,0,1,0,0),('Shubhman',32,40,2,0,0,0,0,0,0,1,0),('Ruturaj',46,39,1,2,0,0,0,0,0,0,0),('Rahane',77,84,10,2,0,0,0,0,0,0,0),('Dhoni',51,49,1,3,0,0,0,0,0,2,0),('Pandya',7,9,1,0,30,0,27,1,0,0,0),('Jadeja',20,14,0,2,36,0,41,2,0,0,0),('kartik',44,52,5,0,0,0,0,0,0,1,0),('Aksar',45,34,7,1,24,0,28,0,1,0,0),('Ashwin',31,40,4,0,42,0,49,2,0,0,0),('BHuwneshwar',0,0,0,0,54,0,52,3,0,0,0),('Bumrah',0,0,0,0,60,0,58,4,0,0,0),('Shami',0,0,0,0,60,0,63,3,0,0,0),('Deepak',0,0,0,0,60,0,69,2,0,0,1),('Umesh',0,0,0,0,54,0,62,1,2,0,0);
/*!40000 ALTER TABLE `match1` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-27 12:04:25
select * from match1;

