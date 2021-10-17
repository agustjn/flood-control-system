-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 16-10-2021 a las 16:42:32
-- Versión del servidor: 10.3.31-MariaDB
-- Versión de PHP: 8.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proyecto`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categories`
--

 CREATE DATABASE /*!32312 IF NOT EXISTS*/ `proyecto` /*!40100 DEFAULT CHARACTER SET latin1 */;

 USE `proyecto`;

CREATE TABLE `categories` (
  `id` int(11) NOT NULL,
  `name` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `categories`
--

INSERT INTO `categories` (`id`, `name`) VALUES
(1, 'Bug'),
(2, 'Question');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `configurations`
--

CREATE TABLE `configurations` (
  `id` int(10) UNSIGNED NOT NULL,
  `view_users_id` int(11) UNSIGNED NOT NULL,
  `view_meeting_points_id` int(11) UNSIGNED NOT NULL,
  `view_issues_id` int(11) UNSIGNED NOT NULL,
  `background` varchar(50) NOT NULL,
  `items_per_page` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `configurations`
--

INSERT INTO `configurations` (`id`, `view_users_id`, `view_meeting_points_id`, `view_issues_id`, `background`, `items_per_page`) VALUES
(1, 1, 1, 1, 'bg-info', 15);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `issues`
--

CREATE TABLE `issues` (
  `id` int(11) UNSIGNED NOT NULL,
  `email` varchar(30) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `category_id` int(10) NOT NULL,
  `status_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `issues`
--

INSERT INTO `issues` (`id`, `email`, `description`, `category_id`, `status_id`) VALUES
(1, 'fede@mail.com', 'No puedo iniciar sesi?n correctamente', 1, 1),
(2, 'jose@mail.com', 'El sistema de dice que hay un error', 1, 2),
(4, 'maria@mail.com', 'No tengo acceso al sistema', 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `statuses`
--

CREATE TABLE `statuses` (
  `id` int(11) NOT NULL,
  `name` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `statuses`
--

INSERT INTO `statuses` (`id`, `name`) VALUES
(1, 'New'),
(2, 'Todo'),
(3, 'In progress');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(10) UNSIGNED NOT NULL,
  `email` varchar(30) NOT NULL,
  `usuario` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `configuration_id` int(10) UNSIGNED NOT NULL,
  `activo` tinyint(1) UNSIGNED NOT NULL,
  `created_at` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `email`, `usuario`, `password`, `first_name`, `last_name`, `configuration_id`, `activo`, `created_at`) VALUES
(1, 'admin', 'admin', '123123', 'Cosme', 'Fulanito', 1, 1, '15/10/2021');

-- --------------------------------------------------------
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `points`
--
CREATE TABLE `points` (
  `id` int(10) UNSIGNED NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `direccion` varchar(30) NOT NULL,
  `coordenadas` varchar(30) NOT NULL,
  `estado` varchar(30) NOT NULL,
  `telefono` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


-- --------------------------------------------------------


--
-- Estructura de tabla para la tabla `view_issues`
--

CREATE TABLE `view_issues` (
  `id` int(10) UNSIGNED NOT NULL,
  `sorted_by_column` varchar(30) NOT NULL,
  `sort_type` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `view_issues`
--

INSERT INTO `view_issues` (`id`, `sorted_by_column`, `sort_type`) VALUES
(1, 'fecha_creacion', 'DESC');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `view_meeting_points`
--

CREATE TABLE `view_meeting_points` (
  `id` int(10) UNSIGNED NOT NULL,
  `sorted_by_column` varchar(30) NOT NULL,
  `sort_type` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `view_meeting_points`
--

INSERT INTO `view_meeting_points` (`id`, `sorted_by_column`, `sort_type`) VALUES
(1, 'nombre', 'ASC');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `view_users`
--

CREATE TABLE `view_users` (
  `id` int(10) UNSIGNED NOT NULL,
  `sort_order` varchar(3) NOT NULL,
  `sorted_by_column` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `view_users`
--

INSERT INTO `view_users` (`id`, `sort_order`, `sorted_by_column`) VALUES
(1, 'ASC', 'first_name');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `configurations`
--
ALTER TABLE `configurations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `view_meeting_points_id` (`view_meeting_points_id`) USING BTREE,
  ADD KEY `view_users_id` (`view_users_id`) USING BTREE,
  ADD KEY `view_issues_id` (`view_issues_id`) USING BTREE;

--
-- Indices de la tabla `issues`
--
ALTER TABLE `issues`
  ADD PRIMARY KEY (`id`),
  ADD KEY `category_id` (`category_id`),
  ADD KEY `status_id` (`status_id`);

--
-- Indices de la tabla `statuses`
--
ALTER TABLE `statuses`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `last_name` (`last_name`),
  ADD UNIQUE KEY `usuario` (`usuario`),
  ADD KEY `password` (`password`),
  ADD KEY `first_name` (`first_name`),
  ADD KEY `activo` (`activo`),
  ADD KEY `created_at` (`created_at`),
  ADD KEY `configuration_id` (`configuration_id`);


  --
  -- Indices de la tabla `points`
  --
  ALTER TABLE `points`
    ADD PRIMARY KEY (`id`),
    ADD UNIQUE KEY `nombre` (`nombre`),
    ADD UNIQUE KEY `direccion` (`direccion`),
    ADD KEY `coordenadas` (`coordenadas`),
    ADD KEY `estado` (`estado`),
    ADD KEY `telefono` (`telefono`),
    ADD KEY `email` (`email`);



--
-- Indices de la tabla `view_issues`
--
ALTER TABLE `view_issues`
  ADD PRIMARY KEY (`id`) USING ;

--
-- Indices de la tabla `view_meeting_points`
--
ALTER TABLE `view_meeting_points`
  ADD PRIMARY KEY (`id`),
  ADD KEY `order_by` (`sorted_by_column`),
  ADD KEY `type` (`sort_type`);

--
-- Indices de la tabla `view_users`
--
ALTER TABLE `view_users`
  ADD PRIMARY KEY (`id`),
  ADD KEY `order_by` (`sort_order`),
  ADD KEY `type` (`sorted_by_column`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `configurations`
--
ALTER TABLE `configurations`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `issues`
--
ALTER TABLE `issues`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `statuses`
--
ALTER TABLE `statuses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `points`
--
ALTER TABLE `points`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;


--
-- AUTO_INCREMENT de la tabla `view_issues`
--
ALTER TABLE `view_issues`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `view_meeting_points`
--
ALTER TABLE `view_meeting_points`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `view_users`
--
ALTER TABLE `view_users`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `issues`
--
ALTER TABLE `issues`
  ADD CONSTRAINT `issues_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`),
  ADD CONSTRAINT `issues_ibfk_2` FOREIGN KEY (`status_id`) REFERENCES `statuses` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
