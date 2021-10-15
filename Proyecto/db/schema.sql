    -- MariaDB dump 10.17  Distrib 10.4.7-MariaDB, for debian-linux-gnu (x86_64)
    --
    -- Host: localhost    Database: proyecto
    -- ------------------------------------------------------
    -- Server version	10.4.7-MariaDB-1:10.4.7+maria~bionic

    /*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
    /*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
    /*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
    /*!40101 SET NAMES utf8mb4 */;
    /*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
    /*!40103 SET TIME_ZONE='+00:00' */;
    /*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
    /*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
    /*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
    /*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

    --
    -- Current Database: `proyecto`
    --

    CREATE DATABASE /*!32312 IF NOT EXISTS*/ `proyecto` /*!40100 DEFAULT CHARACTER SET latin1 */;

    USE `proyecto`;

    --
    -- Table structure for table `categories`
    --

    DROP TABLE IF EXISTS `categories`;
    /*!40101 SET @saved_cs_client     = @@character_set_client */;
    /*!40101 SET character_set_client = utf8 */;
    CREATE TABLE `categories` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(30) DEFAULT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
    /*!40101 SET character_set_client = @saved_cs_client */;

    --
    -- Dumping data for table `categories`
    --

    LOCK TABLES `categories` WRITE;
    /*!40000 ALTER TABLE `categories` DISABLE KEYS */;
    INSERT INTO `categories` VALUES (1,'Bug'),(2,'Question');
    /*!40000 ALTER TABLE `categories` ENABLE KEYS */;
    UNLOCK TABLES;

    --
    -- Table structure for table `issues`
    --

    DROP TABLE IF EXISTS `issues`;
    /*!40101 SET @saved_cs_client     = @@character_set_client */;
    /*!40101 SET character_set_client = utf8 */;
    CREATE TABLE `issues` (
      `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
      `email` varchar(30) DEFAULT NULL,
      `description` text DEFAULT NULL,
      `category_id` int(10) NOT NULL,
      `status_id` int(10) NOT NULL,
      PRIMARY KEY (`id`),
      KEY `category_id` (`category_id`),
      KEY `status_id` (`status_id`),
      CONSTRAINT `issues_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`),
      CONSTRAINT `issues_ibfk_2` FOREIGN KEY (`status_id`) REFERENCES `statuses` (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
    /*!40101 SET character_set_client = @saved_cs_client */;

    --
    -- Dumping data for table `issues`
    --

    LOCK TABLES `issues` WRITE;
    /*!40000 ALTER TABLE `issues` DISABLE KEYS */;
    INSERT INTO `issues` VALUES (1,'fede@mail.com','No puedo iniciar sesión correctamente',1,1),(2,'jose@mail.com','El sistema de dice que hay un error',1,2),(4,'maria@mail.com','No tengo acceso al sistema',1,1);
    /*!40000 ALTER TABLE `issues` ENABLE KEYS */;
    UNLOCK TABLES;

    --
    -- Table structure for table `statuses`
    --

    DROP TABLE IF EXISTS `statuses`;
    /*!40101 SET @saved_cs_client     = @@character_set_client */;
    /*!40101 SET character_set_client = utf8 */;
    CREATE TABLE `statuses` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(30) DEFAULT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
    /*!40101 SET character_set_client = @saved_cs_client */;

    --
    -- Dumping data for table `statuses`
    --

    LOCK TABLES `statuses` WRITE;
    /*!40000 ALTER TABLE `statuses` DISABLE KEYS */;
    INSERT INTO `statuses` VALUES (1,'New'),(2,'Todo'),(3,'In progress');
    /*!40000 ALTER TABLE `statuses` ENABLE KEYS */;
    UNLOCK TABLES;

    --
    -- Table structure for table `users`
    --

    DROP TABLE IF EXISTS `users`;
    /*!40101 SET @saved_cs_client     = @@character_set_client */;
    /*!40101 SET character_set_client = utf8 */;
    CREATE TABLE `users` (
      `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
      `email` varchar(30) NOT NULL,
      `usuario` varchar(30) NOT NULL,
      `password` varchar(30) NOT NULL,
      `first_name` varchar(30) NOT NULL,
      `last_name` varchar(30) NOT NULL,
      `configuration_id` int(10) unsigned NOT NULL,
      `activo` TINYINT(1) unsigned NOT NULL,
      `created_at` varchar(30) NOT NULL,
      PRIMARY KEY (`id`),
      UNIQUE KEY `email` (`email`),
      KEY `password` (`password`),
      KEY `first_name` (`first_name`),
      UNIQUE KEY `last_name` (`last_name`),
      UNIQUE KEY `usuario` (`usuario`),
      KEY `activo` (`activo`),
      KEY `created_at` (`created_at`),
      KEY `configuration_id` (`configuration_id`),
      CONSTRAINT `users_ibfk_1` FOREIGN KEY (`configuration_id`) REFERENCES `configurations` (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
    /*!40101 SET character_set_client = @saved_cs_client */;

    --
    -- Dumping data for table `users`
    --

    LOCK TABLES `users` WRITE;
    /*!40000 ALTER TABLE `users` DISABLE KEYS */;
    INSERT INTO `users` VALUES (1,'admin','admin','123123','Cosme','Fulanito',1,1,"15/10/2021");
    /*!40000 ALTER TABLE `users` ENABLE KEYS */;
    UNLOCK TABLES;
    /*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

    /*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
    /*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
    /*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
    /*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
    /*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
    /*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
    /*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

    -- Dump completed on 2019-09-08 21:44:24
    DROP TABLE IF EXISTS `table_user`;
    /*!40101 SET @saved_cs_client     = @@character_set_client */;
    /*!40101 SET character_set_client = utf8 */;
    CREATE TABLE `table_user` (
      `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
      `order_by` varchar(3)  NOT NULL,
      `type` varchar(30)  NOT NULL,
      PRIMARY KEY (`id`),
      KEY `order_by` (`order_by`),
      KEY `type` (`type`)
    ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

    LOCK TABLES `table_user` WRITE;
    /*!40000 ALTER TABLE `table_user` DISABLE KEYS */;
    INSERT INTO `table_user` VALUES (1,"ASC","usuario");
    /*!40000 ALTER TABLE `table_user` ENABLE KEYS */;
    UNLOCK TABLES;

    DROP TABLE IF EXISTS `meeting_points`;
    /*!40101 SET @saved_cs_client     = @@character_set_client */;
    /*!40101 SET character_set_client = utf8 */;
    CREATE TABLE `meeting_points` (
      `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
      `order_by` varchar(3)  NOT NULL,
      `type` varchar(30)  NOT NULL,
      PRIMARY KEY (`id`),
      KEY `order_by` (`order_by`),
      KEY `type` (`type`)
    ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

    LOCK TABLES `meeting_points` WRITE;
    /*!40000 ALTER TABLE `meeting_points` DISABLE KEYS */;
    INSERT INTO `meeting_points` VALUES (1,"ASC","nombre");
    /*!40000 ALTER TABLE `meeting_points` ENABLE KEYS */;
    UNLOCK TABLES;


    DROP TABLE IF EXISTS `configurations`;
    /*!40101 SET @saved_cs_client     = @@character_set_client */;
    /*!40101 SET character_set_client = utf8 */;
    CREATE TABLE `configurations` (
      `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
      `table_user_id` int(10) unsigned NOT NULL,
      `meeting_points_id` int(10) unsigned NOT NULL,
      `issues_id` int(10) unsigned NOT NULL,
      `background` varchar(50) NOT NULL,
      `items_per_page` int(10) unsigned NOT NULL,
      PRIMARY KEY (`id`),
      KEY `items_per_page` (`items_per_page`),
      KEY `table_user_id` (`table_user_id`),
      KEY `meeting_points_id` (`meeting_points_id`),
      KEY `issues_id` (`issues_id`),
      KEY `background` (`background`),
      CONSTRAINT `configurations_1` FOREIGN KEY (`table_user_id`) REFERENCES `table_user` (`id`),
      CONSTRAINT `configurations_2` FOREIGN KEY (`meeting_points_id`) REFERENCES `meeting_points` (`id`),
      CONSTRAINT `configurations_3` FOREIGN KEY (`issues_id`) REFERENCES `issues` (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
    /*!40101 SET character_set_client = @saved_cs_client */;

    LOCK TABLES `configurations` WRITE;
    /*!40000 ALTER TABLE `configurations` DISABLE KEYS */;
    INSERT INTO `configurations` VALUES (1,1,1,1,"bg-light");
    /*!40000 ALTER TABLE `configurations` ENABLE KEYS */;
    UNLOCK TABLES;
