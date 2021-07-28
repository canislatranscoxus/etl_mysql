/*
lz_sepomex_cp table is the landing zone. We do not need any id
*/
drop table if exists lz_sepomex_cp;
CREATE TABLE `lz_sepomex_cp` (
  `d_codigo`        varchar(5)  NOT     NULL,
  `d_asenta`        varchar(60) DEFAULT NULL,
  `d_tipo_asenta`   varchar(25) DEFAULT NULL,
  `D_mnpio`         varchar(25) DEFAULT NULL,
  `d_estado`        varchar(15) DEFAULT NULL,
  `d_ciudad`        varchar(25) DEFAULT NULL,
  `d_CP`            varchar(5)  DEFAULT NULL,
  `c_estado`        varchar(2)  DEFAULT NULL,
  `c_oficina`       varchar(5)  DEFAULT NULL,
  `c_CP`            varchar(5)  DEFAULT NULL,
  `c_tipo_asenta`   varchar(2)  DEFAULT NULL,
  `c_mnpio`         varchar(3)  DEFAULT NULL,
  `id_asenta_cpcons`varchar(4)  DEFAULT NULL,
  `d_zona`          varchar(7)  DEFAULT NULL,
  `c_cve_ciudad`    varchar(2)  DEFAULT NULL
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/* stg_mty_metro_area. This table has the clean data, ready to go.  */
drop table if exists stg_mty_metro_area;
CREATE TABLE `stg_mty_metro_area` (
  `min_cp` varchar(5),
  `max_cp` varchar(5),
  `D_mnpio` varchar(25) DEFAULT NULL
) CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/* This table is usually create with django. But just in case. */
drop table if exists ship_mty_metro_area;
CREATE TABLE `ship_mty_metro_area` (
  `id` int NOT NULL AUTO_INCREMENT,
  `min_cp` varchar(5) NOT NULL,
  `max_cp` varchar(5) NOT NULL,
  `D_mnpio` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
