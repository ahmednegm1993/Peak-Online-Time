With rank_sales as (
select device_type,
sum(user_count) as total_user,
ROW_NUMBER() over (PARTITION By device_type order by sum(user_count) Desc)AS sales_rank,
        CAST(start_timestamp AS VARCHAR) + ' to ' + CAST(end_timestamp AS VARCHAR) AS time_period
from [dbo].[Peak_Online_Time] 
    GROUP BY 
        device_type, start_timestamp, end_timestamp

)
select device_type,total_user,time_period
from rank_sales 
where sales_rank=1
ORDER BY 
device_type,total_user;