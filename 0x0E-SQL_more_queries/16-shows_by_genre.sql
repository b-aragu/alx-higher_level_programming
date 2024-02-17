-- a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL in the genre column
SELECT `s`.`title`, `t`.`name`
	FROM `tv_shows` AS `s`
	LEFT JOIN `tv_show_genres` AS `g`
		ON  `s`.`id` = `g`.`show_id`

		LEFT JOIN `tv_genres` AS `t`
			ON `t`.`id` = `g`.`genre_id`
	ORDER BY `s`.`title`, `t`.`name` ASC;
