CREATE TABLE IF NOT EXISTS `icingaweb_group` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(64) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `parent` int(10) unsigned DEFAULT NULL,
  `ctime` timestamp NULL DEFAULT NULL,
  `mtime` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_name` (`name`),
  KEY `fk_icingaweb_group_parent_id` (`parent`),
  CONSTRAINT `fk_icingaweb_group_parent_id` FOREIGN KEY (`parent`) REFERENCES `icingaweb_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `icingaweb_group_membership` (
  `group_id` int(10) unsigned NOT NULL,
  `username` varchar(254) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `ctime` timestamp NULL DEFAULT NULL,
  `mtime` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp(),
  PRIMARY KEY (`group_id`,`username`),
  CONSTRAINT `fk_icingaweb_group_membership_icingaweb_group` FOREIGN KEY (`group_id`) REFERENCES `icingaweb_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `icingaweb_user` (
  `name` varchar(254) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `active` tinyint(1) NOT NULL,
  `password_hash` varbinary(255) NOT NULL,
  `ctime` timestamp NULL DEFAULT NULL,
  `mtime` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp(),
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `icingaweb_user_preference` (
  `username` varchar(254) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `section` varchar(64) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(64) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `value` varchar(255) NOT NULL,
  `ctime` timestamp NULL DEFAULT NULL,
  `mtime` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp(),
  PRIMARY KEY (`username`,`section`,`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
