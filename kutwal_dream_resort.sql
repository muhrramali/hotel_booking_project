-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 25, 2026 at 11:12 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kutwal_dream_resort`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add guest', 7, 'add_guest'),
(26, 'Can change guest', 7, 'change_guest'),
(27, 'Can delete guest', 7, 'delete_guest'),
(28, 'Can view guest', 7, 'view_guest'),
(29, 'Can add room', 8, 'add_room'),
(30, 'Can change room', 8, 'change_room'),
(31, 'Can delete room', 8, 'delete_room'),
(32, 'Can view room', 8, 'view_room'),
(33, 'Can add staff', 9, 'add_staff'),
(34, 'Can change staff', 9, 'change_staff'),
(35, 'Can delete staff', 9, 'delete_staff'),
(36, 'Can view staff', 9, 'view_staff'),
(37, 'Can add reservation', 10, 'add_reservation'),
(38, 'Can change reservation', 10, 'change_reservation'),
(39, 'Can delete reservation', 10, 'delete_reservation'),
(40, 'Can view reservation', 10, 'view_reservation'),
(41, 'Can add payment', 11, 'add_payment'),
(42, 'Can change payment', 11, 'change_payment'),
(43, 'Can delete payment', 11, 'delete_payment'),
(44, 'Can view payment', 11, 'view_payment'),
(45, 'Can add housekeeping log', 12, 'add_housekeepinglog'),
(46, 'Can change housekeeping log', 12, 'change_housekeepinglog'),
(47, 'Can delete housekeeping log', 12, 'delete_housekeepinglog'),
(48, 'Can view housekeeping log', 12, 'view_housekeepinglog');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$A5VfXPFOoT4nvJewlV4h0u$8cLq+ZDU8Jh8iJOHB3/YEln9lls3+6x4izQMDGz+XFY=', '2026-06-08 23:20:26.771505', 1, 'admin', 'Resort', 'Admin', 'admin@kutwaldreamresort.com', 1, 1, '2026-06-06 19:19:32.374917'),
(2, 'pbkdf2_sha256$600000$bb2ne8TIVftIBb6WI8NYLw$QL5k82tiBf0I0h/QDGNLILXKmtj9KPintVXOhwqo9uw=', '2026-06-06 19:24:39.443622', 0, 'ali', 'MUHRRAM', 'ALI', 'muhrram008@gmail.com', 0, 1, '2026-06-06 19:24:38.896803'),
(3, 'pbkdf2_sha256$600000$oreTKAqK9lRLPpmwNAwjBU$cLhCsYyJxDfyH89lz5meHipR2DQOws4RPp8tJcx6RB0=', '2026-06-06 19:32:11.500087', 0, 'waseem', 'abbas', 'abas', 'muhrram009@gmail.com', 0, 1, '2026-06-06 19:32:10.944797'),
(4, 'pbkdf2_sha256$600000$B3S1wQxSycAFmoubScd2em$trrWdgVUCYUmQ8ufyns3wYFwqAVdWxWM5PEmKyPcSYk=', '2026-06-08 22:40:50.076165', 0, 'hussain', 'hussain', 'ali', 'hussaiali123@gmail.com', 0, 1, '2026-06-08 22:40:49.550924');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'hotel', 'guest'),
(12, 'hotel', 'housekeepinglog'),
(11, 'hotel', 'payment'),
(10, 'hotel', 'reservation'),
(8, 'hotel', 'room'),
(9, 'hotel', 'staff'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2026-06-06 19:19:29.773781'),
(2, 'auth', '0001_initial', '2026-06-06 19:19:30.337506'),
(3, 'admin', '0001_initial', '2026-06-06 19:19:30.469055'),
(4, 'admin', '0002_logentry_remove_auto_add', '2026-06-06 19:19:30.477298'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2026-06-06 19:19:30.485860'),
(6, 'contenttypes', '0002_remove_content_type_name', '2026-06-06 19:19:30.586608'),
(7, 'auth', '0002_alter_permission_name_max_length', '2026-06-06 19:19:30.646599'),
(8, 'auth', '0003_alter_user_email_max_length', '2026-06-06 19:19:30.661623'),
(9, 'auth', '0004_alter_user_username_opts', '2026-06-06 19:19:30.669086'),
(10, 'auth', '0005_alter_user_last_login_null', '2026-06-06 19:19:30.721462'),
(11, 'auth', '0006_require_contenttypes_0002', '2026-06-06 19:19:30.725202'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2026-06-06 19:19:30.735209'),
(13, 'auth', '0008_alter_user_username_max_length', '2026-06-06 19:19:30.747562'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2026-06-06 19:19:30.761488'),
(15, 'auth', '0010_alter_group_name_max_length', '2026-06-06 19:19:30.777168'),
(16, 'auth', '0011_update_proxy_permissions', '2026-06-06 19:19:30.785163'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2026-06-06 19:19:30.798527'),
(18, 'hotel', '0001_initial', '2026-06-06 19:19:31.453462'),
(19, 'sessions', '0001_initial', '2026-06-06 19:19:31.503209'),
(20, 'hotel', '0002_guest_name_alter_guest_nationality', '2026-06-08 23:14:29.802631');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('k3uc0r72yfz9npgs40iha54e4vsrs2rl', '.eJxVjDsOwjAQBe_iGlle79qOKek5g7X-4QBKpDipEHeHSCmgfTPzXiLwtraw9bKEMYuzAHH63SKnR5l2kO883WaZ5mldxih3RR60y-ucy_NyuH8HjXv71slXtgbRWgNoiKz2BREpVmJXNIMjH9WgDChWDgDBZKqM2aRBRyri_QGs9zad:1wW1EU:K61873P_1KACl0v-RqIs4jS4EZjr6EQUEws9oK5quOI', '2026-06-21 00:19:18.918043'),
('l1uzfv51ak1qpz7a4rrkplpze6otee41', '.eJxVjDsOwjAQBe_iGlle79qOKek5g7X-4QBKpDipEHeHSCmgfTPzXiLwtraw9bKEMYuzAHH63SKnR5l2kO883WaZ5mldxih3RR60y-ucy_NyuH8HjXv71slXtgbRWgNoiKz2BREpVmJXNIMjH9WgDChWDgDBZKqM2aRBRyri_QGs9zad:1wW15K:TAs5frctdWgUQdceLDjrXZNpkErdMvPFLG4Mo8wWgxs', '2026-06-21 00:09:50.893709'),
('p3qq4gz46wqqdadhsmcbsnsqr6an77ul', '.eJxVjDsOwjAQBe_iGlle79qOKek5g7X-4QBKpDipEHeHSCmgfTPzXiLwtraw9bKEMYuzAHH63SKnR5l2kO883WaZ5mldxih3RR60y-ucy_NyuH8HjXv71slXtgbRWgNoiKz2BREpVmJXNIMjH9WgDChWDgDBZKqM2aRBRyri_QGs9zad:1wW1GG:TCN7uxFVULap9mRIO2mNIfcK_nZ6DvhZe9LBw848Cxs', '2026-06-21 00:21:08.696115');

-- --------------------------------------------------------

--
-- Table structure for table `hotel_guest`
--

CREATE TABLE `hotel_guest` (
  `id` bigint(20) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `cnic` varchar(20) NOT NULL,
  `nationality` varchar(50) NOT NULL,
  `country` varchar(50) NOT NULL,
  `address` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `hotel_guest`
--

INSERT INTO `hotel_guest` (`id`, `first_name`, `last_name`, `gender`, `email`, `phone`, `cnic`, `nationality`, `country`, `address`, `created_at`, `user_id`, `name`) VALUES
(1, 'Ali', 'Hassan', 'Male', 'ali@email.com', '+92 321 0000001', '35201-1234567-1', 'Pakistani', 'Pakistan', '', '2026-06-06 19:19:32.955281', NULL, 'unknown'),
(2, 'Zainab', 'Malik', 'Male', 'zainab@email.com', '+92 322 0000002', '35201-2345678-2', 'Pakistani', 'Pakistan', '', '2026-06-06 19:19:32.959828', NULL, 'unknown'),
(3, 'Usman', 'Tariq', 'Male', 'usman@email.com', '+92 323 0000003', '35201-3456789-3', 'Pakistani', 'Pakistan', '', '2026-06-06 19:19:32.961954', NULL, 'unknown'),
(4, 'hussain', 'ALI', 'Male', 'muhrram008@gmail.com', '03199585990', '7150105171849', 'Pakistani', 'Pakistan', '', '2026-06-06 19:24:39.437804', 2, 'unknown'),
(5, 'abbas', 'abas', 'Male', 'muhrram009@gmail.com', '03199585990', '7150105171848', 'Pakistani', 'Pakistan', '', '2026-06-06 19:32:11.492383', 3, 'unknown'),
(6, 'usman', 'khan', 'Male', 'usmankhan12@gmail.com', '+923199585998', '7150105171846', 'Pakistan', 'Pakistan', '', '2026-06-07 00:07:59.182014', NULL, 'unknown'),
(7, 'Zamin', 'Ali', 'Male', 'muhrram007@gmail.com', '03199585990', '7150105171844', 'Pakistan', 'Pakistan', '', '2026-06-08 22:36:48.610528', NULL, 'unknown'),
(8, 'hussain', 'ali', 'Male', 'hussaiali123@gmail.com', '03199585991', '715010517188', 'Pakistani', 'Pakistan', '', '2026-06-08 22:40:50.066261', 4, 'unknown');

-- --------------------------------------------------------

--
-- Table structure for table `hotel_housekeepinglog`
--

CREATE TABLE `hotel_housekeepinglog` (
  `id` bigint(20) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(20) NOT NULL,
  `notes` varchar(200) NOT NULL,
  `room_id` bigint(20) NOT NULL,
  `staff_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `hotel_housekeepinglog`
