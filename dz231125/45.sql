SELECT classroom
from (
		SELECT *,
			MAX(cnt) Over() as max_cnt
		FROM (
				SELECT classroom,
					count(*) as cnt
				from Schedule
				group by classroom
			) as t
	) as t1
where t1.cnt = t1.max_cnt