--

INSERT INTO `hotel_housekeepinglog` (`id`, `date`, `status`, `notes`, `room_id`, `staff_id`) VALUES
(1, '2026-06-07', 'Done', 'Daily cleaning', 8, 4),
(2, '2026-06-07', 'Pending', 'Post checkout cleaning', 6, NULL),
(3, '2026-06-07', 'Pending', 'Post checkout cleaning', 2, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_payment`
--

CREATE TABLE `hotel_payment` (
  `id` bigint(20) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `method` varchar(30) NOT NULL,
  `status` varchar(20) NOT NULL,
  `transaction_id` varchar(60) NOT NULL,
  `payment_date` date NOT NULL,
  `remarks` varchar(200) NOT NULL,
  `reservation_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `hotel_payment`
--

INSERT INTO `hotel_payment` (`id`, `amount`, `method`, `status`, `transaction_id`, `payment_date`, `remarks`, `reservation_id`) VALUES
(1, 31500.00, 'Cash', 'Paid', '', '2026-06-07', '', 2);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_reservation`
--

CREATE TABLE `hotel_reservation` (
  `id` bigint(20) NOT NULL,
  `check_in` date NOT NULL,
  `check_out` date NOT NULL,
  `num_guests` int(10) UNSIGNED NOT NULL CHECK (`num_guests` >= 0),
  `bed_type` varchar(10) NOT NULL,
  `meal_plan` varchar(20) NOT NULL,
  `status` varchar(20) NOT NULL,
  `notes` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `guest_id` bigint(20) NOT NULL,
  `handled_by_id` bigint(20) DEFAULT NULL,
  `room_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `hotel_reservation`
--

INSERT INTO `hotel_reservation` (`id`, `check_in`, `check_out`, `num_guests`, `bed_type`, `meal_plan`, `status`, `notes`, `created_at`, `guest_id`, `handled_by_id`, `room_id`) VALUES
(1, '2026-06-09', '2026-06-12', 2, 'Double', 'Breakfast', 'Confirmed', '', '2026-06-06 19:19:32.965428', 1, 2, 1),
(2, '2026-06-06', '2026-06-09', 2, 'Double', 'Half Board', 'Checked In', '', '2026-06-06 19:19:32.971678', 2, 2, 5),
(3, '2026-06-14', '2026-06-17', 1, 'Double', 'Room only', 'Confirmed', '', '2026-06-06 19:19:32.983668', 3, NULL, 10),
(4, '2026-06-07', '2026-06-09', 2, 'Double', 'Room only', 'Checked Out', 'i need clean and good room', '2026-06-06 19:25:43.814848', 4, NULL, 2),
(5, '2026-06-08', '2026-06-10', 1, 'Double', 'Full Board', 'Checked Out', '', '2026-06-07 00:07:59.211052', 6, NULL, 6),
(6, '2026-06-10', '2026-06-11', 2, 'Double', 'Full Board', 'Confirmed', 'Need a clean and private room. we will arrive at around 2:30 pm on the mention date.', '2026-06-08 22:36:48.610528', 7, NULL, 2),
(7, '2026-06-09', '2026-06-12', 2, 'Double', 'Full Board', 'Pending', '', '2026-06-08 22:48:11.466010', 4, NULL, 7);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_room`
--

CREATE TABLE `hotel_room` (
  `id` bigint(20) NOT NULL,
  `room_number` varchar(10) NOT NULL,
  `room_type` varchar(30) NOT NULL,
  `floor` int(10) UNSIGNED NOT NULL CHECK (`floor` >= 0),
  `price_per_night` decimal(10,2) NOT NULL,
  `capacity` int(10) UNSIGNED NOT NULL CHECK (`capacity` >= 0),
  `bed_type` varchar(10) NOT NULL,
  `status` varchar(20) NOT NULL,
  `has_wifi` tinyint(1) NOT NULL,
  `has_heater` tinyint(1) NOT NULL,
  `has_view` tinyint(1) NOT NULL,
  `image` varchar(100) NOT NULL,
  `description` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `hotel_room`
--

INSERT INTO `hotel_room` (`id`, `room_number`, `room_type`, `floor`, `price_per_night`, `capacity`, `bed_type`, `status`, `has_wifi`, `has_heater`, `has_view`, `image`, `description`) VALUES
(1, '101', 'Alpine View', 2, 8500.00, 2, 'Double', 'Occupied', 1, 1, 1, 'alpine.jpg', 'Panoramic view of Haramosh peaks'),
(2, '102', 'Alpine View', 2, 8500.00, 2, 'Double', 'Occupied', 1, 1, 1, 'alpine.jpg', 'Mountain-facing balcony'),
(3, '201', 'Deluxe Suite', 2, 12000.00, 3, 'Double', 'Available', 1, 1, 1, 'deluxe.jpg', 'Luxury suite with sitting area'),
(4, '202', 'Deluxe Suite', 2, 12000.00, 4, 'Quad', 'Available', 1, 1, 1, 'deluxe.jpg', 'Family deluxe with fireplace'),
(5, '301', 'Lake Chalet', 3, 10500.00, 2, 'Double', 'Occupied', 1, 1, 1, 'chalet.jpg', 'Steps away from Kutwal Lake trail'),
(6, '302', 'Lake Chalet', 3, 10500.00, 3, 'Triple', 'Available', 1, 1, 1, 'chalet.jpg', 'Lake view chalet with heater'),
(7, '401', 'Valley Room', 1, 6500.00, 2, 'Double', 'Available', 1, 1, 1, 'standard.jpg', 'Cozy valley-facing room'),
(8, '402', 'Valley Room', 1, 6500.00, 2, 'Double', 'Available', 1, 1, 1, 'standard.jpg', 'Budget-friendly mountain room'),
(9, '501', 'Guest Cabin', 1, 7500.00, 4, 'Quad', 'Available', 1, 1, 1, 'chalet.jpg', 'Wooden cabin for groups'),
(10, '601', 'Trekker Room', 1, 4500.00, 1, 'Single', 'Occupied', 1, 1, 1, 'standard.jpg', 'Basic room for solo trekkers');

-- --------------------------------------------------------

--
-- Table structure for table `hotel_staff`
--

CREATE TABLE `hotel_staff` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `role` varchar(30) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `shift` varchar(20) NOT NULL,
  `salary` decimal(10,2) NOT NULL,
  `hired_date` date NOT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `hotel_staff`
--

INSERT INTO `hotel_staff` (`id`, `name`, `role`, `phone`, `email`, `shift`, `salary`, `hired_date`, `user_id`) VALUES
(1, 'Ahmed Khan', 'Manager', '+92 300 1111111', 'ahmed@kutwal.com', 'Morning', 85000.00, '2025-12-09', NULL),
(2, 'Sara Ali', 'Receptionist', '+92 300 2222222', 'sara@kutwal.com', 'Morning', 45000.00, '2025-12-09', NULL),
(3, 'Hassan Raza', 'Trek Guide', '+92 300 3333333', 'hassan@kutwal.com', 'Morning', 55000.00, '2025-12-09', NULL),
(4, 'Fatima Noor', 'Housekeeping', '+92 300 4444444', 'fatima@kutwal.com', 'Morning', 35000.00, '2025-12-09', NULL),
(5, 'Imran Shah', 'Chef', '+92 300 5555555', 'imran@kutwal.com', 'Evening', 50000.00, '2025-12-09', NULL),
(6, 'Jamal Khan', 'Chef', '03199585991', 'muhrram007@gmail.com', 'Night', 69999.80, '2026-06-09', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `hotel_guest`
--
ALTER TABLE `hotel_guest`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `hotel_housekeepinglog`
--
ALTER TABLE `hotel_housekeepinglog`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_housekeepinglog_room_id_808d074b_fk_hotel_room_id` (`room_id`),
  ADD KEY `hotel_housekeepinglog_staff_id_9ac3419d_fk_hotel_staff_id` (`staff_id`);

--
-- Indexes for table `hotel_payment`
--
ALTER TABLE `hotel_payment`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `reservation_id` (`reservation_id`);

--
-- Indexes for table `hotel_reservation`
--
ALTER TABLE `hotel_reservation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hotel_reservation_guest_id_7a07305e_fk_hotel_guest_id` (`guest_id`),
  ADD KEY `hotel_reservation_handled_by_id_b9670183_fk_hotel_staff_id` (`handled_by_id`),
  ADD KEY `hotel_reservation_room_id_da1476cd_fk_hotel_room_id` (`room_id`);

--
-- Indexes for table `hotel_room`
--
ALTER TABLE `hotel_room`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `room_number` (`room_number`);

--
-- Indexes for table `hotel_staff`
--
ALTER TABLE `hotel_staff`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `hotel_guest`
--
ALTER TABLE `hotel_guest`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `hotel_housekeepinglog`
--
ALTER TABLE `hotel_housekeepinglog`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `hotel_payment`
--
ALTER TABLE `hotel_payment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `hotel_reservation`
--
ALTER TABLE `hotel_reservation`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `hotel_room`
--
ALTER TABLE `hotel_room`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `hotel_staff`
--
ALTER TABLE `hotel_staff`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `hotel_guest`
--
ALTER TABLE `hotel_guest`
  ADD CONSTRAINT `hotel_guest_user_id_b2d0f561_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `hotel_housekeepinglog`
--
ALTER TABLE `hotel_housekeepinglog`
  ADD CONSTRAINT `hotel_housekeepinglog_room_id_808d074b_fk_hotel_room_id` FOREIGN KEY (`room_id`) REFERENCES `hotel_room` (`id`),
  ADD CONSTRAINT `hotel_housekeepinglog_staff_id_9ac3419d_fk_hotel_staff_id` FOREIGN KEY (`staff_id`) REFERENCES `hotel_staff` (`id`);

--
-- Constraints for table `hotel_payment`
--
ALTER TABLE `hotel_payment`
  ADD CONSTRAINT `hotel_payment_reservation_id_c53d77de_fk_hotel_reservation_id` FOREIGN KEY (`reservation_id`) REFERENCES `hotel_reservation` (`id`);

--
-- Constraints for table `hotel_reservation`
--
ALTER TABLE `hotel_reservation`
  ADD CONSTRAINT `hotel_reservation_guest_id_7a07305e_fk_hotel_guest_id` FOREIGN KEY (`guest_id`) REFERENCES `hotel_guest` (`id`),
  ADD CONSTRAINT `hotel_reservation_handled_by_id_b9670183_fk_hotel_staff_id` FOREIGN KEY (`handled_by_id`) REFERENCES `hotel_staff` (`id`),
  ADD CONSTRAINT `hotel_reservation_room_id_da1476cd_fk_hotel_room_id` FOREIGN KEY (`room_id`) REFERENCES `hotel_room` (`id`);

--
-- Constraints for table `hotel_staff`
--
ALTER TABLE `hotel_staff`
  ADD CONSTRAINT `hotel_staff_user_id_23eb40dd_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
